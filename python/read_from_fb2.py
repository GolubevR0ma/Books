# coding: utf-8
import codecs
input_file = codecs.open('test.fb2', 'r', 'cp1251')

input_text = input_file.read()
out = codecs.open('out.tex', 'w', 'utf-8')
out.write(input_text)
