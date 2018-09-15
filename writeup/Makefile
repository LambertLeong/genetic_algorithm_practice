TEX_SOURCES = $(shell find . -name "*.tex")
BIB_SOURCES = $(shell find . -name "*.bib")

default: leong_lambert_mini_project.pdf

leong_lambert_mini_project.pdf: $(TEX_SOURCES) $(BIB_SOURCES)
	pdflatex mini_project
	#bibtex mini_project
	pdflatex mini_project
	pdflatex mini_project
	@echo "leong_lambert_mini_project.pdf file generated"

clean:
	/bin/rm -f *.aux *.log *.toc  *.blg *.bbl *.lof *.lot
	touch mini_project.tex

