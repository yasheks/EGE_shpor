def calk(begin, end):
    if begin > end:
        return 0
    if begin == end:
        return 1
    return calk(begin + 1, end) + calk(begin *2, end) + calk(begin *3, end)
#задача где к число прибавляется 1, где число умножается на 2 и умножается на 3
print(calk(2,15) * calk(15,30))
#если есть траектория вычесления(здесь это число 15) то мы идем до нужного числа и перемножаем
