.PHONY: all clean view

THIS=Intro_To_Microservices
FINAL=../FinalSlides/$(THIS).pdf

all: slides.pdf

%.tex: %.md
	wiki2beamer  $< > $@

SECTIONS = intro.tex 
TEMPLATE = header.png beamerthemeVlad.sty beamerouterthemeVlad.sty

clean:
	-rm -f slides.aux $(SECTIONS)
	-rm -f *.aux 
	-rm -f *.log 
	-rm -f *.nav 
	-rm -f *.out 
	-rm -f *.snm 
	-rm -f *.toc 
	-rm -f slides.pdf 

slides.pdf: slides.tex  $(SECTIONS) $(TEMPLATE)
	pdflatex  slides
	pdflatex  slides

view: slides.pdf
	evince slides.pdf

view: slides.pdf
	evince slides.pdf
