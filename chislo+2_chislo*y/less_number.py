def calk(begin, end):
    if begin == 15:
        return 0
    #это используется когда число не нужно считать
    if begin > end:
        return 0
    if begin == end:
        return 1
    return calk(begin + 1, end) + calk(begin +3, end)
#плюс 1 и плюс 3
