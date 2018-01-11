# Maintainer: Manuel Domínguez López <mdomlop at gmail dot com>

_pkgver_year=2018
_pkgver_month=01
_pkgver_day=09

_name=retrosmart-openbox-themes
_gitname=${_name}-git

pkgname=${_name}-local
pkgver=1b
pkgrel=1
pkgdesc="Retrosmart themes for Openbox"
url="https://github.com/mdomlop/${_name}.git"
source=()
md5sums=('SKIP')
license=('GPL3')
optdepends=('retrosmart-kvantum-theme: The corresponding theme for Kvantum'
            'retrosmart-gtk-themes: The corresponding GTK themes'
            'retrosmart-aurorae-themes: Retrosmart themes for Aurorae'
            'retrosmart-wallpapers: The corresponding backgrounds project'
            'retrosmart-x11-cursors: The corresponding X11 cursor theme'
            'retrosmart-xfwm4-themes: The corresponding XFwm4 themes')
arch=('any')
group=('retrosmart')
conflicts=(${_name} ${_gitname})
provides=($_name)

prepare() {
    cd "$startdir"
    ./configure
    }

build() {
    cd "$startdir"
    make
    }

package() {
    cd "$startdir"
    make install DESTDIR=${pkgdir} PREFIX='/usr'
}
