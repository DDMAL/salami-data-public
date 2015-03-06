SALAMI Data Set version 1.1
Released 14 March 2012

Metadata Expansion Pack


~@@@@~

This data is released under a Creative Commons 0 license, effectively dedicating it to the public domain. More information about this dedication and your rights, please see the details here:
http://creativecommons.org/publicdomain/zero/1.0/
http://creativecommons.org/publicdomain/zero/1.0/legalcode

~@@@@~

This extension to the SALAMI data set provides additional metadata for the music files used. The intention is to make it easy to determine what audio file corresponds to each SALAMI ID (the SALAMI ID being the number between 1 and 1655 that identifies each entry in the SALAMI database).

Note that the music files used by SALAMI came from 4 distinct sources: Codaich; the Internet Archive's Live Music Archive; the RWC Music Database; and the Isophonics database. (References for each database follow.) The metadata provided in this release follows a different format for each of the 4 sources. 

~@@@@~

1. Codaich
	The metadata are provided in an iTunes XML file. In addition, a CSV file is provided to show the conversions between the SALAMI ID and the two IDs used in the iTunes XML file. The fields are, respectively: SALAMI ID, Persistent ID; Track ID.
	SALAMI_iTunes_library.xml
	id_index_codaich.csv

~@@@@~

2. Internet Archive
	A CSV file is provided, whose fields are, respectively: SALAMI ID; title; creator; album; URL; file name; length (seconds); bitrate (kBits/sec). Note that metadata from the Internet Archive are not wholly consistent, and so some fields may be inaccurate. For example, a song title may be given as "06" when in fact this is the track number that was incorrectly entered as the title by Internet Archive contributor.
	id_index_internetarchive.csv

~@@@@~

3. RWC
	A CSV file is provided, whose fields are, respectively: SALAMI ID; RWC album code; RWC Database name; disc number; track number. All of this information could be derived from the data already provided with SALAMI here but is included for the user's convenience.
	id_index_rwc.csv

~@@@@~

4. Isophonics
	A CSV file is provided, whose fields are, respectively: SALAMI ID; song title as it appears in the SALAMI database; artist; album; song title; track number. 
	id_index_isophonics.csv

~@@@@~

References

Codaich:
http://jmir.sourceforge.net/index_Codaich.html
C. McKay, D. McEnnis and I. Fujinaga. 2006. A large publicly accessible prototype audio database for music research. Proceedings of the International Conference on Music Information Retrieval. 160--3.

Internet Archive: Live Music Archive:
http://www.archive.org/details/etree

RWC Music Database:
http://staff.aist.go.jp/m.goto/RWC-MDB/
M. Goto. 2004. Development of the RWC Music Database. Proceedings of the International Congress on Acoustics. 553--6.

Isophonics Reference Annotations:
http://isophonics.net/
M. Mauch, C. Cannam, M. Davies, S. Dixon, C. Harte, S. Kolozali, D. Tidhar, M. Sandler. 2010. OMRAS2 Metadata Project 2009. Late-breaking paper, International Conference on Music Information Retrieval.