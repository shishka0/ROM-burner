def parse(f):
    data = []
    for line in f:
        addr, word = line.rstrip().split(' ')
        addr = int(addr, base=16)
        word = int(word, base=16)
        data.append((addr, word))
    return data
