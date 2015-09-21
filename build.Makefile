# fixme...
RENDER = ../homepage-build/render.py
HTMLS = $(wildcard *.html)
DEST = docroot
DESTHTMLS = $(addprefix $(DEST)/,$(HTMLS))

build: $(DESTHTMLS)
	echo 'done'

install: $(DESTHTMLS)
	rsync -raHEAXSP $(DEST)/ $(INSTALLTO)/

$(DESTHTMLS): $(DEST)/%.html: %.html
	$(RENDER) $< $@

clean:
	rm -f $(DESTHTMLS)

.PHONY: build install clean
