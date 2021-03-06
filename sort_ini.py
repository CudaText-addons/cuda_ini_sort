﻿__version__ = '$Id: sort_ini.py 543 2008-12-19 13:44:59Z mn $'
# author: Michal Niklas
# adapted to Cudatext: Alexey T.

def do_sort_ini_lines(lines, and_keys):
    section = ''
    sections = {}
    for line in lines:
        line = line.strip()
        if line:
            if line.startswith('['):
                section = line
                continue
            if section:
                try:
                    sections[section].append(line)
                except KeyError:
                    sections[section] = [line, ]
    if sections:
        res = []   
        sk = list(sections.keys())
        sk.sort()
        for k in sk:
            vals = sections[k]
            if and_keys:
                vals.sort()
            res += [k]
            res += vals
            res += ['']
        return res
        
