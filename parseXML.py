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


def words(paraset): #quick-n-dirty tokenization
    all = " ".join(paraset)
    all = re.sub("[^A-Za-z]"," ",all) #kill punctuation
    all = re.sub("  +"," ",all) #only one break
    words = all.split(" ")
    return words

def parse(paper):
    out = dict()
    for metadataField in ["title","author"]:
        out[metadataField] = paper.getElementsByTagName(metadataField)[0].childNodes[0].data
    out["paragraphs"] = [n.firstChild.data for n in paper.getElementsByTagName("text")[0].getElementsByTagName("p")]
    out["words"] = words(out["paragraphs"]) 
    return out
    
all = [parse(paper) for paper in papers]


    
output = open("federalist.json","w")

string = json.dumps(all)

output.write(string)

