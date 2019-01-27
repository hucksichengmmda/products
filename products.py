import os  #operating system
products = []

if os.path.isfile('products.csv'):
	print('yeah,find it!')
	with open('products.csv', 'r', encoding = 'utf-8') as f:
		for line in f:
			if '商品, 价格' in line:
				continue #跳到下一回
			name, price = line.strip().split(',')
			products.append([name, price])
	print(products)
else:
	print('no!,I cannot find the products!')


while True:
	name = input('请输入你的商品名：')
	if name == 'q':
		break
	price = input('请输入商品价格：')
	products.append([name, price])
print(products)
for product in products:
	print(product)

with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('商品, 价格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')
