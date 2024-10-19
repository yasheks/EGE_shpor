def from10_ToAny(n, q): # n - число, q - система счисления
    ans = ''
    alp = "0123456789abcdefghikjklmnopqrstuvwxyz"
    while n:
        ans = alp[n%q] + ans
        n //= q
    return ans
print(from10_ToAny(4, 2))
