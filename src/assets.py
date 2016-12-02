'''
Version 4
'''
def color_sprites(string, clr):
    colors = {
                'black': '\033[0;30m',
                'dark_grey': '\033[1;30m',
                'red': '\033[0;31m',
                'light_red': '\033[1;31m',
                'green': '\033[0;32m',
                'light_green': '\033[1;32m',
                'brown': '\033[0;33m',
                'light_brown': '\033[1;33m',
                'blue': '\033[0;34m',
                'light_blue': '\033[1;34m',
                'purple': '\033[0;35m',
                'light_purple': '\033[1;35m',
                'cyan': '\033[0;36m',
                'light_cyan': '\033[1;36m',
                'light_grey': '\033[0;37m',
                'white': '\033[1;37m',
                'end': '\033[0m'
    }
    return '{0}{1}{2}'.format(colors[clr], string, colors['end'])

sprites = {
    'top_border': color_sprites('▄', 'cyan'),
    'bottom_border': color_sprites('▀', 'cyan'),
    'y_border': color_sprites('█', 'cyan'),
    'ground': ' ',
    'player': '■',
    'enemy': color_sprites('¥', 'light_red'),
    'gold': '*',
    'down': '»',
    'door': color_sprites('∩', 'light_brown')
}

def menu_title():
    title = '''
    ██████╗  ██████╗ ██╗  ██╗██╗  ██╗███████╗ █████╗ ██████╗
    ██╔══██╗██╔═══██╗╚██╗██╔╝██║  ██║██╔════╝██╔══██╗██╔══██╗
    ██████╔╝██║   ██║ ╚███╔╝ ███████║█████╗  ███████║██║  ██║
    ██╔══██╗██║   ██║ ██╔██╗ ██╔══██║██╔══╝  ██╔══██║██║  ██║
    ██████╔╝╚██████╔╝██╔╝ ██╗██║  ██║███████╗██║  ██║██████╔╝
    ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝'''
    state1 = title.split('\n')
    large_title = []
    for i in range(len(state1)):
        state2_split = list(state1[i])
        large_title.append(state2_split)

    return large_title
