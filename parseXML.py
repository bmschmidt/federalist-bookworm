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

fed_dates = {1:'1787-10-27', 2:'1787-10-31', 3:'1787-11-03', 4:'1787-11-07', 5:'1787-11-10', 6:'1787-11-14', 7:'1787-11-15', 8:'1787-11-20', 9:'1787-11-21', 10:'1787-11-22', 11:'1787-11-24', 12:'1787-11-27', 13:'1787-11-28', 14:'1787-11-30', 15:'1787-12-01', 16:'1787-12-04', 17:'1787-12-05', 18:'1787-12-07', 19:'1787-12-08', 20:'1787-12-11', 21:'1787-12-12', 22:'1787-12-14', 23:'1787-12-18', 24:'1787-12-19', 25:'1787-12-21', 26:'1787-12-22', 27:'1787-12-25', 28:'1787-12-26', 29:'1788-01-09', 30:'1787-12-28', 31:'1788-01-01', 32:'1788-01-02', 33:'1788-01-02', 34:'1788-01-05', 35:'1788-01-05', 36:'1788-01-08', 37:'1788-01-11', 38:'1788-01-12', 39:'1788-01-18', 40:'1788-01-18', 41:'1788-01-19', 42:'1788-01-22', 43:'1788-01-23', 44:'1788-01-25', 45:'1788-01-26', 46:'1788-01-29', 47:'1788-01-30', 48:'1788-02-01', 49:'1788-02-02', 50:'1788-02-05', 51:'1788-02-06', 52:'1788-02-08', 53:'1788-02-09', 54:'1788-02-12', 55:'1788-02-13', 56:'1788-02-16', 57:'1788-02-19', 58:'1788-02-20', 59:'1788-02-22', 60:'1788-02-23', 61:'1788-02-26', 62:'1788-02-27', 63:'1788-03-01', 64:'1788-03-05', 65:'1788-03-07', 66:'1788-03-08', 67:'1788-03-11', 68:'1788-03-12', 69:'1788-03-14', 70:'1788-03-15', 71:'1788-03-18', 72:'1788-03-19', 73:'1788-03-21', 74:'1788-03-25', 75:'1788-03-26', 76:'1788-04-01', 77:'1788-04-02', 78:'1788-05-28', 79:'1788-05-28', 80:'1788-06-21', 81:'1788-06-25', 82:'1788-07-02', 83:'1788-07-05', 84:'1788-07-16', 85:'1788-08-13'}

def parse(paper,papernum):
    outputPage = open("webpages/" + str(papernum) + ".htm","w")
    outputPage.write("<h1>Federalist no. %d</h1>\n" %papernum)
    out = dict()
    out['date'] = fed_dates[papernum]
    out['fedNumber'] = str(papernum)
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
