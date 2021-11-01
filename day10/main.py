import pymysql


class Cup():
    # __height = 0.0
    # __valume = 0.0
    # __color = ''
    # __material = ''
    def __init__(self, height, valume, color, material):
        self.__height = height
        self.__valume = valume
        self.__color = color
        self.__material = material

    def use(self):
        print('杯子可以存放液体')

    def atter(self):
        print('这个{}的杯子主要是由{}做成的，有{}cm高，能存放{}ml的水'.format(self.__color, self.__material, self.__height, self.__valume))

    def modify(self, atter, para):
        if atter == 'height':
            self.__height = para


# glass1 = Cup(2.3,1,'白色','玻璃')
# glass1.atter()
# glass1.use()
# glass1.modify('height',2)
# glass1.atter()


class computer():
    __screensize = 0.0
    __price = 0.0
    __cpumodelnum = ''
    __memory = ''
    __sleeptime = 0.0

    def __init__(self, screensize, price, cpumodelnum, memory, sleeptime):
        __screensize = screensize
        __price = price
        __cpumodelnum = cpumodelnum
        __memory = memory
        __sleeptime = sleeptime

    def typy(self):
        input('开始打字：')

    def playgame(self):
        print('游戏加载中……')

    def video(self):
        print('网络环境差，加载失败')
