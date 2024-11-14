def all_variants(text):

    s = 0
    e = 0
    ctn = 0
    while text[s: e] != text:
        if text[e] == text[len(text)-1]:
            s = 0
            ctn += 1
            e = ctn
            yield text[s: e]
        else:
            s += 1
            e += 1
            yield text[s: e]



a = all_variants("abc")
for i in a:
    print(i)