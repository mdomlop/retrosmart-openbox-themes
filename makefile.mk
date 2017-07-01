NAME := 'retrosmart-openbox'
PREFIX='/usr'
DESTDIR=''
TEMPDIR := $(shell mktemp -u --suffix .$(NAME))

$(NAME):

install:
	install -d -m 755 $(DESTDIR)/$(PREFIX)'/share/themes'
	cp -r $(NAME)-* $(DESTDIR)/$(PREFIX)'/share/themes'
	chown -R root:root $(DESTDIR)/$(PREFIX)'/share/themes'/$(NAME)-*/
	chmod -R u=rwX,go=rX $(DESTDIR)/$(PREFIX)'/share/themes'/$(NAME)-*/
	install -Dm 644 AUTHORS $(DESTDIR)/$(PREFIX)/share/doc/$(NAME)/AUTHORS
	install -Dm 644 COPYING $(DESTDIR)/$(PREFIX)/share/licenses/$(NAME)/COPYING
	install -Dm 644 INSTALL $(DESTDIR)/$(PREFIX)/share/doc/$(NAME)/INSTALL
	install -Dm 644 README $(DESTDIR)/$(PREFIX)/share/doc/$(NAME)/README

uninstall:
	rm -rf $(PREFIX)/share/themes/$(NAME)-*/
	rm -rf $(PREFIX)/share/licenses/$(NAME)/
	rm -rf $(PREFIX)/share/doc/$(NAME)/

clean:
	rm -rf $(NAME)-* /tmp/tmp.*.$(NAME)

purge: clean
	rm -f makefile README.md AUTHORS.md INSTALL.md
	@echo makefile deleted. Execute configure script to generate it again.

togit: purge doc
	git add .
	git commit -m 'Updated from makefile'
	git push origin

pacman: clean
	mkdir $(TEMPDIR)
	cp packages/pacman/PKGBUILD $(TEMPDIR)/
	cd $(TEMPDIR); makepkg
	cp $(TEMPDIR)/$(NAME)-*.pkg.tar.xz .
	@echo Package done!
	@echo You can install it as root with:
	@echo pacman -U $(NAME)-*.pkg.tar.xz

pacman-local: clean
	mkdir $(TEMPDIR)
	tar cf $(TEMPDIR)/$(NAME)-themes.tar ../$(NAME)-themes
	cp packages/pacman/local/PKGBUILD $(TEMPDIR)/
	cd $(TEMPDIR); makepkg
	cp $(TEMPDIR)/$(NAME)-*.pkg.tar.xz .
	@echo Package done!
	@echo You can install it as root with:
	@echo pacman -U $(NAME)-*.pkg.tar.xz
