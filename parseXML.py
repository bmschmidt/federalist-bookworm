#!/usr/bin/python


#Build a JSON version of the federalist papers from Matt Jockers' excellent XML version.

from xml.dom.minidom import parseString
import re
import json

file = open('federalist.papers.xml')
data = file.read()
file.close()
dom = parseString(data)

papers = dom.getElementsByTagName("div")

def parse(paper,papernum):
    out = dict()
    paragraph = 1
    for metadataField in ["title","author"]:
        out[metadataField] = paper.getElementsByTagName(metadataField)[0].childNodes[0].data
    for pargroup in paper.getElementsByTagName("text")[0].getElementsByTagName("p"):
        entry = out
        text = pargroup.firstChild.data
        text = re.sub("[\n\r]","",text)
        entry['filename'] = str(papernum) + "-" + str(paragraph)
        entry['paragraphNumber'] = str(paragraph)
        output.write(entry['filename'] + "\t" + text + "\n")
        jsoncatalog.write(json.dumps(entry) + "\n")
        paragraph += 1
    
output = open("input.txt","w")
jsoncatalog = open("jsoncatalog.txt","w")


n=1
for paper in papers:
    parse(paper,papernum=n)
    n += 1
