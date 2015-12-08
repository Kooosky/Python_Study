def func2_2(s,a):
    wds = s.split(" ")
    result = []
    for w in wds:
        if len(w) > int(a):
            result.append(w)
    return result