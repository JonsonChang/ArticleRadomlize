# -*- coding: utf-8 -*-
# coding=UTF-8
import random
import codecs

fin = open('input.txt', 'r')
article = fin.read()


def my_split(str, c):
    tmp = str.split(c)
    return tmp


def list_split(alist, c):
    tmp = []
    for line in alist:
        tmp.extend(my_split(line, c))
    return tmp


def randomlize(alist):
    tmp = []
    blist = alist
    while len(blist) > 0:
        lenght = len(blist)
        idx = random.randint(0, lenght - 1)
        tmp.append(blist[idx])
        blist.remove(blist[idx])

    return tmp


def output(alist):
    fout = codecs.open("output.txt", "w", 'utf-8')

    for line in alist:
        if (len(line.strip())) < 1:
#             fout.write("\r\n")
            pass
        else:
            fout.write(line)
            fout.write(u"，")
    fout.close()


step1 = my_split(article.decode('utf-8'), u'，')
step1 = list_split(step1, u',')
step1 = list_split(step1, u'。')
step1 = list_split(step1, u'；')
step1 = list_split(step1, u'?')
step1 = list_split(step1, u' ')

done = randomlize(step1)
output(done)

for line in done:
    print "--"
    print line
