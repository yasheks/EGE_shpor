def f(s,n): #s - камни, n - кол-во ходов
    if 20<=s<=30: return n%2==0 #если нет ограничений по возврастанию, то не пишем 3 строку 
    if s > 30: return n%2 != 0
    if n == 0: return False
    h = [f(s+1, n-1), f(s*2, n-1)] #пишем все действия с камнями
    if (n-1)%2 == 0:
        return any(h)
    else: return all(h) #в тетради в таблице чекнуть, когда any или all

print("N19", [s for s in range(1,19) if f(s,2)])
print("N20", [s for s in range(1,19) if f(s,3) and not (f(s, 1))])
print("N21", [s for s in range(1,19) if f(s,4) and not (f(s, 2))]) #вывод
