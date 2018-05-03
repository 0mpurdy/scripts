"""Sync two folders"""

import fileman as fm

start = "."
ignored = ['.git','testvenv']


for path in fm.get_files(".", ignored_dirs=ignored):
    print path
