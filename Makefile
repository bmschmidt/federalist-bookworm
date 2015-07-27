
#### Here's the stuff that makes the stuff needed for the federalist.

all: input.txt jsoncatalog.txt
# We don't make it easy to guess at field descriptions: should we?
	bookworm build files/metadata/jsoncatalog.txt
	bookworm prep guessAtFieldDescriptions
# If field_descriptions existed, this would be the only thing necessary.
	bookworm build all

webpages:
	mkdir webpages

input.txt: webpages
	python parseXML.py

#this one is redundant, but just for clarity:
jsoncatalog.txt: webpages
	python parseXML.py

#### Here's the stuff that makes the federalist

bookworm.cnf:
	bookworm init


clean: cleanBookworm
	rm -f input.txt
	rm -f jsoncatalog.txt

cleanBookworm:
	rm -f files;
	bookworm build clean


