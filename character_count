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

    print("ccount =",ccount)
