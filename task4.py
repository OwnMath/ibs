def dicy(dt):
    newdic = {}
    for d in dt:
        if dt[d] >= 3:
            newdic[d] = dt[d]
    return newdic


dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4, 'five': 5}
print(dicy(dict))
