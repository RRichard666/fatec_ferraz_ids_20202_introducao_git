print('Soma ou Subtraçcao')
op = int(input('1 soma 2 subtracao' ))
x = int(input('Digite um valor: '))
y = int(input('Digite outro valor: '))
res = 0
if op == 1:
	res = x + y
else:
	res = x - y
print(res)
