def get_timepoints(annotation)
  list_of_boundaries = []
  annotation.each do |line|
    list_of_boundaries.push(line.split("\t")[0])
  end
  return list_of_boundaries
end

def next_larger_time(on,list)
  onset = on.to_f
  i = 0
  offer = list[i].to_f
  until onset < offer do
    i+=1
    offer = list[i].to_f
  end
  offset = list[i]
  return offset
end

def zipper(array)
  string = ""
  array.each do |line|
    string += line.join("\t") + "\n"
  end
  return string.chomp
end

def parse_arguments(ann_list)
  lowercase = []
  uppercase = []
  instruments = []
  functions = []
  musts = ["end", "silence", "End", "Silence"]
  uppers = 'A'..'Z'
  lowers = 'a'..'zz'
  ann_list.each do |line|
    # Split all the arguments of the annotation into separate parts.
    # Annotations may ONLY consist of letters and brackets.
    bits = line[1]
    time = line[0]
    bits.each do |bit|
      if bit.delete("'`").length<=2 then
        # It is a letter! Check case:
        if uppers.include?(bit.delete("'`")) then
          uppercase << [time, bit]
        elsif lowers.include?(bit.delete("'`")) then
          lowercase << [time, bit]
        end
      elsif !bit.index(/[(\A\()(\)\Z)]/).nil? then
        # It's an instrument label!
        instruments << [time, bit]
      elsif musts.include?(bit) then
        # It's a beginning or ending tag, and we want these in all layers.
        uppercase << [time, bit]
        lowercase << [time, bit]
        instruments << [time, bit]
        functions << [time, bit]
      else
        # It must be a function label then.
        functions << [time, bit]
      end
    end
  end
  return uppercase, lowercase, functions, instruments
end

#### MAIN

# Usage:
# ruby get_sections_sept_2012.rb inputfilename.txt
# 
# Output is parsed version of lab file in the following files:
# "inputfilename_uppercase.txt", "inputfilename_lowercase.txt",
# "inputfilename_functions.txt", "inputfilename_instrumentation.lab",
# "inputfilename_instrumentation.txt"

# 1. Read the input file:
begin
  a = File.open(ARGV[0],'r')
rescue
  puts "Filename not valid. Try again.\n"
end

b = a.readlines
a.close()

# 2. Clean the annotation if necessary: delete lines beginning with # (comments) and with \n (empty lines), as well as lines with no label.
c = b.join
c.gsub!(/\#.*\n/, "\n")
c.gsub!(/\t /, "\t")
c.gsub!(/\n{1,}/, "\n")
c.gsub!(/\A\n/,"")
c.gsub!(/\n[0-9]*\.[0-9]*\n/,"\n")
annotation = c.split("\n")

# 3. Generate a list of boundaries.
list_of_boundaries = get_timepoints(annotation)
array = []
annotation.each_with_index do |line, index|
  array[index] = [line.split("\t")[0].to_f]
  array[index] << line.split("\t")[1].chomp.gsub(" ", "").split(",")
end

# Verify the beginning and ending are formatted correctly. Throw an error if not.
if array[0][0]!=0 || (array[0][1]!=["silence"] && array[0][1]!=["Silence"]) then
  array.insert(0, [0.0, ["silence"]])
  puts "ERROR: song #{ARGV[0]} didn't begin with silence!"
end
if (array[-1][1]!=["end"] && array[-1][1]!=["End"])then
  array.insert(-1, [array[-1][0], ["end"]])
  puts "ERROR: song #{ARGV[0]} didn't end!"
end

# 4. Generate a list of letter labels and their respective onset times. Include 'silence' and the 'end' label, even though Matlab will ignore the 'end' label. Also generate a list of function labels and of instrument tags.
uppercase, lowercase, functions, instruments = parse_arguments(array)

# arrays containing Small and Big boundary times: 
sbounds = lowercase.map {|line| line[0]}
bbounds = uppercase.map {|line| line[0]}

# If a new uppercase section starts and no function is specified, any previous function label ends.
if !functions.empty? then
  # check functions against uppercase
  uppercase.each do |line|
    if !functions.transpose[0].include?(line[0]) then
      functions << [line[0], "no_function"]
    end
  end
end
functions.sort!



# Future work: analyze instruments layer properly and turn it into a set of timespans.
# This step will involve discovering and fixing all the errors in the instrumentation layer of the annotations.

# Save the layers!
filename = ARGV[0]
if !ARGV[1].nil? then
  filename = ARGV[1]
end
outdir = filename.split("/")[0..-2].join("/") + "/parsed"
system("mkdir "+outdir)

filearray = ["uppercase.txt", "lowercase.txt", "functions.txt"]
descriptions = [zipper(uppercase), zipper(lowercase), zipper(functions)]

descriptions.each_index do |indx|
    outfile = File.open(outdir + "/" + filename.split("/")[-1].split(".")[0] + "_" + filearray[indx], 'w')
    outfile.write(descriptions[indx])
    outfile.close
end