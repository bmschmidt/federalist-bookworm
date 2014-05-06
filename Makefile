
#### Here's the stuff that makes the stuff needed for the bookworm.

webpages:
	mkdir webpages
	cat input.txt | perl -ne 'if (m/^(\d+)-(\d+)\t(.*)$$/) {$$doc=$$1;$$par=$$2;$$text=$$3;open(INPUT,">>webpages/$$doc.html"); print INPUT "<p id=p$$2>$$text</p>"}'


input.txt:
	python parseXML.py

#this one is redundant, but just for clarity:
jsoncatalog.txt:
	python parseXML.py

#### Here's the stuff that makes the bookworm

bookworm:
	git clone git@github.com:bmschmidt/Presidio bookworm
	cd bookworm; git checkout lessDiskSpace
	mkdir -p bookworm/files
	mkdir -p bookworm/files/metadata
	mkdir -p bookworm/files/texts

bookworm/files/texts/input.txt: input.txt
	cp $< $@

bookworm/files/metadata/jsoncatalog.txt: jsoncatalog.txt
	cp $< $@

bookworm/bookworm.cnf: bookworm
	python bookworm/scripts/makeConfiguration.py

bookwormdatabase: bookworm bookworm/bookworm.cnf bookworm/files/texts/input.txt bookworm/files/metadata/jsoncatalog.txt
	cd bookworm; git checkout lessDiskSpace;
	cd bookworm; python scripts/guessAtDerivedCatalog.py
	cd bookworm; make all


### And some cleaning methods

clean:
	rm input.txt
	rm jsoncatalog.txt

cleanBookworm:
	rm -f bookworm/files/texts/input.txt
	rm -f bookworm/files/texts/metadata/jsoncatalog.txt
	rm -f bookworm/files/texts/metadata/field_descriptions.json
	cd bookworm; make clean;


