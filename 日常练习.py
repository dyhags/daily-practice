#吃饭练习
#向大家问好
吃饭的人名字=["1","2","3"]
for 吃饭的人 in 吃饭的人名字:
    print("吃饭的人")
print("欢迎！")
#吃饭练习中附加的小游戏
#吃饭前的小游戏
a=["欢迎来到python猜数游戏","资源正在加载中......","一个数，小于100","错误，太大了","错误，还是太大了","正确"]
print("先来玩个小游戏")
print(a[0])
print(a[1])
print(a[2])
#input()
print(a[3])
#input()
#print(a[4])
#input()
#print(a[5])
#披萨练习
yourpizzas=["a","b","c","d","e"]
mypizzas=["f","g","h","y","j"]
myfriend=yourpizzas[:]
print(yourpizzas)
print(myfriend)
print(mypizzas)
#披萨练习的for循环练习
for a in yourpizzas:
    print(a + "i like to")
for b in mypizzas:
    print(b + "ow,i like some")
for c in myfriend:
    print(c + "emmm,i like some to")
    #自助餐的元表和for循环练习
自助餐元表=("ab","cd","ef","gh","ij")
for food in 自助餐元表:
    print(food+"i very like!")
#python拒绝了我对元表的修改
#pop元表 = 自助餐元表.pop()
#给元组变量赋值并检验
a=('a','b','c','d','e')
print(a)
for b in a:
    print(a)
b=('a','b','c','d','e','f','g')
print(b)
for a in b:
    print(a)
#if语句练习
cars=("a","b","c","d","e")
for car in cars:
    if car =="a":
        print(car)
    else:
        print(car.title())
agspeople=("dyh","lmy")
if agspeople[0]!="dyh":
    print("不相等")
else:
    print("相等")
a=("a","b") 
b=("a","b")
if b!=a:
    print("不相等")
else:
    print("相等")
#条件测试
a="asdfghjkl"
print(a=="asdfghjkl")
print("ithink is true")
b="qwertyuiop"
print(b=="asdfghjkl")
print("i think is false")
c="zxcvbnm"
print(c!="asdfghjkl")
print("i think is true")
d="qwertyuiopasdfghjkl"
print(d!="qwertyuiopasdfghjkl")
print("i think is false")