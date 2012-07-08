# coding: utf-8
import re
mystr = " balaflfa\n "
print_out = re.sub("^\s+|\n|\r|\s+$", '', mystr)
print mystr
print print_out
