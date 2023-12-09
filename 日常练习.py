#我并没有做得很好，但，我仍然在成长中.(2023.12.9)
#这是我之前写的，现在继续更（2023.12.9）
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
#来复习一下, :( [马上要考试，啊啊啊啊啊啊啊啊啊] 悲{2023.12.9}
#if的结构练习[1]
age=12
if age > 18:
    print("you can play games")
elif age < 18:
    print("you can't play games")
#if的结构练习[2]
age=18
if age < 18:
    print("you can't play games")
elif age > 18:
    print("you can play games")
else:
    print("you can play games,too")
#if的结构练习[3]    
beautiful=["a","b","c"]
if "a" in beautiful:
    print("hello,a!")
if "b" in beautiful:
    print("hello,b!")
if "c" in beautiful:
    print("hello,c!")
print("hello everyone!")
#年龄练习
newage=12
if newage < 2:
    print("他是婴儿")
elif newage < 4:
    print("他正蹒跚学步")
elif newage < 13:
    print("他是儿童")
elif newage < 20:
    print("他是青少年")
elif newage < 65:
    print("他是成年人")
elif newage > 65:
    print("他是老年人")
#管理员问候 
yonghu=["a","b","c","admin"]
for yonghubiao in yonghu:
    print("hello!")
    if yonghubiao =="admin":
        print("hello,admin!")
#字典{终于开始力}
colour={"a":"green","b":"yellow","c":"red"}
print(colour)
print(colour["a"])
