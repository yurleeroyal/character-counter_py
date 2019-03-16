from collections import Counter
import os


def charcount(lfile):
    f = open(lfile, "r")
    ccount = 0
    line = f.readline()
    while line != "":
        ccount = ccount + len(line)
        line = f.readline()
    f.close()
    print("Character count =", ccount)


def lcount(filename):
    g = open(filename, "r")
    linecount = 0
    line = g.readline()
    while line != "":
            linecount = linecount + 1
            line = g.readline()
    g.close()
    print("Line count =", linecount)


def wcount(filename):
    h = open(filename, "r")
    wordcount = 0
    line = h.readline()
    while line != "":
            linelist = line.split()
            for x in linelist:
                wordcount = wordcount + 1
            line = h.readline()
    h.close()
    print("Word count =", wordcount)


def freqcount(i,anyword):
    mylist = []
    i = open(i,"r")
    linelist = i.read().lower().split()
    for eachw in linelist:
            symbols = "!@#$%^&*()_+{}|[]\;'"":<>?,./"
            for b in range(0, len(symbols)):
               eachw = eachw.replace(symbols[b], "")
            if len(eachw) > 0:
                mylist.append(eachw)
            counts = Counter(mylist)
    i.close
    mylist.append(eachw)
    specifics = counts[anyword]
    print("The word", anyword, "occurs", specifics, "times.")


charcount("filename")
lcount("filename")
wcount("filename")
freqcount("filename","word")
