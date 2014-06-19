Machine Federalist
==================

This is a set of wrappers around a markup copy of the Federalist papers in XML, one of the classical texts for statistical learning and authorship attribution. The marked-up XML was made by Matthew Jockers; other files (such as the XML to json parser) were done for a graduate reading class led by Ben Schmidt at Northeastern.

There is no official license on this: I suspect you would be safe to treat the Jockers-Witten parts as CC-BY-NC, and the Schmidt parts as public domain.

The Makefile will pull the Bookworm repository and try to build a Bookworm based on the data that you put in. At any time, the current build state of the dev branch can be invoked on any machine against this repo by typing:

``` {sh}
git clone git@github.com:bmschmidt/federalist.git
cd federalist; make federalistdatabase
```

That's useful if you want to know if your system is running Bookworm properly.



Texts are from:

Jockers, Matthew L. and Daniela M. Witten. “A Comparative Study of Machine Learning Methods for Authorship Attribution.” Literary and Linguistic Computing, 25.2, (2010): 215-224.


The full text is below:

> "The text of the Federalist Papers was acquired
> through Project Gutenberg and compared against
> the versions available online at the Avalon Project
> of Yale’s Law School (The Federalist Papers 2009).[8]
> In some cases formatting corrections to the
> Gutenberg texts were made and in all cases the
> boilerplate Gutenberg text was removed before analysis.
> To allow for word and bigram tokenization
> using the scripts developed by the authors, the
> corrected text was first marked up into XML.
> ‘‘Div’’ elements separated each paper and its
> author-related metadata: its title and the status of
> the paper’s authorship (e.g. Madison, Hamilton,
> Jay, Coauthored, Disputed)"
