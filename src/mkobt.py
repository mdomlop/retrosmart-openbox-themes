#!/usr/bin/env python

# mkobt --light white --dark black --active blue --inactive darkgrey
# --box grey --notify yellow --menu orange -w red

import configparser
import os
import argparse

def get_config(configfile):
    ''' Get config from config file. Overwrited by command line options. '''
    # FIXME: Need to validate config
    config = configparser.ConfigParser()
    # Hardcoding default config:
    config['DEFAULT'] = {
            'light':'#ffffff',
            'dark':'#000000',
            'active':'#0000ff',
            'menu':'#0000ff',
            'inactive':'#666666',
            'shadow':'#999999',
            'box':'#cccccc',
            'notify':'#ffcc00',
            'warning':'#990000'
            }
    # Get config from config. Works although conf file does not exists:
    config.read(configfile)

    return(config)


def automatic(hexstring):
    if hexstring.startswith('#'):
        hexstring = hexstring[1:]

    r, g, b = tuple(bytes.fromhex(hexstring))

    if (r * 0.299 + g * 0.587 + b * 0.114) > 140:  # 186 # 140
        color = 'black'
    else:
        color = 'white'

    return(color)


def write_rc(theme, directory, nobuttons):
    rc = {}

    number = '0'
    rc['window.client.padding.height'] = number

    border = theme['border']
    rc['border.width'] = border
    rc['menu.separator.width'] = border

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
    if nobuttons:
        texture = 'flat solid'
    rc['window.active.button.pressed.bg'] = texture
    rc['window.inactive.button.pressed.bg'] = texture
    rc['window.active.button.unpressed.bg'] = texture
    rc['window.inactive.button.unpressed.bg'] = texture
    rc['window.active.button.hover.bg'] = texture
    rc['window.inactive.button.hover.bg'] = texture

    color = theme['light']
    rc['osd.button.pressed.box.color'] = color
    rc['window.active.button.disabled.bg.border.color'] = color
    rc['window.active.button.disabled.image.color'] = color
    rc['window.inactive.button.disabled.bg.border.color'] = color
    rc['window.inactive.button.disabled.image.color'] = color

    color = theme['dark']
    rc['border.color'] = color
    rc['osd.button.focused.box.color'] = color
    rc['window.active.button.toggled.bg.border.color'] = color
    rc['window.active.button.toggled.image.color'] = color
    rc['window.inactive.button.toggled.bg.border.color'] = color
    rc['window.inactive.button.toggled.image.color'] = color
    if nobuttons:
        color = theme['active']
    rc['window.active.button.hover.image.color'] = color
    rc['window.active.button.pressed.image.color'] = color
    rc['window.active.button.unpressed.image.color'] = color
    if nobuttons:
        color = theme['inactive']
    rc['window.inactive.button.hover.image.color'] = color
    rc['window.inactive.button.unpressed.image.color'] = color

    color = theme['active']
    rc['osd.hilight.bg.color'] = color
    rc['window.active.client.color'] = color
    rc['window.active.grip.bg.color'] = color
    rc['window.active.handle.bg.color'] = color
    rc['window.active.label.bg.color'] = color
    rc['window.active.title.bg.color'] = color
    rc['window.active.title.separator.color'] = color
    rc['window.inactive.button.pressed.bg.color'] = color

    rc['window.active.label.text.color'] = automatic(color)

    color = theme['inactive']
    rc['menu.title.bg.color'] = color
    rc['window.inactive.client.color'] = color
    rc['window.inactive.grip.bg.color'] = color
    rc['window.inactive.handle.bg.color'] = color
    rc['window.inactive.label.bg.color'] = color
    rc['window.inactive.title.bg.color'] = color
    rc['window.inactive.title.separator.color'] = color
    rc['menu.items.disabled.text.color'] = color

    rc['menu.title.text.color'] = automatic(color)

    color = theme['shadow']
    rc['osd.button.focused.bg.color'] = color

    rc['osd.button.focused.text.color'] = automatic(color)

    if nobuttons:
        color = theme['active']
    rc['window.active.button.hover.bg.color'] = color
    rc['window.active.button.pressed.bg.color'] = color
    if nobuttons:
        color = theme['inactive']
    rc['window.inactive.button.hover.bg.color'] = color

    color = theme['box']
    rc['osd.bg.color'] = color
    rc['osd.button.unpressed.bg.color'] = color
    rc['osd.label.bg.color'] = color
    rc['menu.items.bg.color'] = color
    rc['osd.unhilight.bg.color'] = color
    rc['window.inactive.label.text.color'] = color

    rc['menu.items.text.color'] = automatic(color)
    rc['osd.button.unpressed.text.color'] = automatic(color)
    rc['osd.label.text.color'] = automatic(color)

    if nobuttons:
        color = theme['active']
    rc['window.active.button.unpressed.bg.color'] = color
    if nobuttons:
        color = theme['inactive']
    rc['window.inactive.button.unpressed.bg.color'] = color

    color = theme['warning']
    rc['window.active.button.disabled.bg.color'] = color
    rc['window.inactive.button.disabled.bg.color'] = color

    color = theme['notify']
    rc['window.active.button.toggled.bg.color'] = color
    rc['window.inactive.button.toggled.bg.color'] = color

    color = theme['menu'] or theme['active']
    rc['menu.items.active.bg.color'] = color
    rc['osd.button.pressed.bg.color'] = color

    rc['menu.items.active.text.color'] = automatic(color)
    rc['osd.button.pressed.text.color'] = automatic(color)

    themerc = os.path.join(directory, 'themerc')
    with open(themerc, 'w') as t:
        for k in rc:
            print(k + ': ' + rc[k], file=t)
        t.close()

def install_icons(orig, dest):
    os.makedirs(dest)
    for i in os.listdir(orig):
        o = os.path.join(orig, i)
        d = os.path.join(dest, i)
        with open(o, 'r') as src, open(d, 'w') as  dst:
            for j in open(os.path.join(orig, i), 'r'):
                print(j, end='', file=dst)
            src.close()
            dst.close()


def parseargs():
    ''' Parse arguments from command line. '''
    # Default options:
    config = 'theme.ini'  # Configuration file
    theme = 'DEFAULT'
    name = 'retrosmart-openbox'
    icons = 'pixmaps'
    ALL = False
    clean = False

    parser = argparse.ArgumentParser(
            prog='mkobt',
            description='Makes Openbox themes'
            )

    parser.add_argument('-c', '--config', default=config)
    parser.add_argument('-n', '--name', default=name)
    parser.add_argument('-t', '--theme', default=theme)
    parser.add_argument('-i', '--icons', default=icons)
    parser.add_argument('-a', '--all', default=ALL, action='store_true')
    parser.add_argument('-C', '--clean', default=clean, action='store_true')

    return(parser.parse_args())


def main():
    theme = {}
    settings = parseargs()
    config = get_config(settings.config)

    if settings.all:
        for i in config.sections():
            for j in config[i]:
                theme[j] = config[i][j]
            if settings.clean:
                directory = os.path.join(settings.name + '-' + i + '-clean', 'openbox-3')
            else:
                directory = os.path.join(settings.name + '-' + i, 'openbox-3')
            install_icons(settings.icons, directory)
            write_rc(theme, directory, settings.clean)
    else:
        for i in config[settings.theme]:
            theme[i] = config[settings.theme][i]

        if settings.clean:
            directory = os.path.join(settings.name + '-' + settings.theme + '-clean', 'openbox-3')
        else:
            directory = os.path.join(settings.name + '-' + settings.theme, 'openbox-3')
        install_icons(settings.icons, directory)
        write_rc(theme, directory, settings.clean)



if __name__ == '__main__':
    main()
