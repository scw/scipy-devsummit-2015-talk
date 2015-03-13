all:
	pandoc -t revealjs -s slides.md --slide-level 2 --highlight-style=zenburn -H src/style.html -o index.html
	linkchecker index.html
pdf:
	pandoc -o devsummit-2015-scipy-arcgis-presentation.pdf -V fontsize=12pt -V mainfont=Helvetica --latex-engine=xelatex slides.md 
clean:
	rm index.html slides-handout.pdf
