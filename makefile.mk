BASE := retrosmart-openbox
PREFIX= /usr
DESTDIR=''
PROGRAM_NAME := Retrosmart Openbox themes
EXECUTABLE_NAME := $(BASE)-themes
DESCRIPTION := A retrosmart look theme for Openbox window manager.
VERSION := 0.9b
AUTHOR := Manuel Domínguez López
MAIL := mdomlop@gmail.com
LICENSE := GPLv3+
TIMESTAMP = $(shell LC_ALL=C date '+%a, %d %b %Y %T %z')
TEMPDIR := $(shell mktemp -u --suffix .$(EXECUTABLE_NAME))

$(EXECUTABLE_NAME):

ChangeLog: changelog.in
	@echo "$(EXECUTABLE_NAME) ($(VERSION)) unstable; urgency=medium" > $@
	@echo >> $@
	@echo "  * Git build." >> $@
	@echo >> $@
	@echo " -- $(AUTHOR) <$(MAIL)>  $(TIMESTAMP)" >> $@
	@echo >> $@
	@cat $^ >> $@

install:
	install -d -m 755 $(DESTDIR)/$(PREFIX)'/share/themes'
	cp -r $(BASE)-* $(DESTDIR)/$(PREFIX)'/share/themes'
	chown -R root:root $(DESTDIR)/$(PREFIX)'/share/themes'/$(BASE)-*/
	chmod -R u=rwX,go=rX $(DESTDIR)/$(PREFIX)'/share/themes'/$(BASE)-*/
	install -Dm 644 AUTHORS.md $(DESTDIR)/$(PREFIX)/share/doc/$(EXECUTABLE_NAME)/AUTHORS
	install -Dm 644 COPYING $(DESTDIR)/$(PREFIX)/share/licenses/$(EXECUTABLE_NAME)/COPYING
	install -Dm 644 INSTALL.md $(DESTDIR)/$(PREFIX)/share/doc/$(EXECUTABLE_NAME)/INSTALL
	install -Dm 644 README.md $(DESTDIR)/$(PREFIX)/share/doc/$(EXECUTABLE_NAME)/README

uninstall:
	rm -rf $(PREFIX)/share/themes/$(BASE)-*/
	rm -rf $(PREFIX)/share/licenses/$(EXECUTABLE_NAME)/
	rm -rf $(PREFIX)/share/doc/$(EXECUTABLE_NAME)/

clean:
	rm -rf $(BASE)-* /tmp/tmp.*.$(BASE) ChangeLog debian/changelog debian/README debian/files debian/$(EXECUTABLE_NAME) debian/debhelper-build-stamp debian/$(EXECUTABLE_NAME)*

purge: clean
	rm -f makefile
	@echo makefile deleted. Execute configure script to generate it again.

deb: ChangeLog
	cp README.md debian/README
	cp ChangeLog debian/changelog
	fakeroot debian/rules binary
	mv ../$(EXECUTABLE_NAME)_$(VERSION)_all.deb .
	@echo Package done!
	@echo You can install it as root with:
	@echo dpkg -i $(EXECUTABLE_NAME)_$(VERSION)_all.deb

pkg:
	mkdir $(TEMPDIR)
	tar cf $(TEMPDIR)/$(EXECUTABLE_NAME).tar ../$(EXECUTABLE_NAME)
	cp packages/PKGBUILD $(TEMPDIR)/
	cd $(TEMPDIR); makepkg
	cp $(TEMPDIR)/$(EXECUTABLE_NAME)-*.pkg.tar.xz .
	@echo Package done!
	@echo You can install it as root with:
	@echo pacman -U $(EXECUTABLE_NAME)-*.pkg.tar.xz
