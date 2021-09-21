def filt(in_num):
    if (in_num>50) and (in_num % 2==1) :
        return True
    else:
        return False


numbers = [0, 99, 100, 53, 44, 23, 4, 8, 16, 15, 77, 51]
print(list(filter(filt, numbers)))

