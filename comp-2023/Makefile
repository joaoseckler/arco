MD=$(wildcard *.md) $(wildcard eps/*.md)
HTML=$(MD:.md=.html)

all: $(HTML)

%.html: %.md templates
	./build.sh $*


