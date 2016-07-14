#!/usr/bin/env python

# mkobtheme --light white --dark black --active blue --inactive darkgrey
# --box grey --notify yellow --menu orange -w red

import argparse

rc = {}


def parseargs():
    global args
    # Default options:
    light = '#ffffff'
    dark = '#000000'
    active = '#0000ff'
    inactive = '#666666'
    shadow = '#999999'
    box = '#cccccc'
    notify = '#ffcc00'
    warning = '#990000'
    clean = False

    parser = argparse.ArgumentParser(
            prog='mkobtheme',
            description='Make an openbox theme'
            )
    parser.add_argument('-l', '--light', default=light)
    parser.add_argument('-d', '--dark', default=dark)
    parser.add_argument('-a', '--active', default=active)
    parser.add_argument('-i', '--inactive', default=inactive)
    parser.add_argument('-s', '--shadow', default=shadow)
    parser.add_argument('-b', '--box', default=box)
    parser.add_argument('-n', '--notify', default=notify)
    parser.add_argument('-w', '--warning', default=warning)
    parser.add_argument('-m', '--menu')
    parser.add_argument('-C', '--clean', default=clean, action='store_true')

    args = parser.parse_args()


def automatic(hexstring):
    if hexstring.startswith('#'):
        hexstring = hexstring[1:]

    r, g, b = tuple(bytes.fromhex(hexstring))

    if (r * 0.299 + g * 0.587 + b * 0.114) > 186:
        color = 'black'
    else:
        color = 'white'

    return(color)


def print_rc():
    for k in rc:
        print(k + ': ' + rc[k])


def main():
    parseargs()

    number = '0'
    rc['window.client.padding.height'] = number

    number = '2'
    rc['border.width'] = number
    rc['menu.separator.width'] = number

    number = '5'
    rc['menu.overlap'] = number
    rc['padding.height'] = number

    number = '7'
    rc['padding.width'] = number
    rc['window.client.padding.width'] = number
    rc['window.handle.width'] = number

    justify = 'left'
    rc['menu.items.justify'] = justify
    rc['menu.title.text.justify'] = justify
    rc['window.label.text.justify'] = justify

    texture = 'flat solid'
    rc['window.inactive.label.bg'] = texture
    rc['menu.items.active.bg'] = texture
    rc['menu.items.bg'] = texture
    rc['menu.title.bg'] = texture
    rc['osd.bg'] = texture
    rc['osd.hilight.bg'] = texture
    rc['osd.label.bg'] = texture
    rc['osd.unhilight.bg'] = texture
    rc['window.active.grip.bg'] = texture
    rc['window.active.handle.bg'] = texture
    rc['window.active.label.bg'] = texture
    rc['window.active.title.bg'] = texture
    rc['window.inactive.grip.bg'] = texture
    rc['window.inactive.handle.bg'] = texture
    rc['window.inactive.title.bg'] = texture

    texture = 'flat solid border'
    rc['osd.button.focused.bg'] = texture
    rc['osd.button.pressed.bg'] = texture
    rc['osd.button.unpressed.bg'] = texture
    rc['window.active.button.toggled.bg'] = texture
    rc['window.inactive.button.toggled.bg'] = texture
    rc['window.active.button.disabled.bg'] = texture
    rc['window.inactive.button.disabled.bg'] = texture
    rc['window.active.button.pressed.bg'] = texture
    if args.clean:
        texture = 'flat solid'
    rc['window.inactive.button.pressed.bg'] = texture
    rc['window.active.button.unpressed.bg'] = texture
    rc['window.inactive.button.unpressed.bg'] = texture
    rc['window.active.button.hover.bg'] = texture
    rc['window.inactive.button.hover.bg'] = texture

    color = args.light
    rc['osd.button.pressed.box.color'] = color
    rc['window.active.button.disabled.bg.border.color'] = color
    rc['window.active.button.disabled.image.color'] = color
    rc['window.inactive.button.disabled.bg.border.color'] = color
    rc['window.inactive.button.disabled.image.color'] = color

    color = args.dark
    rc['border.color'] = color
    rc['osd.button.focused.box.color'] = color
    rc['window.active.button.toggled.bg.border.color'] = color
    rc['window.active.button.toggled.image.color'] = color
    rc['window.inactive.button.toggled.bg.border.color'] = color
    rc['window.inactive.button.toggled.image.color'] = color
    if args.clean:
        color = args.active
    rc['window.active.button.hover.image.color'] = color
    rc['window.active.button.pressed.image.color'] = color
    rc['window.active.button.unpressed.image.color'] = color
    if args.clean:
        color = args.inactive
    rc['window.inactive.button.hover.image.color'] = color
    rc['window.inactive.button.unpressed.image.color'] = color

    color = args.active
    rc['osd.hilight.bg.color'] = color
    rc['window.active.client.color'] = color
    rc['window.active.grip.bg.color'] = color
    rc['window.active.handle.bg.color'] = color
    rc['window.active.label.bg.color'] = color
    rc['window.active.title.bg.color'] = color
    rc['window.active.title.separator.color'] = color
    rc['window.inactive.button.pressed.bg.color'] = color

    rc['window.active.label.text.color'] = automatic(color)

    color = args.inactive
    rc['menu.title.bg.color'] = color
    rc['window.inactive.client.color'] = color
    rc['window.inactive.grip.bg.color'] = color
    rc['window.inactive.handle.bg.color'] = color
    rc['window.inactive.label.bg.color'] = color
    rc['window.inactive.title.bg.color'] = color
    rc['window.inactive.title.separator.color'] = color
    rc['menu.items.disabled.text.color'] = color

    rc['menu.title.text.color'] = automatic(color)

    color = args.shadow
    rc['osd.button.focused.bg.color'] = color

    rc['osd.button.focused.text.color'] = automatic(color)

    if args.clean:
        color = args.active
    rc['window.active.button.hover.bg.color'] = color
    rc['window.active.button.pressed.bg.color'] = color
    if args.clean:
        color = args.inactive
    rc['window.inactive.button.hover.bg.color'] = color

    color = args.box
    rc['osd.bg.color'] = color
    rc['osd.button.unpressed.bg.color'] = color
    rc['osd.label.bg.color'] = color
    rc['menu.items.bg.color'] = color
    rc['osd.unhilight.bg.color'] = color
    rc['window.inactive.label.text.color'] = color

    rc['menu.items.text.color'] = automatic(color)
    rc['osd.button.unpressed.text.color'] = automatic(color)
    rc['osd.label.text.color'] = automatic(color)

    if args.clean:
        color = args.active
    rc['window.active.button.unpressed.bg.color'] = color
    if args.clean:
        color = args.inactive
    rc['window.inactive.button.unpressed.bg.color'] = color

    color = args.warning
    rc['window.active.button.disabled.bg.color'] = color
    rc['window.inactive.button.disabled.bg.color'] = color

    color = args.notify
    rc['window.active.button.toggled.bg.color'] = color
    rc['window.inactive.button.toggled.bg.color'] = color

    color = args.menu or args.active
    rc['menu.items.active.bg.color'] = color
    rc['osd.button.pressed.bg.color'] = color

    rc['menu.items.active.text.color'] = automatic(color)
    rc['osd.button.pressed.text.color'] = automatic(color)

    print_rc()


if __name__ == '__main__':
    main()
