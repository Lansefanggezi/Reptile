def add_end(l=[]):
	l.append('end')
	return l
list= add_end(['liu','xiao','kang'])
print(list)
def cacl(numbers):
	sum = 0
	while numbers >0:
		sum = sum + numbers * numbers
		numbers = numbers -1
	return sum
print(cacl(4))
def cacl1(numbers):
	sum = 0
	for x in numbers:
		sum = sum + x * x
	return sum
print(cacl1([1,2,3,4]))

def cacl2(*numbers):
	sum = 0
	for x in numbers:
		sum = sum + x * x
	return sum
print(cacl2(1,2,3,4))
num = [1,2,3,4]
numT = (1,2,3,4)
print(cacl1(num))
print(cacl2(*num))
print(cacl2(*numT))
def persons(name,age,**kw):
	print('name:',name,'age:',age,'orther',kw)
persons('liuxiaokang',18,xingbie='nan')
extra = {'city':'tianjin','sex':'man'}
persons('Carl',23,city = extra['city'],sex = extra['sex'])
persons('Carl',23,**extra)