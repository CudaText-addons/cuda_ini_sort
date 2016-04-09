#Author: Alexey T.
#License: MIT

from cudatext import *
from .sort_ini import *

def do_sort(and_keys):
    lines = ed.get_text_all().splitlines()
    if not lines: return
    lines = do_sort_ini_lines(lines, and_keys)
    if not lines: return
    ed.set_text_all('\n'.join(lines))
    ed.set_caret(0, 0)
    msg_status('Sorted ini lines')
        

class Command:
    def sort_all(self):
        do_sort(True)
    def sort_not_keys(self):
        do_sort(False)
        
