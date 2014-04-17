
#### Here's the stuff that makes the stuff needed for the bookworm.

input.txt:
	python parseXML.py

#this one is redundant, but just for clarity:
jsoncatalog.txt:
	python parseXML.py


#### Here's the stuff that makes the bookworm

bookworm:
	git clone git@github.com:bmschmidt/Presidio bookworm
	mkdir -p bookworm/files
	mkdir -p bookworm/files/metadata
	mkdir -p bookworm/files/texts

bookworm/files/texts/input.txt: input.txt
	cp $< $@

bookworm/files/metadata/jsoncatalog.txt: jsoncatalog.txt
	cp $< $@

bookwormdatabase: bookworm bookworm/files/texts/input.txt bookworm/files/metadata/jsoncatalog.txt
	cd bookworm; git checkout dev;
	cd bookworm; python scripts/guessAtDerivedCatalog.py
	cd bookworm; make all bookwormName=federalist


### And some cleaning methods

clean:
	rm input.txt
	rm jsoncatalog.txt

cleanBookworm:
	rm -f bookworm/files/texts/input.txt
	rm -f bookworm/files/texts/metadata/jsoncatalog.txt
	rm -f bookworm/files/texts/metadata/field_descriptions.json
	cd bookworm; make clean;


