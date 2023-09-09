#讀取檔案
items = []
with open('items.csv', 'r', encoding='utf-8') as f:
    for line in f:
        if 'Product name,Price' in line:
            continue  #continue/break都必須在迴圈裡意指跳出或跳過
        name, price = line.strip().split(',')
        items.append([name, price])
print(items)

#讓使用者輸入
while True:
    name = input('請輸入商品名稱: ')
    if name == 'q':
        break
    price = input('請輸入商品價格: ')
    price = int(price)
    items.append([name, price])
print(items)

#印出所有購買紀錄
for p in items:
    print(p[0], '的價格是', p[1])

#寫入檔案
with open('items.csv', 'w', encoding='utf-8') as f:
    f.write('Product name,Price\n')
    for p in items:
        f.write(p[0] + ',' + str(p[1]) + '\n')