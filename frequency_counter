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
