# -*- coding: utf-8 -*-
# coding=UTF-8
import random
import codecs


class article_rnd:
    infile = ""
    outfile = ""

    def __init__(self, infile_name, outfile_name):
        self.infile = infile_name
        self.outfile = outfile_name
        fin = open(infile_name, 'r')
        self.article = fin.read()

    def my_split(self, str, c):
        tmp = str.split(c)
        return tmp

    def list_split(self, alist, c):
        tmp = []
        for line in alist:
            tmp.extend(self.my_split(line, c))
        return tmp

    def randomlize(self, alist):
        tmp = []
        blist = alist
        while len(blist) > 0:
            lenght = len(blist)
            idx = random.randint(0, lenght - 1)
            tmp.append(blist[idx])
            blist.remove(blist[idx])

        return tmp

    def output(self, alist):
        fout = codecs.open(self.outfile, "w", 'utf-8')
        newSection = True
        for aline in alist:
            line = aline.strip()
            if (len(line)) < 3:
                if newSection != True:
                    fout.write(u"。\r\n")
                else:
                    fout.write(u"\r\n")
                newSection = True
            else:
                if newSection != True:
                    fout.write(u"，")
                fout.write(line)
                newSection = False
        fout.close()

    def process(self):
        step1 = self.my_split(self.article.decode('utf-8'), u'，')
        step1 = self.list_split(step1, u"\n")
        step1 = self.list_split(step1, u',')
        step1 = self.list_split(step1, u'。')
        step1 = self.list_split(step1, u'；')
        step1 = self.list_split(step1, u'?')
        step1 = self.list_split(step1, u' ')

        done = self.randomlize(step1)
        self.output(done)


a = article_rnd("input.txt", "output.txt")
a.process()

