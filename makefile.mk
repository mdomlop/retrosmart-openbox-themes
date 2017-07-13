BASE := 'retrosmart-openbox'
NAME := $(BASE)-themes
PREFIX := '/usr/local'
TEMPDIR := $(shell mktemp -u --suffix .$(NAME))

$(NAME):

install:
	install -d -m 755 $(PREFIX)'/share/themes'
	cp -r $(BASE)-* $(PREFIX)'/share/themes'
	chown -R root:root $(PREFIX)'/share/themes'/$(BASE)-*/
	chmod -R u=rwX,go=rX $(PREFIX)'/share/themes'/$(BASE)-*/
	install -Dm 644 AUTHORS $(PREFIX)/share/doc/$(NAME)/AUTHORS
	install -Dm 644 COPYING $(PREFIX)/share/licenses/$(NAME)/COPYING
	install -Dm 644 INSTALL $(PREFIX)/share/doc/$(NAME)/INSTALL
	install -Dm 644 README $(PREFIX)/share/doc/$(NAME)/README

uninstall:
	rm -rf $(PREFIX)/share/themes/$(BASE)-*/
	rm -rf $(PREFIX)/share/licenses/$(NAME)/
	rm -rf $(PREFIX)/share/doc/$(NAME)/

clean:
	rm -rf $(BASE)-* /tmp/tmp.*.$(BASE) README.md AUTHORS.md INSTALL.md

purge: clean
	rm -f makefile
	@echo makefile deleted. Execute configure script to generate it again.

pkg:
	mkdir $(TEMPDIR)
	tar cf $(TEMPDIR)/$(NAME).tar ../$(NAME)
	cp packages/PKGBUILD $(TEMPDIR)/
	cd $(TEMPDIR); makepkg
	cp $(TEMPDIR)/$(NAME)-*.pkg.tar.xz .
	@echo Package done!
	@echo You can install it as root with:
	@echo pacman -U $(NAME)-*.pkg.tar.xz
