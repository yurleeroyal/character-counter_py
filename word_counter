def word_count(filename):
    h = open(filename,"r")
    wordcount = 0
    line = h.readline()
    while line != "":
            linelist = line.split()
            for x in linelist:
                wordcount = wordcount + 1
            line = h.readline()
    h.close()
    print ("Word count =", wordcount)
