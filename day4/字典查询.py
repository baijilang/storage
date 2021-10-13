'''list=[]通过角标来获取值
字典判断是根据键来判断
任务：#dict={地球：{中国：
		{北京：{昌平：{沙河：{起码路：北科院}}}}，
		美国：{
}
name=input”地球
if  name in  dict
	name1=input  #中国
	if name1 #中国# in dict[name#地球#]：
		print dict[地球][中国]
把键换成变量'''
dict={'地球':{'中国':
		{'北京':{'昌平':{'沙河':{'起码路':'北科院'}}}},
		'美国':'华盛顿'}
}
while True:
	plane=input("星球：")
	if plane in dict:
		country=input("输入国家：")
		if country in dict[plane]:
			capital=input("输入首都：")
			if capital in dict[plane][country]:
				city=input("输入城市：")
				if city in dict[plane][country][capital]:
					town=input("输入地区：")
					if town in dict[plane][country][capital][city]:
						street=input("输入街道：")
						if street in dict[plane][country][capital][city][town]:
							print(dict[plane][country][capital][city][town][street])
						elif street=="q":break
						else:print("错误")
					elif town == "q":break
					else:print("错误")
				elif city == "q":break
				else:print("错误")
			elif capital == "q":break
			else:print("错误")
		elif country == "q":break
		else:print("错误")
	elif plane == "q":break
	else:print("错误")