from BankTool import Bank

bank = Bank('工商银行')

while True:
    bank.homepage()
    index = input('请输入指令:')
    if index == '1':
        bank.add()
        continue

    elif index == '2':
        bank.save_money()
        continue

    elif index == '3':
        bank.get_money()
        continue

    elif index == '4':
        bank.trans_money()
        continue

    elif index == '5':
        bank.search_info()
        continue

    elif index == '6':
        break

    else:
        print('未识别的指令')
        continue
