THEMENAME='retrosmart'
SUFFIX='-openbox-themes-out'
NAME=$(THEMENAME)$(SUFFIX)
SRCDIR='src'
OUTDIR='.'
PREFIX='/usr'
INSTALLDIR=$(PREFIX)'/share/themes'
export ROOT_DIR=${PWD}

$(NAME): clean build

build:
	mkdir -p $(OUTDIR)/$(NAME)
	cd $(OUTDIR)/$(NAME) && \
	python $(ROOT_DIR)/src/mkobtheme.py $(ROOT_DIR)/src/rc $(ROOT_DIR)/src/mkrc.py
	for i in $(OUTDIR)/$(NAME)/*; \
		do \
		name=`basename "$$i"`; \
		dir=$(OUTDIR)/$(NAME)/$$name/openbox-3; \
		mkdir -p "$$dir"; \
		mv "$$i"/themerc "$$dir"/; \
		cp $(SRCDIR)/pixmaps/* "$$dir"; \
	done

install: uninstall $(NAME)
	install -d -m 755 $(INSTALLDIR)
	cp -r $(OUTDIR)/$(NAME)/* $(INSTALLDIR)
	chown -R root:root $(INSTALLDIR)/$(THEMENAME)-openbox-*/
	chmod -R u=rwX,go=rX $(INSTALLDIR)/$(THEMENAME)-openbox-*/

uninstall:
	rm -Rf $(INSTALLDIR)/$(THEMENAME)-openbox-*/

clean:
	rm -Rf $(OUTDIR)/$(NAME)

togit:
	git add .
	git commit -m "Updated from makefile"
	git push origin
