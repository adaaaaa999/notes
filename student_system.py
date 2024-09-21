#管理學生成績:1.新增2.刪除
#查詢學生成績:可以使用1.姓名2.全部
#將成績儲存到硬碟上 csv
#ps 資料格式有多種，例如:csv,json...
import os
grade = {} #存放全部資料
def student_system():
    try:
        load()
    except FileNotFoundError:
        print('第一次執行，所以沒有檔案可以載入')
    while True:
     os.system('cls')
     print('========================================')
     print('= 學生成績管理系統')
     #使用字典儲存學生的資料
     print('=')
     print('= 版本: 0.01')
     print('= 開發者: ADA')
     print('========================================')
     print('1.管理學生成績')
     print('2.查詢學生成績')
     print('3.離開系統')
     user_input = int(input('請輸入編號: '))
     if user_input == 1:
        management()
     elif user_input ==2:
        query()
     elif user_input ==3:
        print('系統已關閉')
        break
     else :
        input('輸入錯誤，輸入任意鍵重新選擇')
        continue

# 管理學生成績
def management():
    while True:
        print('-------------------')
        print('- 管理學生成績')
        print('-------------------')
        print('1. 新增學生成績')
        print('2. 刪除學生成績')
        print('3. 回主選單')
        user_input = input('=> ')

        if user_input == '1':
            add_grade()
        elif user_input == '2':
            del_grade()
        elif user_input == '3':
            break
        else:
            print('輸入錯誤，請重新輸入!')

# 查詢學生成績
def query():
    while True:
        print('-------------------')
        print('- 查詢學生成績')
        print('-------------------')
        print('1. 姓名查詢')
        print('2. 全部查詢')
        print('3. 回主選單')
        user_input = input('=> ')

        if user_input == '1':
            query_by_name()
        elif user_input == '2':
            query_all()
        elif user_input == '3':
            break
        else:
            print('輸入錯誤，請重新輸入!')
    
# 新增學生成績
def add_grade():
    name = input('請輸入姓名: ')
    no = input('請輸入學號: ')
    chinese = input('請輸入國文成績: ')
    english = input('請輸入英文成績: ')
    math = input('請輸入數學成績: ')

    # 新增到字典
    grade[name] = [no, chinese, english, math]

    # 寫入檔案
    save()

    # 測試用
    print(grade)
    
# 刪除成績
def del_grade():
    user_input = input('請輸入姓名: ')

    if user_input in grade:
        del grade[user_input]
        print('刪除完成')
    else:
        print('查無此人')

    save()

def query_by_name():
    user_input = input('請輸入姓名: ')

    if user_input in grade:
        print(f'姓名: {user_input}, 學號: {grade[user_input][0]}, 國文: {grade[user_input][1]}, 英文: {grade[user_input][2]}, 數學: {grade[user_input][3]}')
    else:
        print('查無此人')

def query_all():
    for i in grade:
        print(f'姓名: {i}, 學號: {grade[i][0]}, 國文: {grade[i][1]}, 英文: {grade[i][2]}, 數學: {grade[i][3]}')

def save():
    with open('student_system.csv', 'w', encoding='utf-8') as file:
        for i in grade:
            file.write(f'{i},{grade[i][0]},{grade[i][1]},{grade[i][2]},{grade[i][3]}\n')


def load():
    with open('student_system.csv', 'r', encoding='utf-8') as file:
        for i in file: # 從檔案一列一列讀進來
            i = i.split(',')
            grade[i[0]] = [i[1], i[2], i[3], i[4].strip()]

    print(grade)

student_system()

