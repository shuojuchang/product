#寫入檔案
products = []
while True:
    name = input('請輸入產品名稱: ')
    if name == 'q':
        break
    price = input('請輸入價格: ')
    price = int(price)
    p = []
    p.append(name)
    p.append(price)
    products.append(p)

with open('products.csv', 'w') as f:
    f.write('Item no.,unit price \n')
    for p in products:
        f.write(p[0] + ',' + str(p[1]) + '\n')

