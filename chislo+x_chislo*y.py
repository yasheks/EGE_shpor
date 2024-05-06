def calk(begin, end):
    if begin > end:
        return 0
    if begin == end:
        return 1
    return calk(begin + 2, end) + calk(begin *5, end)
#задача где к число прибавляется 2 и где число умножается на 5
print(calk(2,50))
