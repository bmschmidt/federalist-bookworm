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
    outputPage = open("webpages/" + str(papernum) + ".htm","w")
    outputPage.write("<h1>Federalist no. %d</h1>\n" %papernum)
    out = dict()
    paragraph = 1
    for metadataField in ["title","author"]:
        out[metadataField] = paper.getElementsByTagName(metadataField)[0].childNodes[0].data
    for pargroup in paper.getElementsByTagName("text")[0].getElementsByTagName("p"):
        entry = out
        text = pargroup.firstChild.data
        if len(text) > 0:
            text = re.sub("[\n\r]","",text)
            outputPage.write("\n<div id=%d><b>%d</b>: %s</div>\n" %(paragraph,paragraph,text))
            entry['filename'] = str(papernum) + "-" + str(paragraph)
            entry['paragraphNumber'] = str(paragraph)
            author = entry['author']
            entry['searchstring'] = "<a href=http://bmschmidt.github.io/federalist-bookworm/%(papernum)d.htm#%(paragraph)d>Federalist no. %(papernum)d (%(author)s)paragraph %(paragraph)d</a>" %(locals())
            output.write(entry['filename'] + "\t" + text + "\n")
            jsoncatalog.write(json.dumps(entry) + "\n")
            paragraph += 1
    outputPage.write("<div></em>Thanks to Daniela Witten and Matthew Jockers for sharing the marked-up XML text of this document</div></div>")

output = open("input.txt","w")
jsoncatalog = open("jsoncatalog.txt","w")


n=1
for paper in papers:
    parse(paper,papernum=n)
    n += 1
