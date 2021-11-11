# 打开文件

with open('baidu_x_system.log', 'r+', encoding='utf-8') as f:
    count_dict = {}
    for line in f.readlines():
        line_cut = line.split(' ')
        if line_cut[0] in count_dict:
            count_dict[line_cut[0]] += 1
        else:
            count_dict[line_cut[0]] = 1

with open('login_count_info.txt', 'w', encoding='utf-8') as f1:
    f1.write('登录信息统计\n')
    f1.write('ip'.center(16, ' ') + ' ' * 4 + 'count'.center(6, ' ') + '\n')
    for key, value in count_dict.items():
        f1.write(str(key).center(16, ' ') + ' ' * 4 + str(value).center(6, ' ') + '\n')
print('success!')

with open('login_count_info.txt', 'r', encoding='utf-8') as f3:
    print(f3.read())
