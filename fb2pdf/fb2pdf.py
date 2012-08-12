#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs, lxml
filename = ur'utopia.fb2'
with codecs.open(filename, encoding='UTF-8') as file_object:
  for line in file_object:
    line = line.rstrip('\n')
    print(line)
