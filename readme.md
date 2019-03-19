SALAMI Data Set version 2.0
===========================

Contents
--------

Each piece of music has 1 or 2 associated text files, since one or two listeners annotated each piece. (In the rare case of piece #78, there are 3 files, to indicate a 3-layer annotation by one listener.) The files are all labelled "textfile1.txt" and "textfile2.txt" and organized in directories by their unique SONG_ID: ```~/annotations/[song_id]/textfile[annotator_number].txt```. Each of these folders contains a subfolder, named ```parsed```, which contains separate files for each layer of the annotation: uppercase letters, lowercase letters, and functions.

Annotations are provided as a single file in the format in which they were written. To understand how to parse this format, please look up the Annotator's Guide at http://ddmal.music.mcgill.ca/research/salami/annotations.

Metadata describing these files, including artist, track name, song duration and information about which annotators described them, are available in ```metadata.csv```. Additional metadata, with specialized fields for each source database, are provided under ```~/metadata```, and described by ```readme_metadata.txt```.


Changelog
---------

Changes made in update to version 2.0 (17 March 2015):

* Added 50% more data! All annotations with SALAMI ID equal to 3 mod 4 were added.
* Metadata files updated to describe new annotated pieces

Changes made in update to version 1.9 (11 March 2015):

* Now hosted on GitHub
* Revision history reaches back to raw input from annotators
* Many, many formatting errors corrected (such as misplaced end times, and annotations erroneously copied into two places). Thanks Thomas Grill and Jan Schlüter for helping to identify errors

Changes made in update to version 1.2 (25 Sept 2012):

* Parsed version of all annotations included

Changes made in update to version 1.1.1 (21 April 2012):

* Metadata for Isophonics files were all incorrect (SALAMI ID #1600-1654), and have been changed. Thanks to Florian Kaiser for spotting the errors.

Changes made in update to version 1.1 (14 March 2012):

* 28 Isophonics annotation files added (SALAMI ID #1600-1654)
* Additional metadata files with separate readme

License
-------

This data is released under a Creative Commons 0 license, effectively dedicating it to the public domain. More information about this dedication and your rights, please see the details here:
http://creativecommons.org/publicdomain/zero/1.0/
http://creativecommons.org/publicdomain/zero/1.0/legalcode

Citing SALAMI
-------------

However, if publishing work based on this data, we kindly ask you to cite the following paper describing its production and contents:

Jordan B. L. Smith, J. Ashley Burgoyne, Ichiro Fujinaga, David De Roure, and J. Stephen Downie. 2011. Design and creation of a large-scale database of structural annotations. *Proceedings of the International Society for Music Information Retrieval Conference*. Miami, FL. 555-60.


Resources
---------

Visit the SALAMI homepage for detailed documentation (like the Annotator's Guide) and all other information about the SALAMI project:
http://ddmal.music.mcgill.ca/research/salami

Visit the SALAMI page under DDMAL's Github for some handy community-written resources for managing SALAMI:
https://github.com/DDMAL/SALAMI

We cannot share the SALAMI audio directly, but we can point you to matching audio files on YouTube. A list of matching items can be found here: https://github.com/jblsmith/matching-salami


References
----------

Some of the music for which we provide annotations was drawn from the RWC Popular, Classical, Jazz and Genre databases. Information on this music can be found in the following articles:

Masataka Goto, Hiroki Hashiguchi, Takuichi Nishimura, and Ryuichi Oka. 2002. RWC Music Database: Popular, Classical, and Jazz Music Databases. *Proceedings of the International Conference on Music Information Retrieval.* Paris, France. 287-8.

Masataka Goto, Hiroki Hashiguchi, Takuichi Nishimura, and Ryuichi Oka. 2003. RWC Music Database: Music Genre Database and Musical Instrument Sound Database. *Proceedings of the International Conference on Music Information Retrieval.* Baltimore, MD. 229-30.

Please consult the RWC website for more details. https://staff.aist.go.jp/m.goto/RWC-MDB/




	
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
