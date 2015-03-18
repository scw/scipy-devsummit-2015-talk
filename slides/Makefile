all:
	pandoc -t revealjs -s slides.md --slide-level 2 --highlight-style=zenburn -H src/style.html -o index.html
check:
	linkchecker --check-extern index.html
pdf:
	pandoc -o devsummit-2015-scipy-arcgis-presentation-handout.pdf -V fontsize=12pt -V mainfont=Helvetica --latex-engine=xelatex slides.md
compress:
	mv ../devsummit-2015-scipy-arcgis-presentation-full.pdf devsummit-2015-scipy-arcgis-presentation-full-uncompressed.pdf
	convert -density 200 -compress jpeg -quality 92 devsummit-2015-scipy-arcgis-presentation-full-uncompressed.pdf compressed.pdf
	mv compressed.pdf ../devsummit-2015-scipy-arcgis-presentation-full.pdf
clean:
	rm index.html devsummit-2015-scipy-arcgis-presentation-handout.pdf
