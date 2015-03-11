SALAMI Data Set version 1.9
11 March 2015

Released as 1.9 11 March 2015
Released as 1.2 25 Sept 2012
Updated (1.1.1) 21 April 2012
Released as 1.1 14 March 2012

~@@@@~

Changes made in update to version 1.9:
-- Now hosted on GitHub
-- Revision history reaches back to raw input from annotators
-- Many, many formatting errors corrected (such as misplaced end times, and annotations erroneously copied into two places). Thanks Thomas Grill and Jan Schlüter for helping to identify errors

Changes made in update to version 1.2:
-- Parsed version of all annotations included

Changes made in update to version 1.1.1:
-- Metadata for Isophonics files were all incorrect (SALAMI ID #1600-1654), and have been changed. Thanks to Florian Kaiser for spotting the errors.

Changes made in update to version 1.1:
-- 28 Isophonics annotation files added (SALAMI ID #1600-1654)
-- Additional metadata files with separate readme

~@@@@~

This data is released under a Creative Commons 0 license, effectively dedicating it to the public domain. More information about this dedication and your rights, please see the details here:
http://creativecommons.org/publicdomain/zero/1.0/
http://creativecommons.org/publicdomain/zero/1.0/legalcode

~@@@@~

However, if publishing work based on this data, we kindly ask you to cite the following paper describing its production and contents:

Jordan B. L. Smith, J. Ashley Burgoyne, Ichiro Fujinaga, David De Roure, and J. Stephen Downie. 2011. Design and creation of a large-scale database of structural annotations. Proceedings of the International Society for Music Information Retrieval Conference. Miami, FL. 555-60.

Detailed documentation, up to date links, and all other information about the SALAMI project can be found at the SALAMI homepage:
http://salami.music.mcgill.ca

~@@@@~

The files included in this data set are:

data.zip               [contains annotation files]
metadata.csv           [describes content of files]
readme.txt             [explains package]
readme_metadata.txt    [explains additional metadata]

Additional metadata files now include:
id_index_codaich.csv
id_index_internetarchive.csv
id_index_isophonics.csv
id_index_rwc.csv
SALAMI_iTunes_library.xml

~@@@@~

Each piece of music has 1 or 2 associated text files, since one or two listeners annotated each piece (in the rare case of piece #78, there are 3 files, to indicate a 3-layer annotation by one listener). The files are all labelled "textfile1.txt" and "textfile2.txt" and organized in directories by their unique SONG_ID.

Brief metadata for the pieces of music used are given in a CSV spreadsheet. The fields are, in order:
SONG_ID, SOURCE, ANNOTATOR1, ANNOTATOR2, SONG_DURATION, SONG_TITLE, ARTIST, ANNOTATION_TIME1, ANNOTATION_TIME2, TEXTFILE1, TEXTFILE2, CLASS, GENRE, SUBMISSION_DATE1, SUBMISSION_DATE2, PRIVACY, XEQS1, XEQS2

The fields indicate:
SONG_ID                   Unique identifier for piece of music
SOURCE                    Either Codaich, IA (Internet Archive), or RWC
ANNOTATOR1                ID number for first annotator
ANNOTATOR2                ID number for second annotator
SONG_DURATION             Duration of the piece, in seconds
SONG_TITLE                Title
ARTIST                    Artist
ANNOTATION_TIME1          Self-reported time to complete annotation for first annotator
ANNOTATION_TIME2          Self-reported time to complete annotation for second annotator
TEXTFILE1                 File path for first annotator's file
TEXTFILE2                 File path for second annotator's file
CLASS                     Broad genre (classical, jazz, popular, world, Live_Music_Archive, or unknown)
GENRE                     Narrow genre
SUBMISSION_DATE1          Date of submission of first annotation
SUBMISSION_DATE2          Date of submission of second annotation
XEQS1                     Was the first annotation converted automatically from X/= notation? X indicates yes; 0 indicates no.
XEQS2                     Was the second annotation converted automatically from X/= notation? X indicates yes; 0 indicates no.

Annotations are provided as a single file in the format in which they were written. To understand how to parse this format, please look up the Annotator's Guide at salami.music.mcgill.ca.

~@@@@~

New for version 1.2: parsed version of annotations.

A Ruby script was used to parse the annotations into separate files for the large-scale music similarity labels, small-scale music similarity labels, and function labels. The script which did the parsing is available on the SALAMI website but is not part of this package. Instrumentation labels are not yet included.

Note that the parsed annotations do not correct any errors in the annotations, which still exist where they may.

~@@@@~

Note that some of the music for which we provide annotations was drawn from the RWC Popular, Classical, Jazz and Genre databases. Information on this music can be found in the following articles:

Masataka Goto, Hiroki Hashiguchi, Takuichi Nishimura, and Ryuichi Oka. 2002. RWC Music Database: Popular, Classical, and Jazz Music Databases. Proceedings of the International Conference on Music Information Retrieval. Paris, France. 287-8.

Masataka Goto, Hiroki Hashiguchi, Takuichi Nishimura, and Ryuichi Oka. 2003. RWC Music Database: Music Genre Database and Musical Instrument Sound Database. Proceedings of the International Conference on Music Information Retrieval. Baltimore, MD. 229-30.





       .+++++~ .                        
     .I$77$OII==+?=.                    
   .7$ZZZZ7Z?=~~+===+                   
  .I$ZZZ$Z?==~=~==~~=+                  
  .7$$ZZ77=+===~~~.~:=                  
  .+ZZ$ZZ?~=~~~:=~=~=?                  
 ...$$7$7~+=~~~~=:=~~:                  
 ....7$7$:=,~:~..::=~.                  
  ..,,~77++++~~~~=?=~                   
   ..:=+IIII:=::~=~.     ....  ..       
      .,~=+=:~+,:..  ..~??=~+++++?.     
          ...      .,,+?=++===++?+?+~.  
           ...?$7$?7?Z+?+===~?=++~=+=.  
       ..:$I+7$7??+~++7II=?+===+?+?~?=. 
      .,$I+II77I??+7??+~??I+?+~++?==~.  
      ,?III?77?$7???+?++?+++I$+++~:.    
      .?77??~?7$7+77?+?++?=:?I+~+.      
      .,77?I++=IZ~?77+?+??=?=???I.      
       .:I?I=~?=I?ZZ77I++=?I?II~ .      
          ~$+I77II7I?I~II+=+?,          
              =?~~..                    
                         


,---.     |              o
`---.,---.|    ,---.,-.-..
    |,---||    ,---|| | ||
`---'`---^`---'`---^` ' '`

Structural Analysis of Large Amounts of Music Information.