def func2_3(s,sw):
    wds = s.split(" ")
    result = []
    for w in wds:
        if w not in sw:
            result.append(w)
    return result