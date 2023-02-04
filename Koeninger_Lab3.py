#Max Koeninger
#This program is complete

PKG_PRICE = 149

pkg_num = int(input('Enter the number of packages purchased: '))
fin_price = pkg_num * PKG_PRICE

if(pkg_num <= 0):
    print('Invalid number of packages!')
elif(pkg_num < 10):
    discount = 0
    print('Discount amount = $0')
    print(f'total after discount = ${fin_price}')
elif(pkg_num >= 10 and pkg_num <50):
    discount = fin_price * 0.1
    fin_price -= discount
    print(f'Discount amount = ${discount:,.2f}')
    print(f'total after discount = ${fin_price:,.2f}')
elif(pkg_num >= 50 and pkg_num <100):
    discount = fin_price * 0.2
    fin_price -= discount
    print(f'Discount amount = ${discount:,.2f}')
    print(f'total after discount = ${fin_price:,.2f}')
elif(pkg_num >= 100 and pkg_num <150):
    discount = fin_price * 0.3
    fin_price -= discount
    print(f'Discount amount = ${discount:,.2f}')
    print(f'total after discount = ${fin_price:,.2f}')
else:
    discount = fin_price * 0.4
    fin_price -= discount
    print(f'Discount amount = ${discount:,.2f}')
    print(f'total after discount = ${fin_price:,.2f}')
