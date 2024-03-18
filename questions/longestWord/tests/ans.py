def longestWord(xx):
    l = xx[0]

    for w in xx[1:]:
        if len(w) > len(l):
            l = w
            
    return l
