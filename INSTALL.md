Install instructions
--------------------

- Install as usual:

        $ ./configure
        $ make
        # make install

- To uninstall:

        # make uninstall

### Or for locally build a Arch Linux packgage:

- Execute:

        $ make pkg
        # pacman -U retrosmart-*.pkg.xz

## Packaging:

- Debian:

        $ ./configure
        $ make dpkg
        # dpkg -i retrosmart-openbox-themes_*_all.deb

- Arch Linux:

You can also install it from AUR. I you have yaourt installed.

        $ yaourt -S retrosmart-openbox-themes

