name = "lzl"

def f1():
    name = "Eric"
    def f2():
        name = "snor"
        print(name)
    f2()
f1()  

def f1():
    print(name)
def f2():
    name = "eric"  #学过函数，肯定知道最后f1()执行完会输出Snor；我们先记住一个概念，Python中有作用域链，变量会由内到外找，先去自己作用域去找，自己没有再去上级去找，直到找不到报错
    f1()
f2()

li = [lambda: x for x in range(10)]
res = li[0] ()
print(res)

def func ():
    a = 1 
    def foo():
        nonlocal a
        a = 12
        print(a) ## 没有这句就是 一个12 一个1  有这句就是2个 12 nonlocal是把局部变成上层的作用域 作用整个函数
    foo()       
    print(a)
func()
#global 局部变量 外层的作用于变量 当前模块的全局变量 内置变量

s=0
def glo():
    global s
    s+=1
    print(s)
glo()


#self 表达的意思是 类里面不确定的某一个对象 

class student:
    def study(self):
        print()
    def coding(self):
        print()
    def ask(self):
        print()

yoyo=student() #这句话就是对yoyo这个学生进行实例化之后 就是方法的调用
yoyo.ask()
yoyo.coding()
yoyo.study()

class province:
    country ="zhongguo"
    def __init__(self,name)
        self.name = name
shanghai=province("shanghai")
print(shanghai.name)
print(province.country)  #直接访问普通字段实力化名字之后.参数 直接访问静态字段类名.参数



