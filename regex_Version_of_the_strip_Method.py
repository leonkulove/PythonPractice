#!python3
# this sample is copied from
# https://stackoverflow.com/questions/34954040/chapter-7-automate-the-boring-stuff-with-python-practice-project-regex-versio

import re


def String(Orii, Argg=''):
    if Argg == '':
        regex1 = re.compile(r'^(\s+)')
        mo = regex1.sub('', Orii)
        regex2 = re.compile(r'(\s+)$')
        mo = regex2.sub('', mo)
        print(mo)
    else:
        AA = re.compile(Argg)
        BB = AA.sub('', Orii)
        print(BB)


text = '        So, you can create the illusion of smooth motion        '
String(text, 'e')
String(text)
