import textwrap

menu_title = 'Main menu'
menu_start = menu_title + ' - '
print(menu_start, end='')

options = ['a', 'b', 'c']
ii = ' '
si = ' ' * len(menu_start)
print('.%s.' %si)
olist = '\n'.join(options)
print(olist)
print(textwrap.fill(olist, initial_indent=ii, subsequent_indent=si, replace_whitespace=False))
