def all_variants(text):
    s = 0
    e = 1
    ctn = 1
    while text[s: e] != text:
        yield text[s: e]
        if e == len(text):
            s = 0
            ctn += 1
            e = ctn
        else:
            s += 1
            e += 1
    yield text

a = all_variants("abcde")
for i in a:
    print(i)