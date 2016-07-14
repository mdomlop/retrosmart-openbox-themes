THEMENAME='retrosmart'
SUFFIX='-openbox-themes'
NAME=$(THEMENAME)$(SUFFIX)
SRCDIR='src'
OUTDIR='.'
PREFIX='/usr'
INSTALLDIR=$(PREFIX)'/share/themes'

$(NAME): clean
	mkdir -p $(OUTDIR)/$(NAME)
	for i in $(SRCDIR)/$(THEMENAME)-*; \
	    do \
	    name=`basename "$$i"`; \
	    dir=$(OUTDIR)/$(NAME)/$$name/openbox-3; \
	    mkdir -p "$$dir"; \
	    cp "$$i"/themerc "$$dir"/; \
	    cp $(SRCDIR)/pixmaps/* "$$dir"; \
	done


install: uninstall $(NAME)
	cp -r $(OUTDIR)/$(NAME)/* $(INSTALLDIR)
	chown -R root:root $(INSTALLDIR)/$(THEMENAME)-openbox-*/
	chmod -R u=rwX,go=rX $(INSTALLDIR)/$(THEMENAME)-openbox-*/

uninstall:
	rm -Rf $(INSTALLDIR)/$(THEMENAME)-openbox-*/

clean:
	rm -Rf $(OUTDIR)/$(NAME)

