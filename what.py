def twostring(a, b):
    what = []
    watch = []
    for i in a: 
        if i in b:
            what.append(i)
    for i in range(len(a)): 
        if a[i] in b:
            watch.append(i)
    print(what)
    print(watch)

twostring('watch','what')
