# fixme...
RENDER ?= ../homepage-build/render.py
HTMLS = $(wildcard *.html)
DEST = docroot
DESTHTMLS = $(addprefix $(DEST)/,$(HTMLS))
RENDERFLAGS =

build: $(DESTHTMLS)
	echo 'done'

install: $(DESTHTMLS)
	rsync -raHEAXSP --delete $(DEST)/ $(INSTALLTO)/

$(DESTHTMLS): $(DEST)/%.html: %.html
	$(RENDER) $(RENDERFLAGS) $< $@

clean:
	rm -f $(DESTHTMLS)

.PHONY: build install clean
