import os #載入operating system

#讀取檔案
def read_file(filename):
    items = []
    if os.path.isfile(filename): #檢查檔案在不在
        print('yeah I found it!')
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                if 'Product name,Price' in line:
                    continue  #continue/break都必須在迴圈裡意指跳出或跳過
                name, price = line.strip().split(',')
                items.append([name, price])
        print(items)
    else:
        print('oops ! the file is missing.')
    return items

#讓使用者輸入
def user_input(items):
    while True:
        name = input('請輸入商品名稱: ')
        if name == 'q':
            break
        price = input('請輸入商品價格: ')
        price = int(price)
        items.append([name, price])
    print(items)
    return items

#印出所有購買紀錄
def print_products(items):
    for p in items:
        print(p[0], '的價格是', p[1])

#寫入檔案
def write_file(filename, items):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('Product name,Price\n')
        for p in items:
            f.write(p[0] + ',' + str(p[1]) + '\n')


items = read_file('items.csv')   #items.csv是這次尋找的檔名,即是def設定參數時的變數,下次找其他檔名亦不須進到程式碼一個一個修改
items = user_input(items)        #有return時才需要 回傳 items = user_input(items)
print_products(items)            #因此為印出項目,故不需要回傳
write_file('items.csv', items)   #因為此為寫入檔案,故不需要回傳