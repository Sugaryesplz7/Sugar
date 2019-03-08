'''a = 1
b = 2
def func(c,d):
    e = 111
    print("L={0}".format(locals()))
    print("G={0}".format(globals()))

func(10,20)
'''
'''
x = 100
y = 200
z1 = eval("x+y")
z2 = exec("x+y")
print(z1)
print(z2)
help(exec)
exec.__doc__
exec(print("x+y"))
'''
'''
x = 0
def func():
    global x
    x +=1
    print(x)
    func()
func()
'''
'''
def fino(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fino(n-1) + fino(n-2)

print(fino(10))
'''
a = [1,2,3,4]
b = 2
c = a * b
print(c)
print(id(a))
print(id(b))
print(id(c))
a = ["a","b","c"]
b = [i*10 for i in a]
print(b)
print(len(a))
print(max(a))
