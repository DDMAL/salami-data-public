import numpy as np
import glob
import re
import string
import os

def getFilenames(directory):
    filenames = glob.glob(directory + "/*/textfile*.txt")
    return filenames

def preProcessAnnotation(text):
    times = []
    tags = []
    for line in text:
        # Strip comments, split along tab
        time, tag = line.strip().split("#")[0].split("\t")
        while (time[-1]=='0') and (time[-2]!="."):
            time = time[0:-1]
        # Decimal point handling to make Python the same as Ruby:
        # decimal_places = len(time.split(".")[1])
        # if decimal_places<9:
        #     time += "0" * (9-decimal_places)
        # if decimal_places>9:
        #     time = time[-(decimal_places-9)]
        times += [time]
        # Rule 1: all spaces or commas are separators:
        # tags += [[t for t in re.split('[ ,]*',tag) if t]]
        # Rule 2: comma, with optional space afterwards, is the only acceptable separator:
        tags += [[t.strip() for t in tag.split(",") if t]]
    return times, tags

def parseIntoLayers(tags,basic_tags,valid_uppercase,valid_lowercase,valid_functions):
    lowercase = [[] for t in tags]
    uppercase = [[] for t in tags]
    functions = [[] for t in tags]
    instruments = [[] for t in tags]
    justInstruments = [[] for t in tags]
    errors = []
    for i,timestep in enumerate(tags):
        for tag in timestep:
            # Basic tags are assigned to all the annotations:
            if tag in basic_tags:
                lowercase[i] += [tag]
                uppercase[i] += [tag]
                functions[i] += [tag]
                instruments[i] += [tag]
            # Uppercase, lowercase, and bracket-ended tags go to their respective annotations
            # (uppercase, lowercase, and instruments), and leftovers goes to functions.
            # Note that we ignore all apostrophes (optional prime symbols).
            elif re.sub("'","",tag) in valid_uppercase:
                uppercase[i] += [tag]
            elif re.sub("'","",tag) in valid_lowercase:
                lowercase[i] += [tag]
            elif (tag[0] in "()") or (tag[-1] in "()"):
                instruments[i] += [tag]
                justInstruments[i] += [tag]
            else:
                functions[i] += [tag]
                if tag.lower() not in valid_functions:
                    errors += [[tag, str(i), "unexpected_function"]]
    return lowercase, uppercase, functions, instruments, justInstruments, errors

def snapFunctionsToUppercase(functions,uppercase):
    # The format says that function labels are assumed to be in effect until the next uppercase letter.
    # If a new uppercase letter appears without a function label, then that section has no function label.
    for i in range(len(uppercase)):
        if (uppercase[i]) and not (functions[i]):
            functions[i] += ["no_function"]
    return functions

def annotationPlusTimes(sequence, times):
    zippedSequence = zip(times,sequence)
    trimmedSequence = [z[0] + "\t" + ", ".join(z[1]) for z in zippedSequence if z[1]]
    output = "\n".join(trimmedSequence)
    return output

def writeAnnotations(filename, uppercase=[], lowercase=[], functions=[], instruments=[], instrumentLab=[]):
    basename = os.path.basename(filename).split(".")[0]
    dirname = os.path.dirname(filename)
    savepath = dirname + "/parsed/"
    uppername = savepath + basename + "_uppercase.txt"
    lowername = savepath + basename + "_lowercase.txt"
    functname = savepath + basename + "_functions.txt"
    instrname = savepath + basename + "_instruments.txt"
    instlab = savepath + basename + "_instruments.lab"
    if uppercase:
        with open(uppername, 'w') as f:
            f.write(annotationPlusTimes(uppercase, times))
    if lowercase:
        with open(lowername, 'w') as f:
            f.write(annotationPlusTimes(lowercase, times))
    if functions:
        with open(functname, 'w') as f:
            f.write(annotationPlusTimes(functions, times))
    if instruments:
        with open(instrname, 'w') as f:
            f.write(annotationPlusTimes(instruments, times))
    if instrumentLab:
        with open(instlab, 'w') as f:
            f.write("\n".join(["\t".join(line) for line in instrumentLab]))

def convertInstrumentsToLab(justInstruments,times):
    openTags = {}
    instrumentLab = []
    errors = []
    # For each moment in time:
    for i,line in enumerate(justInstruments):
        now = times[i]
        if i<len(justInstruments[0:-1]):
            soon = times[i+1]
        else:
            soon = times[i]
            # We should never have to use this value of 'soon', of course, but let's just set it in case.
        # Look at the instrument tags (possibly several) in sequence:
        for word in line:
            instr = re.sub("[\(\)]","",word)
            if word[0]=="(":
                # If word already in stack, something is wrong:
                if instr in openTags.keys():
                    print "Re-opening tag that was not closed!"
                    errors += [[now, word, "close_missing_reopen"]]
                # Either way, add it to the open tag stack:
                openTags[instr] = now
            if word[-1]==")":
                # Look for a match in the open tag stack:
                if instr in openTags.keys():
                    instrumentLab += [[openTags[instr], soon, instr]]
                    del openTags[instr]
                else:
                    print "Tag was closed but no open tag could be found!"
                    errors += [[now, word, "open_missing"]]
    # After all the tags have been added, is there anything left in the openTagStack?
    for instr in openTags.keys():
        print "Tag was opened but no close tag could be found!"
        errors += [[openTags[instr], instr, "close_missing"]]
    return instrumentLab, errors

filenames = getFilenames("/Users/jordan/Documents/repositories/salami-data-public/annotations")
# Cut tags sequence into four separate sequences:
# Lowercase, uppercase, function and instrument
# Each sequence also has silence and end tags
basic_tags = ["Silence","silence","End","end"]
valid_uppercase = [A for A in string.ascii_uppercase] +  [A+B for A in string.ascii_uppercase for B in string.ascii_uppercase]
valid_lowercase = [a for a in string.ascii_lowercase] +  [a+b for a in string.ascii_lowercase for b in string.ascii_lowercase]
# A list of intended valid functions, but not using it for now.
valid_functions = ["Break", "Bridge", "Chorus", "Coda", "Development", "Exposition", "Fade-out", "Head", "Instrumental", "Interlude", "Intro", "Main_Theme", "No_function", "Outro", "Post-chorus", "Post-verse", "Pre-Chorus", "Pre-Verse", "Recap", "Secondary_Theme", "Solo", "Theme", "Transition", "Variation", "Verse"]
valid_functions = [item.lower() for item in valid_functions]
allErrors = []
# Do one file:
# filename = filenames[142]
# Do all files:
for filename in filenames:
    print filename
    text = open(filename,'r').readlines()
    times, tags = preProcessAnnotation(text)
    lowercase, uppercase, functions, instruments, justInstruments, errorsFuncs = parseIntoLayers(tags,basic_tags,valid_uppercase,valid_lowercase,valid_functions)
    functions = snapFunctionsToUppercase(functions,uppercase)
    instrumentLab, errorsInsts = convertInstrumentsToLab(justInstruments,times)
    errors = errorsFuncs + errorsInsts
    if len(errors):
        allErrors += [[filename, errors]]
    writeAnnotations(filename, uppercase, lowercase, functions, instruments, instrumentLab)

# List all the errors in an easy-to-read way:
with open("list_of_errors.txt",'w') as f:
    for row in allErrors:
        f.write(row[0] + "\n\t" + "\n\t".join(["\t".join(item) for item in row[1]]) + "\n")
