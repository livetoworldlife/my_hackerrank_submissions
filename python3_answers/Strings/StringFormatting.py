def print_formatted(number):
    wid = len("{0:b}".format(number))
    for i in range(1,number + 1):
        print("{:{width}d} {:{width}o} {:{width}X} {:{width}b}".format(i, i, i, i,width=wid))
