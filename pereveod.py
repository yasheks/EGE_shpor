def f7(n):
    st = ""
    while n > 0:
        zef = n%7
        n //=7
        st = str(zef) + st
    return st

#перевод в 7 систему счисления
