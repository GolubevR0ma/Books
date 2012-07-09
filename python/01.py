# coding: utf-8
import re
mystr = " ba bdf bla laflfa\n "
print_out = re.sub("^\s+|\n|\r|\s+$", '', mystr)
print mystr
print print_out
