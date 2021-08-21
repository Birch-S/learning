# 碧蓝航线


class Shipess:
    def __init__(self, name):
        self.name = name
        self.__intimacy = 50

    def inti(self):
        print('{}跟你的好感度是{}.'.format(self.name, self.__intimacy))

    def kiss(self):
        self.__intimacy = self.__intimacy + 1
        print('你亲了{}.'.format(self.name))

    def say(self):
        print('{}说困了.'.format(self.name))
        return


laffey = Shipess('拉菲')
laffey.inti()



