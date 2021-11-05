# 路飞学成直训营17期_task1
# W：白激浪

file = open(r'待分拣地址.txt','r+',encoding='utf8')
info = eval(file.read())
file.close()

def title(x):
	province = []  # 创建列表接收地址中的省或市名
	for i in x:
		m = i[1]
		if (m[2] == '省' or m[2] == '市') and m[0:3] not in province:
			province.append(m[0:3])
		elif (m[3] == '省' or m[3] == '市') and m[0:4] not in province:
			province.append(m[0:4])
		else:
			pass
	return province


def select(x):
	combination = {}
	province = title(x)
	for i in province:
		part = []
		for m in x:
			if m[1][0:3] == i or m[1][0:4] == i:
				part.append(m)
				x.remove(m)
		combination[i] = part
	return combination


a = select(info)
B = open(r'test1.txt','w+')
B.write('东风快递地址分拣')
B.close()
for key,value in a.items():
	B = open(r'test1.txt', 'a+')
	param = '\n' + key + ':'
	B.write(param)
	B.close()
	for i in value:
		B = open(r'test1.txt', 'a+')
		param = str(i) + ',\n'
		B.write(param)
		B.close()

print('success!')
