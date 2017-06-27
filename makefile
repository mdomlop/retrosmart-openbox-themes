THEMENAME := 'retrosmart-openbox'
MYSRCDIR='src'
PREFIX='/usr'
INSTALLDIR=$(PREFIX)'/share/themes'
pkgver='0.2.a'
TEMPDIR := $(shell mktemp -u --suffix .$(THEMETHEMENAME))

$(THEMENAME):
	python $(MYSRCDIR)/mkobtheme.py $(MYSRCDIR)/rc $(MYSRCDIR)/mkrc.py $(THEMENAME)
	for i in $(THEMENAME)-*; \
		do \
		mkdir -p "$$i"/openbox-3; \
		mv "$$i"/themerc "$$i"/openbox-3/; \
		cp $(MYSRCDIR)/pixmaps/* "$$i"/openbox-3/; \
	done

install:
	install -d -m 755 $(INSTALLDIR)
	cp -r $(THEMENAME)-* $(INSTALLDIR)
	chown -R root:root $(INSTALLDIR)/$(THEMENAME)-*/
	chmod -R u=rwX,go=rX $(INSTALLDIR)/$(THEMENAME)-*/

uninstall:
	rm -Rf $(INSTALLDIR)/$(THEMENAME)-*/

clean:
	rm -Rf $(THEMENAME)-*

togit: clean
	git add .
	git commit -m 'Updated from makefile'
	git push origin

pacman: clean
	mkdir $(TEMPDIR)
	cp packages/pacman/PKGBUILD $(TEMPDIR)/
	cd $(TEMPDIR); makepkg
	cp $(TEMPDIR)/$(THEMENAME)-*.pkg.tar.xz .
	@echo Package done!
	@echo You can install it as root with:
	@echo pacman -U $(THEMENAME)-*.pkg.tar.xz
