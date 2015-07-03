
#### Here's the stuff that makes the stuff needed for the federalist.

webpages:
	mkdir webpages

input.txt: webpages
	python parseXML.py

#this one is redundant, but just for clarity:
jsoncatalog.txt: webpages
	python parseXML.py

#### Here's the stuff that makes the federalist

federalist:
	git clone http://github.com/Bookworm-Project/BookwormDB federalist
	cd federalist; git checkout master
	mkdir -p federalist/files
	mkdir -p federalist/files/metadata
	mkdir -p federalist/files/texts

federalistdatabase: federalist input.txt jsoncatalog.txt
	cd federalist; git checkout master; make files/metadata/jsoncatalog.txt;
	cd federalist; python scripts/guessAtDerivedCatalog.py
	cd federalist; make all


### And some cleaning methods

clean:
	rm input.txt
	rm jsoncatalog.txt

cleanFederalist:
	rm -f federalist/files/texts/input.txt
	rm -f federalist/files/texts/metadata/jsoncatalog.txt
	rm -f federalist/files/texts/metadata/field_descriptions.json
	cd federalist; make clean;


