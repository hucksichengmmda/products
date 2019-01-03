products = []
while True:
	name = input('请输入你的商品名：')
	if name == 'q':
		break
	price = input('请输入商品价格：')
	products.append([name, price])
print(products)