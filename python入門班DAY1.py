#上課內容包含:
#print
#input、int
#if else判斷 、for in迴圈、break迴圈中止、continue忽略下面從頭開始、range搭配迴圈執行幾次
#list 使用說明
#import、pip3 導入模組以及安裝

#============================================================================================        
#TYPE=========================================================================================
#============================================================================================
#使用type判別資料型態
print (type(3.3)) #float浮點數
print (type('嗨')) #str字串
print (type(3)) #int整數
#true和false屬於bool(布林)型態
print (type(True))
print (type(False))

#============================================================================================        
#INPUT=========================================================================================
#============================================================================================
print('變換')
print(3 + 3)
print(3.4)
print('3' + '3')
my_data = input() # 讓使用者從鍵盤輸入資料
print(type(3))
print(type('3'))
print(type(3.4))
print(my_data)

# 讓使用者輸入兩個數字
a1 = input('請輸入第一個數字: ')
a2 = input('請輸入第二個數字: ')
# 資料轉型(把字串傳型成數字)
a1 = int(a1)
a2 = int(a2)
# 輸出
print(a1, '和', a2, '的總和為:', a1 + a2)

#============================================================================================        
#IF判斷=========================================================================================
#============================================================================================
score = input('請輸入成績: ')
score = int(score)
if score >= 60:
    print('及格')
if score < 60:
    print('不及格')

#============================================================================================        
#IN=========================================================================================
#============================================================================================
#使用多行字串需使用三個單引號框起來
data = '''今（17）日台灣還是處於低壓帶，水氣偏多，各地雲量也有明顯偏多情形，氣象署預報員陳姵安表示，尤其風場以西南風為主，在中南部地區會帶來局部較大雨勢，預計低壓帶影響到下週二，下週三起雨勢才會有明顯趨緩情形。此外，由於19日至23日適逢年度大潮，西部沿海、新北至嘉義一帶可能有海水倒灌，要留意局部大雨可能造成積淹水情況。'''
user = input ('請輸入關鍵字 : ')
if user in data :#取內容物
    print (user,'有出現在新聞內')
else :
 print (user,'沒有出現在新聞內')

#============================================================================================        
#LIST=========================================================================================
#============================================================================================
a = [2, 4, 6] # list資料型態，並將list存放到a變數裡
a[0] = 9  # 將第一筆資料修改成9
print(a[0])  # 取得list內的第一筆資料
print(a[1])  # 取得list內的第2筆資料
print(a[2])  # 取得list內的第3筆資料
a.append(88)  # 將88新增到a變數裡面的list(從最後面新增)
a.insert(0, 77) # 從第一筆資料的地方插入77
a.remove(4) # 將4這筆資料從list裡面刪除
print(a)
a.insert(4, 777) # 從list最後面插入777
print(a)
del a[2]  # 2是list索引值，代表第三筆資料，del為刪除
print(a)

#============================================================================================        
#FOR IN迴圈=========================================================================================
#============================================================================================
a = [1, 2, 3, 4]
for temp in a:#a的資料會一筆筆被temp讀取
    print(temp)

#幫每一筆資料+10
a = [33, 32, 33, 34, 45, 56, 63, 21]
for temp in a:
    print('加分後:', temp + 10)

#不及格才+10
a = [35, 63, 25, 47, 93]
final = [] # 建立空的list
for temp in a:
    if temp < 60:#如果小於60，執行if內程式並把數值加入list內，如果大於60則執行else內程式，再把數值加入list
        print('最終成績:', temp + 10)
        final.append(temp + 10)
    else:
        print('最終成績:', temp)
        final.append(temp)
print(final)#列出加入所有數值的list

#============================================================================================        
#Ubike即時查詢(csv)=========================================================================================
#============================================================================================
import csv #導入csv模組
import requests #透過pip3(pip 3.0)進行安裝，用於網路上抓資料
#網址是字串，需要加單引號
response = requests.get('https://data.tycg.gov.tw/api/v1/rest/datastore/a1b4714b-3b75-4ff8-a8f2-cc377e4eaa0f?format=csv&limit=999')
#用.運算子可以直接使用裡面的程式碼(透過.叫出的函式，只屬於.前面的)，稱作"方法"。 沒有.的函式，ex:print，叫做"函式"
#括號內=給予這個函式的參數，有多個參數要使用逗號區分開
#利用response收集這個網址回傳的資料，裡面是複合型資料
#寫上limit=999，才會回傳999筆資料(如網站資料大於999，則可將數字再調大)，否則他只會回傳一定的數量(可能不會全部的資料)
with open('ubike_v2.csv','w',encoding='utf-8') as file:#存到變數file裡面
    #open必須給的參數:1.檔名 2.模式(read(r)、write(w)... 3.encoding，順序不可以換
    file.write(response.text)
#寫text，response裡面的資料才會以text顯現
#w是寫入檔案，r是讀取檔案
#寫入編碼格式(在電腦看到、儲存的資料格式)utf-8(國際編碼)
#在程式中，每個字都有屬於它的編碼，假設沒有解碼，只會看到他的編碼，不會看到字
#這份檔案會寫入ubike_v2.csv(這份檔案不存在沒關係，因為是寫入，如果是讀取則需要是存在的)
#寫入之後，檔案會跑到左手邊的欄位
with open ('ubike_v2.csv','r',encoding='utf-8')as file:#存到變數file裡面
    result = csv.reader(file)
    #把file(大筆字串)根據"逗號位置"切割成一筆筆資料，存入result這個特殊櫃裡面
    #如果沒有這一行程式，在搜尋'中央大學'時，無法從大筆字串單獨找到中央大學，只能自己下去一個個找
    result = list(result)
    #把result做成list
    user = input('請輸入要搜尋的站台: ')
    for row in result: #row會隨著result的每一筆資料變動
        if user in row[3]: #找輸入的名稱，模糊搜尋
         print ('站名',row[3],'地址',row[6])
         print('  - 目前可借:', row[12])
         print('  - 目前空位:', row[5])
         print()