Metadata Information
====================

This file explains the various metadata files that accompany the SALAMI annotation data set. It does not explain how the annotations themselves are formatted, which is explained in the Annotator's Guide, availble at http://salami.music.mcgill.ca.


Metadata descriptions
---------------------

##### ```metadata.csv```

This is the main metadata file and describes all the pieces in the collection.

The fields are:

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


The remaining metadata files are intended to make it easier to determine what audio file corresponds to each ```SONG_ID``` (the ```SONG_ID``` being the number between 1 and 1655 that identifies each entry in the SALAMI database).

The music files used by SALAMI came from 4 distinct sources: Codaich; the Internet Archive's Live Music Archive; the RWC Music Database; and the Isophonics database. (References for each database follow.) Hence, we have 4 separate metadata files provided information relevant to each dataset.

##### Codaich: ```id_index_codaich.csv```, ```SALAMI_iTunes_library.xml```

The metadata are provided in an iTunes XML file. In addition, a CSV file is provided to show the conversions between the SALAMI ID and the two IDs used in the iTunes XML file.

The fields are:

	SONG_ID                   Unique identifier for piece of music
	Persistent ID			  Identifier provided by iTunes
	Track ID				  Identifier provided by iTunes
	


##### Internet Archive: ```id_index_internetarchive.csv```

The fields are:

	SONG_ID                   Unique identifier for piece of music
	TITLE  					  Song title
	ARTIST					  Artist
	ALBUM					  Album (usually the name of the set, including the date and location)
	URL						  Original URL where audio file was downloaded
	FILE_NAME				  File name in SALAMI database including character substitutions
	SONG_DURATION             Duration of the piece, in seconds
	BITRATE					  Audio file bitrate, in kBits/sec
	
These metadata were culled automatically from the Internet Archive and are not entirely consistent, so some of these fields may be inaccurate. For example, a song title may be given as "06" when in fact this is the track number that was incorrectly entered as the title by Internet Archive contributor.

##### RWC: ```id_index_rwc.csv```

The fields are:

	SONG_ID                   Unique identifier for piece of music
	RWC_ID					  Name of the track within the RWC namespace
	GENRE					  Genre according to RWC origin
	CAT_SUFFIX				  Disc number
	TRACK_NUMBER			  Track number
	TITLE  					  Song title
	ARTIST					  Artist
	

##### Isophonics: ```id_index_isophonics.csv```

The fields are:

	SONG_ID                   Unique identifier for piece of music
	TITLE_IN_SALAMI			  File name in SALAMI database including character substitutions
	ARTIST					  Artist
	ALBUM					  Album title
	TITLE  					  Song title
	TRACK_NUMBER			  Track number


License
-------

This data is released under a Creative Commons 0 license, effectively dedicating it to the public domain. More information about this dedication and your rights, please see the details here:
http://creativecommons.org/publicdomain/zero/1.0/
http://creativecommons.org/publicdomain/zero/1.0/legalcode



References
----------

#####Codaich
http://jmir.sourceforge.net/index_Codaich.html
C. McKay, D. McEnnis and I. Fujinaga. 2006. A large publicly accessible prototype audio database for music research. *Proceedings of the International Conference on Music Information Retrieval.* 160--3.

#####Internet Archive; Live Music Archive
http://www.archive.org/details/etree

#####RWC Music Database
http://staff.aist.go.jp/m.goto/RWC-MDB/
M. Goto. 2004. Development of the RWC Music Database. *Proceedings of the International Congress on Acoustics.* 553--6.

#####Isophonics Reference Annotations
http://isophonics.net/
M. Mauch, C. Cannam, M. Davies, S. Dixon, C. Harte, S. Kolozali, D. Tidhar, M. Sandler. 2010. OMRAS2 Metadata Project 2009. Late-breaking paper,* International Conference on Music Information Retrieval.*