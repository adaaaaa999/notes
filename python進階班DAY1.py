#===========================================================================================
#yield
#===========================================================================================

#yield 迭代 (一筆一筆取資料)，為for in迴圈的原理
#有yield之後，foo()就不會是函式，而是一個產生器
#可以用來節省記憶體，如果有很大數據，就不會一次全給
def foo():#產生器會呼叫裡面要做的事情，輸入next(y)會呼叫產生器
    print('start')
    t = yield 1 #遇到yield相當於暫停，需要再輸入一次next(y)再呼叫一次產生器才會繼續進行
    print(f'contine: {t}')
    t1 = yield 2
    print(f'contine 2: {t1}')

y = foo()#為產生器，呼叫foo時會回傳值給y
print(y)#打這個不會有裡面的東西，只會回傳產生器foo()，而不會執行裡面的東西

print('開始執行產生器')
a = next(y)#有這個產生器才會執行，但中間遇到yield就會暫停，就會需要再打next(y)去呼叫產生器
print(a)#上面執行後，會回傳1這個值到a，那我們需要print出來他才會顯示
b=y.send('yes')#可以使用send觸發繼續執行，遇到yield依然會暫停，差別是會把send後面的值回傳
print(b)
next(y)

#========================================================================
#取得不定長度數字
data = []
def give_me_number():
    while True:
        user = input('number(離開=quit)=> ')
        if user=='quit':
            break
        else:
            yield int(user)
for i in give_me_number():
    data.append(i)

print(sum(data))

#========================================================================
#抓隨機數字出來加總
import random
def get_3_random_number():
    index=0
    while index<3:
     yield random.randint(0,10)
     index +=1

data = []#建立一個空清單
for i in get_3_random_number():#i會抓每次yield裡面的值
   data.append(i)#把每一次i抓到的值存入data

print(data,sum(data))#前面顯示data清單，後面顯示data清單的總和

#data = list(get_3_random_number())  #list會自動把裡面資料一筆筆抓出來
#print(data,sum(data))

#===========================================================================================
#oop物件導向
#===========================================================================================
#定義輪廓 class類別，一個class可以有很多個object物件
#這個函式專屬於某種物體，則稱為"方法"，變數專屬於某種物體，稱為"屬性"
class Car:
    def __init__(self):#有__開頭不用主動呼叫，他會在建立物件的時候主動被呼叫
        self.color = '無色'
        print('我是__init__')

    def __str__(self):
        return f'我是車子{self.color}車子'#會當成字串來使用，在有需要當字串使用時會自動呼叫
    
    def show(self):#把self當作沒有，但是一定得打，如果要傳參數可以逗號再加
        print(f'我是車子{self.color}')

a = Car() #建立物件
a.color = '紅色' #建立物件屬性，透過self抓得到，要注意屬性要建立在呼叫之前
a.show()#呼叫car物件的方法show
#不同變數建立的物件彼此是獨立的
b = Car()
b.color = '黑色'
print(a)

#=============================================================================
#oop的其中一個特性 : 覆載(繼承)
class Car:
    def __init__(self):
        self.color = '銀色'
        self.gas = 0

    def run(self):
        print('開車')

    def set_color(self, color):
        self.color = color

    def show(self):
        print(f'我是{self.color}的車子')

class Truck(Car):  # Truck類別繼承自Car類別
    # def __init__(self):
    #     self.color = '銀色'
    #     self.gas = 0

    # def run(self):
    #     print('開車')

    # def set_color(self, color):
    #     self.color = color

    # 覆載覆類別的show方法
    def show(self):
        super().show()#使用後可以顯示原本被覆蓋的父類別
        print(f'我是{self.color}卡車')

    def drop():
        print('卸貨')


class SportCar(Car):
    # def __init__(self):
    #     self.color = '銀色'
    #     self.gas = 0

    # def run(self):
    #     print('開車')

    # def set_color(self, color):
    #     self.color = color

    def show(self):
        super().show()
        print(f'我是{self.color}跑車')

    def turbo(self):
        print('進入加速模式')

    
truck = Truck()
truck.set_color('藍色')
truck.run()
truck.show()

sport_car = SportCar()
sport_car.set_color('紅色')
sport_car.run()
sport_car.show()

#========================================================================
#oop其中一個特性 : 多形
class Triangle:
    def __init__(self, level):
        self.__level = level

    def show(self):
        for i in range(self.__level):
            for j in range(i + 1):
                print('*', end='')
            print()

class RTriangle:
    def __init__(self, level):
        self.__level = level

    def show(self):
        for i in range(0, -self.__level, -1):
            for j in range(self.__level + i):
                print('*', end='')
            print()


class Rectangle:
    def __init__(self, level):
        self.__level = level
    
    def show(self):
        for i in range(self.__level):
            for j in range(self.__level):
                print('*', end='')
            print()


class Line:
    def __init__(self, level):
        self.__level = level

    def show(self):
        for i in range(self.__level):
            print('**')

# r = Triangle(5)
# r.show()
# r2 = Rectangle(5)
# r2.show()
# r1 = RTriangle(5)
# r1.show()
# line = Line(3)
# line.show()

graph = []
graph.append(Triangle(5))
graph.append(Rectangle(5))
graph.append(RTriangle(5))
graph.append(Line(3))
             
for i in graph:
    i.show()

#===========================================================================================
#aop物件導向
#===========================================================================================
#oop由上而下擴充功能，aop橫向擴充功能
def c(func):
    def b(name):
     print('start')
     func()
     print('end')
    
@c #裝飾器，裝飾後，原本裡面得函式會取代base(name)
def base(name):
    print('我是小小程式',name)

print(base)


#===========================================================================================
#json資料格式
#===========================================================================================
#API應用程式介面
#JSON 字串格式
import json
a = '[1,2,3,4]'#json string
print(a,type(a))
a = json.loads(a) #json=>python
print(a,type(a),a[0])
a.append('hello')
a=json.dumps(a)#python=>json
print(a,type(a))