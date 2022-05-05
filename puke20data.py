"""
版本号puke2022.05.3.14:15
1.将获胜者数据大量保存为excel文件
"""
import copy
import sys
import random, pygame, time
from collections import Counter
from pygame.locals import *
import pandas as pd
import math
from datarecord import write_Data_Record


Version = 'puke2022.05.3.14:15'
玩家数 = 9
data = 1
Puke_List = []
puke花色 = []
puke大小 = []
player1数字 = []
玩家2数字 = []
玩家3数字 = []
玩家4数字 = []
玩家5数字 = []
玩家6数字 = []
玩家7数字 = []
玩家8数字 = []
玩家9数字 = []
player1花色 = []
玩家2花色 = []
玩家3花色 = []
玩家4花色 = []
玩家5花色 = []
玩家6花色 = []
玩家7花色 = []
玩家8花色 = []
玩家9花色 = []
Puke_List1 = []
Puke_List2 = []
Puke_List1花色 = []
Puke_List2花色 = []
final_winner = []

# 主窗口
class MainGame():
    window = None
    Screen_Heigh = 700#屏幕高度
    Screen_Width = 1400#屏幕宽度
    Game_Launcher = 0 #游戏进程

    Color_Black = pygame.Color(100, 100, 100)#背景颜色

    def __init__(self):
        pass

    def startGame(self):
        pygame.display.init()
        MainGame.window = pygame.display.set_mode([MainGame.Screen_Width, MainGame.Screen_Heigh])  # 创建窗口加载窗口
        pygame.display.set_caption("%s" % Version)#版本号标题显示
        # 给扑克牌坐标
        self.ShowMyPuke()
        self.ShowE_Puke()
        self.ShowUrealPuke()
        pygame.font.init()#初始化字体模块
        # print(pygame.font.get_default_font())#输出默认字体
        # print(pygame.font.get_fonts())#获取所有可用字体
        # MainGame.window.blit(MainGame.显示文字("fuckyou"),(1400/2,700/2))
        while True:
            # 将窗口填充颜色
            MainGame.window.fill(MainGame.Color_Black)
            # 获取事件
            self.GetEvent()
            #显示开始游戏画面
            if MainGame.Game_Launcher == 0:
                # 清空数据库
                MainGame.数据清零()
                MainGame.window.blit(MainGame.开始游戏("开始游戏"), (1400 / 5, 700 / 3))
            #开始游戏
            if 0<MainGame.Game_Launcher <= 7:
                # 展示扑克牌
                self.展示扑克()
            if MainGame.Game_Launcher == 8:
                MainGame.window.blit(MainGame.游戏结束("游戏结束"), (1400 / 2.6, 700 / 5))
                self.展示扑克()
                #展示获胜者牌组
                for i in range(len(final_winner)):
                    MainGame.window.blit(MainGame.获胜者展示("获胜者为：玩家{0}".format(final_winner[i][0])),(1400 / 5, 700 / 1.5-80+30*i))
            if MainGame.Game_Launcher == 9:
                #流程清零
                MainGame.Game_Launcher = 0
            # 更新显示
            pygame.display.update()
            time.sleep(0.05)

    def 数据清零():
        global Puke_List, puke花色, puke大小, player1数字, 玩家2数字, 玩家3数字, 玩家4数字, 玩家5数字, 玩家6数字, 玩家7数字, 玩家8数字, 玩家9数字, player1花色, 玩家2花色, 玩家3花色, 玩家4花色, 玩家5花色, 玩家6花色, 玩家7花色, 玩家8花色, 玩家9花色
        global Puke_List1, Puke_List2, Puke_List1花色, Puke_List2花色
        Puke_List = []
        puke花色 = []
        puke大小 = []
        player1数字 = []
        玩家2数字 = []
        玩家3数字 = []
        玩家4数字 = []
        玩家5数字 = []
        玩家6数字 = []
        玩家7数字 = []
        玩家8数字 = []
        玩家9数字 = []
        player1花色 = []
        玩家2花色 = []
        玩家3花色 = []
        玩家4花色 = []
        玩家5花色 = []
        玩家6花色 = []
        玩家7花色 = []
        玩家8花色 = []
        玩家9花色 = []
        Puke_List1 = []
        Puke_List2 = []
        Puke_List1花色 = []
        Puke_List2花色 = []
        final_winner = []

    def 展示扑克(self):
        MainGame.My_Puke1_1.Display_Puke()
        MainGame.My_Puke1_2.Display_Puke()
        MainGame.En_Puke1_2.Display_Puke()
        MainGame.En_Puke1_1.Display_Puke()
        MainGame.Ur_Puke1.Display_Puke()
        MainGame.Ur_Puke2.Display_Puke()
        MainGame.Ur_Puke3.Display_Puke()
        MainGame.Ur_Puke4.Display_Puke()
        MainGame.Ur_Puke5.Display_Puke()

        if 玩家数 >= 3:
            MainGame.En_Puke2_2.Display_Puke()
            MainGame.En_Puke2_1.Display_Puke()
        if 玩家数 >= 4:
            MainGame.En_Puke3_2.Display_Puke()
            MainGame.En_Puke3_1.Display_Puke()
        if 玩家数 >= 5:
            MainGame.En_Puke4_2.Display_Puke()
            MainGame.En_Puke4_1.Display_Puke()
        if 玩家数 >= 6:
            MainGame.En_Puke5_2.Display_Puke()
            MainGame.En_Puke5_1.Display_Puke()
        if 玩家数 >= 7:
            MainGame.En_Puke6_2.Display_Puke()
            MainGame.En_Puke6_1.Display_Puke()
        if 玩家数 >= 8:
            MainGame.En_Puke7_2.Display_Puke()
            MainGame.En_Puke7_1.Display_Puke()
        if 玩家数 == 9:
            MainGame.En_Puke8_2.Display_Puke()
            MainGame.En_Puke8_1.Display_Puke()
    def 流程展示():
        if MainGame.Game_Launcher >= 2:
            MainGame.Ur_Puke1.Surface_Puke = Puke_List[0]
            MainGame.Ur_Puke2.Surface_Puke = Puke_List[1]
            MainGame.Ur_Puke3.Surface_Puke = Puke_List[2]
        if MainGame.Game_Launcher >= 4:
            MainGame.Ur_Puke4.Surface_Puke = Puke_List[3]
        if MainGame.Game_Launcher >= 6:
            MainGame.Ur_Puke5.Surface_Puke = Puke_List[4]
        MainGame.My_Puke1_1.Surface_Puke = Puke_List[5]
        MainGame.My_Puke1_2.Surface_Puke = Puke_List[6]
        if 玩家数 >= 2 and MainGame.Game_Launcher >= 6:
            MainGame.En_Puke1_1.Surface_Puke = Puke_List[7]
            MainGame.En_Puke1_2.Surface_Puke = Puke_List[8]
        if 玩家数 >= 3 and MainGame.Game_Launcher >= 6:
            MainGame.En_Puke2_1.Surface_Puke = Puke_List[9]
            MainGame.En_Puke2_2.Surface_Puke = Puke_List[10]
        if 玩家数 >= 4 and MainGame.Game_Launcher >= 6:
            MainGame.En_Puke3_1.Surface_Puke = Puke_List[11]
            MainGame.En_Puke3_2.Surface_Puke = Puke_List[12]
        if 玩家数 >= 5 and MainGame.Game_Launcher >= 6:
            MainGame.En_Puke4_1.Surface_Puke = Puke_List[13]
            MainGame.En_Puke4_2.Surface_Puke = Puke_List[14]
        if 玩家数 >= 6 and MainGame.Game_Launcher >= 6:
            MainGame.En_Puke5_1.Surface_Puke = Puke_List[15]
            MainGame.En_Puke5_2.Surface_Puke = Puke_List[16]
        if 玩家数 >= 7 and MainGame.Game_Launcher >= 6:
            MainGame.En_Puke6_1.Surface_Puke = Puke_List[17]
            MainGame.En_Puke6_2.Surface_Puke = Puke_List[18]
        if 玩家数 >= 8 and MainGame.Game_Launcher >= 6:
            MainGame.En_Puke7_1.Surface_Puke = Puke_List[19]
            MainGame.En_Puke7_2.Surface_Puke = Puke_List[20]
        if 玩家数 >= 9 and MainGame.Game_Launcher >= 6:
            MainGame.En_Puke8_1.Surface_Puke = Puke_List[21]
            MainGame.En_Puke8_2.Surface_Puke = Puke_List[22]

    def GetEvent(self):
        global final_winner
        global data
        # 1.获取所有事件
        eventlist = pygame.event.get()
        # 2.对时间进行判断处理（1.点击关闭按钮 2.按下键盘上的某个按键）
        for event in eventlist:
            # 判断event.type 是否quit,如果时退出的话,直接调用程序结束方法
            if event.type == pygame.QUIT:
                self.EndGame()
            # 按F11全屏
            if event.type == pygame.KEYDOWN:
                #输出日志记录data.xlsx
                if event.key == pygame.K_F11:
                    print("全屏")
                    #写入日志data.xlsx
                    data = write_Data_Record(final_winner,data)


                if event.key == pygame.K_p and 1<MainGame.Game_Launcher<=9:
                    MainGame.流程展示()
                    MainGame.Game_Launcher += 1
                    print(MainGame.Game_Launcher)
                if event.key == pygame.K_0 and MainGame.Game_Launcher == 1:
                    Rules.玩家发牌接牌(self)
                    final_winner = Rules.判断各玩家牌大小(self)[1]
                    MainGame.Game_Launcher+= 1
                    # print(final_winner)
                    # print(Puke_List)
                    print(MainGame.Game_Launcher)
                    if event.key == pygame.K_0 and MainGame.Game_Launcher >= 2:
                        MainGame.流程展示()

                if event.key == pygame.K_9:
                    print("获胜者：")
            #鼠标点击“开始游戏“按钮
            if event.type == MOUSEBUTTONDOWN and MainGame.Game_Launcher == 0 and 280<event.pos[0]<1077 and 234<event.pos[1]<476:#按下鼠标时
                #游戏进程控制
                MainGame.Game_Launcher += 1
                print(event)#输出事件属性
                print(event.pos)#输出事件中的坐标
                print(pygame.mouse.get_pressed(num_buttons=3))#输出事件中的三个鼠标按键状态
            if event.type == MOUSEWHEEL:#鼠标滚轮滚动时
                print(event)
                print(event.y)

    def EndGame(self):
        exit()

    # 展示扑克
    def ShowMyPuke(self):
        MainGame.My_Puke1_1 = Puke(1400 / 2 - 75, 700 - 125)
        MainGame.My_Puke1_2 = Puke(1400 / 2 + 10, 700 - 125)
    def ShowE_Puke(self):
        MainGame.En_Puke1_1 = Puke(1400 / 5 - 75, 700 - 175)
        MainGame.En_Puke1_2 = Puke(1400 / 5 + 10, 700 - 175)
        if 玩家数>=3:
            MainGame.En_Puke2_1 = Puke(1400 / 8 - 75, 700 - 325)
            MainGame.En_Puke2_2 = Puke(1400 / 8 + 10, 700 - 325)
        if 玩家数>=4:
            MainGame.En_Puke3_1 = Puke(1400 / 8 - 75, 700 - 475)
            MainGame.En_Puke3_2 = Puke(1400 / 8 + 10, 700 - 475)
        if 玩家数>=5:
            MainGame.En_Puke4_1 = Puke(1400 / 5 - 75, 700 - 625)
            MainGame.En_Puke4_2 = Puke(1400 / 5 + 10, 700 - 625)
        if 玩家数>=6:
            MainGame.En_Puke5_1 = Puke(1400-(1400 / 5 - 75), 700 - 175)
            MainGame.En_Puke5_2 = Puke(1400-(1400 / 5 + 10), 700 - 175)
        if 玩家数>=7:
            MainGame.En_Puke6_1 = Puke(1400-(1400 / 8 - 75), 700 - 325)
            MainGame.En_Puke6_2 = Puke(1400-(1400 / 8 + 10), 700 - 325)
        if 玩家数>=8:
            MainGame.En_Puke7_1 = Puke(1400-(1400 / 8 - 75), 700 - 475)
            MainGame.En_Puke7_2 = Puke(1400-(1400 / 8 + 10), 700 - 475)
        if 玩家数==9:
            MainGame.En_Puke8_1 = Puke(1400-(1400 / 5 - 75), 700 - 625)
            MainGame.En_Puke8_2 = Puke(1400-(1400 / 5 + 10), 700 - 625)
    def ShowUrealPuke(self):
        # if MainGame.Game_Launcher >= 3:
            MainGame.Ur_Puke1 = Puke(1400 / 2 - 200, 700 - 425)
            MainGame.Ur_Puke2 = Puke(1400 / 2 - 100, 700 - 425)
            MainGame.Ur_Puke3 = Puke(1400 / 2 - 0, 700 - 425)
        # if MainGame.Game_Launcher >= 5:
            MainGame.Ur_Puke4 = Puke(1400 / 2 + 100, 700 - 425)
        # if MainGame.Game_Launcher >= 7:
            MainGame.Ur_Puke5 = Puke(1400 / 2 + 200, 700 - 425)
    def 开始游戏(content):
        pygame.font.init()
        #引用字体文件
        font = pygame.font.Font("./方正粗黑宋简体.ttf",200)
        #引用字体颜色、背景颜色
        text_sf = font.render(content, True, pygame.Color(100, 255, 100), pygame.Color(100,0, 100))
        return text_sf
    def 游戏结束(content):
        pygame.font.init()
        # 引用字体文件
        font = pygame.font.Font("./方正粗黑宋简体.ttf", 100)
        # 引用字体颜色、背景颜色
        text_sf = font.render(content, True, pygame.Color(100, 255, 100), pygame.Color(100, 0, 100))
        return text_sf
    def 获胜者展示(content):
        pygame.font.init()
        # 引用字体文件
        font = pygame.font.Font("./方正粗黑宋简体.ttf", 30)
        # 引用字体颜色、背景颜色
        text_sf = font.render(content, True, pygame.Color(100, 255, 100), pygame.Color(100, 0, 100))
        return text_sf

class BaseItem(pygame.sprite.Sprite):
    def __init__(self):
        pass

# 扑克类
class Puke(BaseItem):
    def __init__(self, left, top):
        # Puke_List清单与扑克图片对应
        self.images = {
            'a14': pygame.image.load('./图片汇总/a1.jpg'),
            'a2': pygame.image.load('./图片汇总/a2.png'),
            'a3': pygame.image.load('./图片汇总/a3.png'),
            'a4': pygame.image.load('./图片汇总/a4.png'),
            'a5': pygame.image.load('./图片汇总/a5.png'),
            'a6': pygame.image.load('./图片汇总/a6.png'),
            'a7': pygame.image.load('./图片汇总/a7.png'),
            'a8': pygame.image.load('./图片汇总/a8.png'),
            'a9': pygame.image.load('./图片汇总/a9.png'),
            'a10': pygame.image.load('./图片汇总/a10.png'),
            'a11': pygame.image.load('./图片汇总/a11.png'),
            'a12': pygame.image.load('./图片汇总/a12.png'),
            'a13': pygame.image.load('./图片汇总/a13.png'),
            'b14': pygame.image.load('./图片汇总/b1.png'),
            'b2': pygame.image.load('./图片汇总/b2.png'),
            'b3': pygame.image.load('./图片汇总/b3.png'),
            'b4': pygame.image.load('./图片汇总/b4.png'),
            'b5': pygame.image.load('./图片汇总/b5.png'),
            'b6': pygame.image.load('./图片汇总/b6.png'),
            'b7': pygame.image.load('./图片汇总/b7.png'),
            'b8': pygame.image.load('./图片汇总/b8.png'),
            'b9': pygame.image.load('./图片汇总/b9.png'),
            'b10': pygame.image.load('./图片汇总/b10.png'),
            'b11': pygame.image.load('./图片汇总/b11.png'),
            'b12': pygame.image.load('./图片汇总/b12.png'),
            'b13': pygame.image.load('./图片汇总/b13.png'),
            'c14': pygame.image.load('./图片汇总/c1.png'),
            'c2': pygame.image.load('./图片汇总/c2.png'),
            'c3': pygame.image.load('./图片汇总/c3.png'),
            'c4': pygame.image.load('./图片汇总/c4.png'),
            'c5': pygame.image.load('./图片汇总/c5.png'),
            'c6': pygame.image.load('./图片汇总/c6.png'),
            'c7': pygame.image.load('./图片汇总/c7.png'),
            'c8': pygame.image.load('./图片汇总/c8.png'),
            'c9': pygame.image.load('./图片汇总/c9.png'),
            'c10': pygame.image.load('./图片汇总/c10.png'),
            'c11': pygame.image.load('./图片汇总/c11.png'),
            'c12': pygame.image.load('./图片汇总/c12.png'),
            'c13': pygame.image.load('./图片汇总/c13.png'),
            'd14': pygame.image.load('./图片汇总/d1.png'),
            'd2': pygame.image.load('./图片汇总/d2.png'),
            'd3': pygame.image.load('./图片汇总/d3.png'),
            'd4': pygame.image.load('./图片汇总/d4.png'),
            'd5': pygame.image.load('./图片汇总/d5.png'),
            'd6': pygame.image.load('./图片汇总/d6.png'),
            'd7': pygame.image.load('./图片汇总/d7.png'),
            'd8': pygame.image.load('./图片汇总/d8.png'),
            'd9': pygame.image.load('./图片汇总/d9.png'),
            'd10': pygame.image.load('./图片汇总/d10.png'),
            'd11': pygame.image.load('./图片汇总/d11.png'),
            'd12': pygame.image.load('./图片汇总/d12.png'),
            'd13': pygame.image.load('./图片汇总/d13.png'),
            '背面': pygame.image.load('./图片汇总/背面.png')
        }
        self.Surface_Puke = '背面'
        self.image = self.images[self.Surface_Puke]
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top
        # print(self.images[self.Surface_Puke])

    # 展示扑克方法
    def Display_Puke(self):
        if MainGame.Game_Launcher ==1:
            self.Surface_Puke = '背面'
        self.image = self.images[self.Surface_Puke]
        MainGame.window.blit(self.image, self.rect)


# 规则制定
class Rules:
    def __init__(self):
        pass
    #发牌方法
    def 玩家发牌接牌(self):
        Rules.puke发牌(self)
        Rules.puke玩家接牌(self)
        # print(Puke_List1)
        # print(Puke_List1花色)
        # print(Puke_List2)
        # print(Puke_List2花色)
        # print(puke大小)
        # print(puke花色)
    def puke发牌(self):
        global 玩家数
        # a黑桃，b红桃，c方片，d梅花
        HuaSe = ('a', 'b', 'c', 'd')
        ShuZi = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)
        # 发牌数l
        l发牌数 = 0
        # time.time()
        while l发牌数 < (5 + 2 * 玩家数):
            i = random.randint(0, 3)
            j = random.randint(0, 12)
            k = str(HuaSe[i]) + str(ShuZi[j])
            # if MainGame.Puke_List == []:
            #     MainGame.Puke_List.append(str(k))
            l2 = l发牌数
            l发牌数 += 1
            for n in range(len(Puke_List)):
                if k == Puke_List[n]:
                    l发牌数 -= 1
                    break
            if l2 < l发牌数:
                Puke_List.append(str(k))
                puke花色.append(HuaSe[i])
                puke大小.append(ShuZi[j])
    #接牌方法
    def puke玩家接牌(self):
        global 玩家数
        global puke大小,puke花色
        global player1数字,玩家2数字,玩家3数字,玩家4数字,玩家5数字,玩家6数字,玩家7数字,玩家8数字,玩家9数字,player1花色,玩家2花色,玩家3花色,玩家4花色,玩家5花色,玩家6花色,玩家7花色,玩家8花色,玩家9花色
        i = 2
        while i <= 玩家数:
            if i == 2 and i <= 玩家数:
                player1数字.append(puke大小[0:5])
                player1数字.append(puke大小[5:7])
                玩家2数字.append(puke大小[0:5])
                玩家2数字.append(puke大小[7:9])
                player1花色.append(puke花色[0:5])
                player1花色.append(puke花色[5:7])
                玩家2花色.append(puke花色[0:5])
                玩家2花色.append(puke花色[7:9])
                player1数字 = Rules.数字数据处理(player1数字)
                玩家2数字 = Rules.数字数据处理(玩家2数字)
                player1花色 = Rules.花色数据处理(player1花色)
                玩家2花色 = Rules.花色数据处理(玩家2花色)
                # print(player1数字)
                # print(player1花色)
                # print(玩家2数字)
                # print(玩家2花色)
                i +=1
            if i == 3 and i <= 玩家数:
                玩家3数字.append(puke大小[0:5])
                玩家3数字.append(puke大小[9:11])
                玩家3数字 = Rules.数字数据处理(玩家3数字)
                玩家3花色.append(puke花色[0:5])
                玩家3花色.append(puke花色[9:11])
                玩家3花色 = Rules.花色数据处理(玩家3花色)

                # print(玩家3数字)
                # print(玩家3花色)
                i += 1
            if i == 4 and i <= 玩家数:
                玩家4数字.append(puke大小[0:5])
                玩家4数字.append(puke大小[11:13])
                玩家4数字 = Rules.数字数据处理(玩家4数字)
                # print(玩家4数字)
                玩家4花色.append(puke花色[0:5])
                玩家4花色.append(puke花色[11:13])
                玩家4花色 = Rules.花色数据处理(玩家4花色)
                # print(玩家4花色)
                i += 1
            if i == 5 and i <= 玩家数:
                玩家5数字.append(puke大小[0:5])
                玩家5数字.append(puke大小[13:15])
                玩家5数字 = Rules.数字数据处理(玩家5数字)
                # print(玩家5数字)
                玩家5花色.append(puke花色[0:5])
                玩家5花色.append(puke花色[13:15])
                玩家5花色 = Rules.花色数据处理(玩家5花色)
                # print(玩家5花色)
                i += 1
            if i == 6 and i <= 玩家数:
                玩家6数字.append(puke大小[0:5])
                玩家6数字.append(puke大小[15:17])
                玩家6数字 = Rules.数字数据处理(玩家6数字)
                # print(玩家6数字)
                玩家6花色.append(puke花色[0:5])
                玩家6花色.append(puke花色[15:17])
                玩家6花色 = Rules.花色数据处理(玩家6花色)
                # print(玩家6花色)
                i += 1
            if i == 7 and i <= 玩家数:
                玩家7数字.append(puke大小[0:5])
                玩家7数字.append(puke大小[17:19])
                玩家7数字 = Rules.数字数据处理(玩家7数字)
                # print(玩家7数字)
                玩家7花色.append(puke花色[0:5])
                玩家7花色.append(puke花色[17:19])
                玩家7花色 = Rules.花色数据处理(玩家7花色)
                # print(玩家7花色)
                i += 1
            if i == 8 and i <= 玩家数:
                玩家8数字.append(puke大小[0:5])
                玩家8数字.append(puke大小[19:21])
                玩家8数字 = Rules.数字数据处理(玩家8数字)
                # print(玩家8数字)
                玩家8花色.append(puke花色[0:5])
                玩家8花色.append(puke花色[19:21])
                玩家8花色 = Rules.花色数据处理(玩家8花色)
                # print(玩家8花色)
                i += 1
            if i == 9 and i <= 玩家数:
                玩家9数字.append(puke大小[0:5])
                玩家9数字.append(puke大小[21:23])
                玩家9数字 = Rules.数字数据处理(玩家9数字)
                # print(玩家9数字)
                玩家9花色.append(puke花色[0:5])
                玩家9花色.append(puke花色[21:23])
                玩家9花色 = Rules.花色数据处理(玩家9花色)
                # print(玩家9花色)
                i += 1
    def 数字数据处理(list):
        list_None = []
        for i in range(len(list)):
            for j in range(len(list[i])):
                list_None.append(list[i][j])
        Puke_List2.append(list_None)
        # print(Puke_List2)
        return list_None
    def 花色数据处理(list):
        list_None = []
        for i in range(len(list)):
            for j in range(len(list[i])):
                list_None.append(list[i][j])
        Puke_List2花色.append(list_None)
        return list_None
    #单个玩家牌型组合
    def 玩家牌型所有可能组合(list_2):
        list_none = []
        for i in list_2:
            list_none.append(Rules.puke7出2留5(i))
        # print(list_none)
        return list_none
    def puke7出2留5(list_1):
        list_2 = list_1.copy()
        list_none = []
        for i in range(7):
            for j in range(6):
                list_3 = list_2.copy()
                if len(list_3) == 7:
                    del (list_3[i])
                    del (list_3[j])
                    # print(list_3)
                    list_none.append(list_3)
        # print(len(list_none))
        # print(list_none)
        return list_none
    #牌型判断方法
    def 判断各玩家牌大小(self):
        list_none = []
        for i in range(玩家数):
            list_none.append(Rules.返回数字组合最大值(self)[i])
        # print(list_none)
        list_none1 = []
        list_none2 = []
        list_final = []
        list_final1 = []
        for i in range(len(list_none)):
            list_none1.append(Rules.玩家内部牌型判断(list_none[i]))
        #增加同花所有牌判定
        list_none同花判定 = []
        for i in range(len(Puke_List2花色)):
            list_none同花判定.append(Rules.puke同花顺牌型显示(Puke_List2[i],Puke_List2花色[i]))
        # print(list_none同花判定)
        # print(list_none1)
        for i in range(len(list_none同花判定)):
            if list_none同花判定[i][0] != 1 and list_none同花判定[i][0]>list_none1[i][0][0]:
                del list_none1[i]
                list_none1.insert(i,[list_none同花判定[i]])
        # print(list_none1)
        for i in range(玩家数):
            list_none2.append(list_none1[i][0][0])
        for i in range(玩家数):
            if max(list_none2) == list_none1[i][0][0]:
                list_final.append([i,list_none1[i][0]])
        # print("list_final")
        # print(list_final)
        list_final1.append(Rules.玩家之间牌型判断(list_final))
        print("list_final1")
        # print(list_final1)
        list_final1 = list_final1[0][0]
        print(list_final1)
        print(list_none1)
        return [list_none1,list_final1]
        # print(Puke_List2)
        # print(Puke_List2花色)
    def puke四条葫芦判断(list_1,list_2):
        list_1234 = Counter(list_1)  # 统计列表中相同数组的个数
        if len(Counter(list_1)) == 5:
            if Rules.puke顺子判断(list_1) != 5:
                # print("单牌")
                return [1,sorted(list_1),list_1,list_2]
            else:
                # print("顺子")
                return [5,[max(list_1)],list_1,list_2]
            # print(sorted(list_1))
            # print(sorted(list_1,reverse=True))#倒序排列
        if len(Counter(list_1)) == 4:
            # print("一对")
            list2 = Counter(list_1).values()
            # print(str(list(list2)))
            # 将值字典list_1中的值对应赋予list2,由于他们位置一一对应
            list_3 = []
            list_4 = []
            for i in range(4):
                if list(list2)[i] == 2:
                    list_4.insert(0,list(Counter(list_1))[i])
                if list(list2)[i] == 1:
                    list_3.append(list(Counter(list_1))[i])
                    # print("一对%g"%list(Counter(list_1))[i])
            list_4.append(sorted(list_3))
            return [2,list_4,list_1,list_2]
        if len(Counter(list_1)) == 3:
            # print("两队或三条")
            list2 = Counter(list_1).values()
            list_none = []
            list_none1 = []
            list_3 = []
            for i in range(3):
                if list(list2)[i] == 2:
                    # print("一对%g"%list(Counter(list_1))[i])
                    list_none.append(list(Counter(list_1))[i])
                if list(list2)[i] == 3:
                    list_none1.append(list(Counter(list_1))[i])
                if list(list2)[i] == 1:
                    list_3.append(list(Counter(list_1))[i])
            list_none = sorted(list_none)
            # print(list_none)
            for i in range(3):
                if list(list2)[i] == 2 and len(list_3)==1:
                    return [3, [sorted(list_none),list_3[0]], list_1,list_2]
                elif list(list2)[i] == 3 and len(list_3)>1:
                    # print("三条%g"%list(Counter(list_1))[i])
                    return [4, [list_none1,sorted(list_3)], list_1,list_2]
        if len(Counter(list_1)) == 2:
            list1 = list(Counter(list_1))
            list2 = Counter(list_1).values()
            list_none1 = []
            list_none2 = []
            for i in range(2):
                if list(list2)[i] == 2:
                    list_none1.append(list1[i])
                elif list(list2)[i] == 3:
                    list_none1.insert(0, list1[i])
                elif list(list2)[i] == 4:
                    list_none2.insert(0, list1[i])
                elif list(list2)[i] == 1:
                    list_none2.append(list1[i])
            for i in range(2):
                if list(list2)[i] == 2:
                    return [7, list_none1, list_1,list_2]
                elif list(list2)[i] == 3:
                    return [7, list_none1, list_1,list_2]
                elif list(list2)[i] == 4:
                    return [8, list_none2, list_1,list_2]
    def 返回数字组合最大值(self):
        list_none = Rules.数字牌型判断(Puke_List2)
        list_nonenone = []
        for i in range(len(list_none)):
            list_nonenone.append(list_none[i][0])
        list_none1 = []
        list_final = []

        for i in range(len(list_nonenone)):
            if i / 42 < 1:
                player1数字.append([1,list_none[i]])
            elif 1 <= i / 42 < 2:
                玩家2数字.append([2,list_none[i]])
            elif 2 <= i / 42 < 3:
                玩家3数字.append([3,list_none[i]])
            elif 3 <= i / 42 < 4:
                玩家4数字.append([4,list_none[i]])
            elif 4 <= i / 42 < 5:
                玩家5数字.append([5,list_none[i]])
            elif 5 <= i / 42 < 6:
                玩家6数字.append([6,list_none[i]])
            elif 6 <= i / 42 < 7:
                玩家7数字.append([7,list_none[i]])
            elif 7 <= i / 42 < 8:
                玩家8数字.append([8,list_none[i]])
            elif 8 <= i / 42 < 9:
                玩家9数字.append([9,list_none[i]])
        # print(player1数字)

        return player1数字,玩家2数字,玩家3数字,玩家4数字,玩家5数字,玩家6数字,玩家7数字,玩家8数字,玩家9数字
    def 数字牌型判断(list):
        global Puke_List1,Puke_List1花色,Puke_List2,Puke_List2花色
        global puke大小, puke花色
        global player1数字, 玩家2数字, 玩家3数字, 玩家4数字, 玩家5数字, 玩家6数字, 玩家7数字, 玩家8数字, 玩家9数字, player1花色, 玩家2花色, 玩家3花色, 玩家4花色, 玩家5花色, 玩家6花色, 玩家7花色, 玩家8花色, 玩家9花色
        list_final = []
        Puke_List1 = Rules.玩家牌型所有可能组合(Puke_List2)
        Puke_List1花色 = Rules.玩家牌型所有可能组合(Puke_List2花色)
        # print(Puke_List1)
        # for i in range(len(Puke_List1)):
        #     for j in range(len(Puke_List1[i])):
        #         if i == 0:
        #             player1数字 = Puke_List1[i]
        #             player1花色 = Puke_List1花色[i]
        #         elif i == 1:
        #             玩家2数字 = Puke_List1[i]
        #             玩家2花色 = Puke_List1花色[i]
        #         elif i == 2:
        #             玩家3数字 = Puke_List1[i]
        #             玩家3花色 = Puke_List1花色[i]
        #         elif i == 3:
        #             玩家4数字 = Puke_List1[i]
        #             玩家4花色 = Puke_List1花色[i]
        #         elif i == 4:
        #             玩家5数字 = Puke_List1[i]
        #             玩家5花色 = Puke_List1花色[i]
        #         elif i == 5:
        #             玩家6数字 = Puke_List1[i]
        #             玩家6花色 = Puke_List1花色[i]
        #         elif i == 6:
        #             玩家7数字 = Puke_List1[i]
        #             玩家7花色 = Puke_List1花色[i]
        #         elif i == 7:
        #             玩家8数字 = Puke_List1[i]
        #             玩家8花色 = Puke_List1花色[i]
        #         elif i == 8:
        #             玩家9数字 = Puke_List1[i]
        #             玩家9花色 = Puke_List1花色[i]
        for i in range(len(Puke_List1)):
            for j in range(len(Puke_List1[i])):
                list_final.append(Rules.puke四条葫芦判断(Puke_List1[i][j],Puke_List1花色[i][j]))
        # print(list_final)
        return list_final

    def 玩家之间牌型判断(list):
        list_1 = []
        list_final = []
        # print("list")
        # print(list)
        # print("hello")
        # print(list[0])
        if len(list)>1:
            for i in range(len(list)):
                list_1.append(list[i])
            n = list[i][1][0]
            if n == 1:
                list_final.append(Rules.玩家间单牌最大组合输出(list_1))
            if n == 2:
                list_final.append(Rules.玩家间小对最大组合输出(list_1))
            if n == 3:
                list_final.append(Rules.玩家间两对最大组合输出(list_1))
            if n == 4:
                list_final.append(Rules.玩家间三条最大组合输出(list_1))
            if n == 5:
                list_final.append(Rules.玩家间顺子最大组合输出(list_1))
            if n == 6:
                list_final.append(Rules.玩家间同花最大组合输出(list_1))
            if n == 7:
                list_final.append(Rules.玩家间葫芦最大组合输出(list_1))
            if n == 8:
                list_final.append(Rules.玩家间金刚最大组合输出(list_1))
            if n == 9:
                list_final.append(Rules.玩家间同花顺最大组合输出(list_1))
        elif len(list)==1:
            list_final = copy.copy([list])
        # print("玩家之间牌型判断")
        # print(list_final)
        return list_final
    def 玩家间单牌最大组合输出(list):
        list1 = list.copy()
        list2 = []
        list3 = []
        list4 = []
        list5 = []
        list6 = []
        list7 = []
        list8 = []
        list9 = []
        list10 = []
        list11 = []
        list12 = []
        list_final = []
        if len(list) > 1:
            for i in range(len(list)):
                # print(list[i][2])
                list2.append((list[i]))
                list3.append(max(list[i][1][1]))
            for i in range(len(list3)):
                if max(list3) == list3[i]:
                    list4.append(list2[i])
            list_final = list4
            if len(list_final) > 1:
                for i in range(len(list4)):
                    list5.append(list4[i][1][1][3])
                for i in range(len(list5)):
                    if max(list5) == list5[i]:
                        list6.append(list4[i])
                list_final = list6
                if len(list_final) > 1:
                    for i in range(len(list6)):
                        list7.append(list6[i][1][1][2])
                    for i in range(len(list7)):
                        if max(list7) == list7[i]:
                            list8.append(list6[i])
                    list_final = list8
                    if len(list_final) > 1:
                        for i in range(len(list_final)):
                            list9.append(list_final[i][1][1][1])
                        for i in range(len(list9)):
                            if max(list9) == list9[i]:
                                list10.append(list_final[i])
                        list_final = list10
                        if len(list_final) > 1:
                            for i in range(len(list_final)):
                                list11.append(list_final[i][1][1][0])
                            for i in range(len(list11)):
                                if max(list11) == list11[i]:
                                    list12.append(list_final[i])
                            list_final = list12
            for i in range(len(list2)):
                if list2[i] == list_final:
                    list_final = list1[i]
        elif len(list) == 1:
            list_final = list
        # print(list_final)
        return list_final
    def 玩家间小对最大组合输出(list):
        list1 = list.copy()
        list2 = []
        list3 = []
        list4 = []
        list5 = []
        list6 = []
        list7 = []
        list8 = []
        list9 = []
        list10 = []
        list_final = []
        if len(list) > 1:
            for i in range(len(list)):
                # print(list[i][2])
                list2.append((list[i]))
                list3.append(list[i][1][1][0])
            # print(list2)
            for i in range(len(list3)):
                if max(list3) == list3[i]:
                    list4.append(list2[i])
            # print(list4)
            list_final = list4
            if len(list_final) > 1:
                for i in range(len(list4)):
                    list5.append(list4[i][1][1][1][2])
                for i in range(len(list5)):
                    if max(list5) == list5[i]:
                        list6.append(list4[i])
                # print(list6)
                list_final = list6
                if len(list_final) > 1:
                    for i in range(len(list6)):
                        list7.append(list6[i][1][1][1][1])
                    for i in range(len(list7)):
                        if max(list7) == list7[i]:
                            list8.append(list6[i])
                    list_final = list8
                    if len(list_final) > 1:
                        for i in range(len(list_final)):
                            list9.append(list_final[i][1][1][1][0])
                        for i in range(len(list9)):
                            if max(list9) == list9[i]:
                                list10.append(list_final[i])
                        # print(list10)
                        list_final = list10
            for i in range(len(list2)):
                if list2[i] == list_final:
                    list_final = list1[i]
        elif len(list) == 1:
            list_final = list
        # print(list_final)
        return list_final
    def 玩家间两对最大组合输出(list):
        list1 = list.copy()
        list2 = []
        list3 = []
        list4 = []
        list5 = []
        list6 = []
        list7 = []
        list8 = []
        list_final = []
        if len(list) > 1:
            for i in range(len(list)):
                list2.append((list[i]))
                list3.append(list[i][1][1][0][1])
            for i in range(len(list3)):
                if max(list3) == list3[i]:
                    list4.append(list2[i])
            list_final = list4
            if len(list_final) > 1:
                for i in range(len(list4)):
                    list5.append(list4[i][1][1][0][0])
                for i in range(len(list5)):
                    if max(list5) == list5[i]:
                        list6.append(list4[i])
                list_final = list6
                if len(list_final) > 1:
                    for i in range(len(list6)):
                        list7.append(list6[i][1][1][1])
                    for i in range(len(list7)):
                        if max(list7) == list7[i]:
                            list8.append(list6[i])
                    list_final = list8
            for i in range(len(list2)):
                if list2[i] == list_final:
                    list_final = list1[i]
        elif len(list) == 1:
            list_final = list
        # print(list_final)
        return list_final
    def 玩家间三条最大组合输出(list):
        list1 = list.copy()
        list2 = []
        list3 = []
        list4 = []
        list5 = []
        list6 = []
        list7 = []
        list8 = []
        list_final = []
        if len(list) > 1:
            for i in range(len(list)):
                list2.append((list[i]))
                list3.append(list[i][1][1][0])
            for i in range(len(list3)):
                if max(list3) == list3[i]:
                    list4.append(list2[i])
            list_final = list4
            if len(list_final) > 1:
                for i in range(len(list4)):
                    list5.append(list4[i][1][1][1][1])
                for i in range(len(list5)):
                    if max(list5) == list5[i]:
                        list6.append(list4[i])
                list_final = list6
                if len(list_final) > 1:
                    for i in range(len(list6)):
                        list7.append(list6[i][1][1][1][0])
                    for i in range(len(list7)):
                        if max(list7) == list7[i]:
                            list8.append(list6[i])
                    list_final = list8
            for i in range(len(list2)):
                if list2[i] == list_final:
                    list_final = list1[i]
        elif len(list) == 1:
            list_final = list
        # print(list_final)
        return list_final
    def 玩家间葫芦最大组合输出(list):
        list1 = list.copy()
        list2 = []
        list3 = []
        list4 = []
        list5 = []
        list6 = []
        list_final = []
        if len(list) > 1:
            for i in range(len(list)):
                list2.append((list[i]))
                list3.append(list[i][1][1][0])
            for i in range(len(list3)):
                if max(list3) == list3[i]:
                    list4.append(list2[i])
            list_final = list4
            if len(list_final) > 1:
                for i in range(len(list4)):
                    list5.append(list4[i][1][1][1])
                for i in range(len(list5)):
                    if max(list5) == list5[i]:
                        list6.append(list4[i])
                list_final = list6
            for i in range(len(list2)):
                if list2[i] == list_final:
                    list_final = list1[i]
        elif len(list) == 1:
            list_final = list
        # print(list_final)
        return list_final
    def 玩家间金刚最大组合输出(list):
        list1 = list.copy()
        list2 = []
        list3 = []
        list4 = []
        list5 = []
        list6 = []
        list_final = []
        if len(list) > 1:
            for i in range(len(list)):
                list2.append((list[i]))
                list3.append(list[i][1][1][0])
            for i in range(len(list3)):
                if max(list3) == list3[i]:
                    list4.append(list2[i])
            list_final = list4
            if len(list_final) > 1:
                for i in range(len(list4)):
                    list5.append(list4[i][1][1][1])
                for i in range(len(list5)):
                    if max(list5) == list5[i]:
                        list6.append(list4[i])
                list_final = list6
            for i in range(len(list2)):
                if list2[i] == list_final:
                    list_final = list1[i]
        elif len(list) == 1:
            list_final = list
        # print(list_final)
        return list_final
    def 玩家间顺子最大组合输出(list):
        list1 = list.copy()
        list2 = []
        list3 = []
        list4 = []
        list_final = []
        if len(list) > 1:
            for i in range(len(list)):
                list2.append((list[i]))
                list3.append(list[i][1][1])
            for i in range(len(list3)):
                if max(list3) == list3[i]:
                    list4.append(list2[i])
            list_final = list4
            for i in range(len(list2)):
                if list2[i] == list_final:
                    list_final = list1[i]
        elif len(list) == 1:
            list_final = list
        # print(list_final)
        return list_final
    def 玩家间同花最大组合输出(list):
        list1 = list.copy()
        list2 = []
        list3 = []
        list4 = []
        list5 = []
        list6 = []
        list7 = []
        list8 = []
        list9 = []
        list10 = []
        list11 = []
        list12 = []
        list_final = []
        if len(list) > 1:
            for i in range(len(list)):
                # print(list[i][2])
                list2.append((list[i]))
                list3.append(max(list[i][1][1][1]))
            for i in range(len(list3)):
                if max(list3) == list3[i]:
                    list4.append(list2[i])
            list_final = list4
            if len(list_final) > 1:
                for i in range(len(list4)):
                    list5.append(list4[i][1][1][1][3])
                for i in range(len(list5)):
                    if max(list5) == list5[i]:
                        list6.append(list4[i])
                list_final = list6
                if len(list_final) > 1:
                    for i in range(len(list6)):
                        list7.append(list6[i][1][1][1][2])
                    for i in range(len(list7)):
                        if max(list7) == list7[i]:
                            list8.append(list6[i])
                    list_final = list8
                    if len(list_final) > 1:
                        for i in range(len(list_final)):
                            list9.append(list_final[i][1][1][1][1])
                        for i in range(len(list9)):
                            if max(list9) == list9[i]:
                                list10.append(list_final[i])
                        list_final = list10
                        if len(list_final) > 1:
                            for i in range(len(list_final)):
                                list11.append(list_final[i][1][1][1][0])
                            for i in range(len(list11)):
                                if max(list11) == list11[i]:
                                    list12.append(list_final[i])
                            list_final = list12
            for i in range(len(list2)):
                if list2[i] == list_final:
                    list_final = list1[i]
        elif len(list) == 1:
            list_final = list
        # print(list_final)
        return list_final
    def 玩家间同花顺最大组合输出(list):
        list1 = list.copy()
        list2 = []
        list3 = []
        list4 = []
        list_final = []
        if len(list) > 1:
            for i in range(len(list)):
                list2.append((list[i]))
                list3.append(list[i][1][1][4])
            for i in range(len(list3)):
                if max(list3) == list3[i]:
                    list4.append(list2[i])
            list_final = list4
            for i in range(len(list2)):
                if list2[i] == list_final:
                    list_final = list1[i]
        elif len(list) == 1:
            list_final = list
        # print(list_final)
        return list_final

    def 玩家内部牌型判断(list):
        list_1 = []
        list_2 = []
        list_3 = []
        list_final = []
        for i in range(7, len(list)):
            list_1.append(list[i][1][0])
        # print(list_1)
        for i in range(len(list_1)):
            if max(list_1) == list_1[i]:
                list_2.append(i)
                list_3.append(list[i + 7][1])
        # print(list_2)
        # print(list_3)
        # print(list[0 + 7])
        n = list_3[0][0]
        if n == 1:
            list_final.append(Rules.单牌最大组合输出(list_3))
        if n == 2:
            list_final.append(Rules.小对最大组合输出(list_3))
        if n == 3:
            list_final.append(Rules.两对最大组合输出(list_3))
        if n == 4:
            list_final.append(Rules.三条最大组合输出(list_3))
        if n == 5:
            list_final.append(Rules.顺子最大组合输出(list_3))
        if n == 6:
            list_final.append(Rules.同花最大组合输出(list_3))
        if n == 7:
            list_final.append(Rules.葫芦最大组合输出(list_3))
        if n == 8:
            list_final.append(Rules.金刚最大组合输出(list_3))
        if n == 9:
            list_final.append(Rules.同花顺最大组合输出(list_3))
        # print("内部牌型判断")
        # print(list_final)
        return list_final
    def 单牌最大组合输出(list):
        list1 = list.copy()
        list2 = []
        list3 = []
        list4 = []
        list5 = []
        list6 = []
        list7 = []
        list8 = []
        list9 = []
        list10 = []
        list11 = []
        list12 = []
        list_final = []
        if len(list) > 1:
            for i in range(len(list)):
                # print(list[i][2])
                list2.append((list[i]))
                list3.append(max(list[i][1]))
            for i in range(len(list3)):
                if max(list3) == list3[i]:
                    list4.append(list2[i])
            list_final = list4
            if len(list_final) > 1:
                for i in range(len(list4)):
                    list5.append(list4[i][1][3])
                for i in range(len(list5)):
                    if max(list5) == list5[i]:
                        list6.append(list4[i])
                list_final = list6
                if len(list_final) > 1:
                    for i in range(len(list6)):
                        list7.append(list6[i][1][2])
                    for i in range(len(list7)):
                        if max(list7) == list7[i]:
                            list8.append(list6[i])
                    list_final = list8
                    if len(list_final) > 1:
                        for i in range(len(list_final)):
                            list9.append(list_final[i][1][1])
                        for i in range(len(list9)):
                            if max(list9) == list9[i]:
                                list10.append(list_final[i])
                        list_final = list10
                        if len(list_final) > 1:
                            for i in range(len(list_final)):
                                list11.append(list_final[i][1][0])
                            for i in range(len(list11)):
                                if max(list11) == list11[i]:
                                    list12.append(list_final[i])
                            list_final = list12
                            if len(list_final) > 1:
                                list_final = list_final[0]
            for i in range(len(list2)):
                if list2[i] == list_final:
                    list_final = list1[i]
        elif len(list) == 1:
            list_final = list
        # print(list_final)
        return list_final
    def 小对最大组合输出(list):
        list1 = list.copy()
        list2 = []
        list3 = []
        list4 = []
        list5 = []
        list6 = []
        list7 = []
        list8 = []
        list9 = []
        list10 = []
        list_final = []
        if len(list) > 1:
            for i in range(len(list)):
                # print(list[i][2])
                list2.append((list[i]))
                list3.append(list[i][1][0])
            # print(list2)
            for i in range(len(list3)):
                if max(list3) == list3[i]:
                    list4.append(list2[i])
            # print(list4)
            list_final = list4
            if len(list_final) > 1:
                for i in range(len(list4)):
                    list5.append(list4[i][1][1][2])
                for i in range(len(list5)):
                    if max(list5) == list5[i]:
                        list6.append(list4[i])
                # print(list6)
                list_final = list6
                if len(list_final) > 1:
                    for i in range(len(list6)):
                        list7.append(list6[i][1][1][1])
                    for i in range(len(list7)):
                        if max(list7) == list7[i]:
                            list8.append(list6[i])
                    list_final = list8
                    if len(list_final) > 1:
                        for i in range(len(list_final)):
                            list9.append(list_final[i][1][1][0])
                        for i in range(len(list9)):
                            if max(list9) == list9[i]:
                                list10.append(list_final[i])
                        # print(list10)
                        list_final = list10
                        if len(list_final) > 1:
                            list_final = list_final[0]
            for i in range(len(list2)):
                if list2[i] == list_final:
                    list_final = list1[i]
        elif len(list) == 1:
            list_final = list
        # print(list_final)
        return list_final
    def 两对最大组合输出(list):
        list1 = list.copy()
        list2 = []
        list3 = []
        list4 = []
        list5 = []
        list6 = []
        list7 = []
        list8 = []
        list_final = []
        if len(list) > 1:
            for i in range(len(list)):
                list2.append((list[i]))
                list3.append(list[i][1][0][1])
            for i in range(len(list3)):
                if max(list3) == list3[i]:
                    list4.append(list2[i])
            list_final = list4
            if len(list_final) > 1:
                for i in range(len(list4)):
                    list5.append(list4[i][1][0][0])
                for i in range(len(list5)):
                    if max(list5) == list5[i]:
                        list6.append(list4[i])
                list_final = list6
                if len(list_final) > 1:
                    for i in range(len(list6)):
                        list7.append(list6[i][1][1])
                    for i in range(len(list7)):
                        if max(list7) == list7[i]:
                            list8.append(list6[i])
                    list_final = list8
                    if len(list_final) > 1:
                        list_final = list_final[0]
            for i in range(len(list2)):
                if list2[i] == list_final:
                    list_final = list1[i]
        elif len(list) == 1:
            list_final = list
        # print(list_final)
        return list_final
    def 三条最大组合输出(list):
        list1 = list.copy()
        list2 = []
        list3 = []
        list4 = []
        list5 = []
        list6 = []
        list7 = []
        list8 = []
        list_final = []
        if len(list) > 1:
            for i in range(len(list)):
                list2.append((list[i]))
                list3.append(list[i][1][0])
            for i in range(len(list3)):
                if max(list3) == list3[i]:
                    list4.append(list2[i])
            list_final = list4
            if len(list_final) > 1:
                for i in range(len(list4)):
                    list5.append(list4[i][1][1][1])
                for i in range(len(list5)):
                    if max(list5) == list5[i]:
                        list6.append(list4[i])
                list_final = list6
                if len(list_final) > 1:
                    for i in range(len(list6)):
                        list7.append(list6[i][1][1][0])
                    for i in range(len(list7)):
                        if max(list7) == list7[i]:
                            list8.append(list6[i])
                    list_final = list8
                    if len(list_final) > 1:
                        list_final = list_final[0]
            for i in range(len(list2)):
                if list2[i] == list_final:
                    list_final = list1[i]
        elif len(list) == 1:
            list_final = list
        # print(list_final)
        return list_final
    def 葫芦最大组合输出(list):
        list1 = list.copy()
        list2 = []
        list3 = []
        list4 = []
        list5 = []
        list6 = []
        list_final = []
        if len(list) > 1:
            for i in range(len(list)):
                list2.append((list[i]))
                list3.append(list[i][1][0])
            for i in range(len(list3)):
                if max(list3) == list3[i]:
                    list4.append(list2[i])
            list_final = list4
            if len(list_final) > 1:
                for i in range(len(list4)):
                    list5.append(list4[i][1][1])
                for i in range(len(list5)):
                    if max(list5) == list5[i]:
                        list6.append(list4[i])
                list_final = list6
                if len(list_final) > 1:
                    list_final = list_final[0]
            for i in range(len(list2)):
                if list2[i] == list_final:
                    list_final = list1[i]
        elif len(list) == 1:
            list_final = list
        # print(list_final)
        return list_final
    def 金刚最大组合输出(list):
        list1 = list.copy()
        list2 = []
        list3 = []
        list4 = []
        list5 = []
        list6 = []
        list_final = []
        if len(list) > 1:
            for i in range(len(list)):
                list2.append((list[i]))
                list3.append(list[i][1][0])
            for i in range(len(list3)):
                if max(list3) == list3[i]:
                    list4.append(list2[i])
            list_final = list4
            if len(list_final) > 1:
                for i in range(len(list4)):
                    list5.append(list4[i][1][1])
                for i in range(len(list5)):
                    if max(list5) == list5[i]:
                        list6.append(list4[i])
                list_final = list6
                if len(list_final) > 1:
                    list_final = list_final[0]
            for i in range(len(list2)):
                if list2[i] == list_final:
                    list_final = list1[i]
        elif len(list) == 1:
            list_final = list
        # print(list_final)
        return list_final
    def 顺子最大组合输出(list):
        list1 = list.copy()
        list2 = []
        list3 = []
        list4 = []
        list_final = []
        if len(list) > 1:
            for i in range(len(list)):
                list2.append((list[i]))
                list3.append(list[i][1])
            for i in range(len(list3)):
                if max(list3) == list3[i]:
                    list4.append(list2[i])
            list_final = list4
            if len(list_final) > 1:
                list_final = list_final[0]
            for i in range(len(list2)):
                if list2[i] == list_final:
                    list_final = list1[i]
        elif len(list) == 1:
            list_final = list
        # print(list_final)
        return list_final
    def 同花最大组合输出(list):
        list1 = list.copy()
        list2 = []
        list3 = []
        list4 = []
        list5 = []
        list6 = []
        list7 = []
        list8 = []
        list9 = []
        list10 = []
        list11 = []
        list12 = []
        list_final = []
        if len(list) > 1:
            for i in range(len(list)):
                # print(list[i][2])
                list2.append((list[i]))
                list3.append(max(list[i][1][1]))
            for i in range(len(list3)):
                if max(list3) == list3[i]:
                    list4.append(list2[i])
            list_final = list4
            if len(list_final) > 1:
                for i in range(len(list4)):
                    list5.append(list4[i][1][1][3])
                for i in range(len(list5)):
                    if max(list5) == list5[i]:
                        list6.append(list4[i])
                list_final = list6
                if len(list_final) > 1:
                    for i in range(len(list6)):
                        list7.append(list6[i][1][1][2])
                    for i in range(len(list7)):
                        if max(list7) == list7[i]:
                            list8.append(list6[i])
                    list_final = list8
                    if len(list_final) > 1:
                        for i in range(len(list_final)):
                            list9.append(list_final[i][1][1][1])
                        for i in range(len(list9)):
                            if max(list9) == list9[i]:
                                list10.append(list_final[i])
                        list_final = list10
                        if len(list_final) > 1:
                            for i in range(len(list_final)):
                                list11.append(list_final[i][1][1][0])
                            for i in range(len(list11)):
                                if max(list11) == list11[i]:
                                    list12.append(list_final[i])
                            list_final = list12
                            if len(list_final) > 1:
                                list_final = list_final[0]
            for i in range(len(list2)):
                if list2[i] == list_final:
                    list_final = list1[i]
        elif len(list) == 1:
            list_final = list
        # print(list_final)
        return list_final
    def 同花顺最大组合输出(list):
        list1 = list.copy()
        list2 = []
        list3 = []
        list4 = []
        list_final = []
        if len(list) > 1:
            for i in range(len(list)):
                list2.append((list[i]))
                list3.append(list[i][1][4])
            for i in range(len(list3)):
                if max(list3) == list3[i]:
                    list4.append(list2[i])
            list_final = list4
            if len(list_final) > 1:
                list_final = list_final[0]
            for i in range(len(list2)):
                if list2[i] == list_final:
                    list_final = list1[i]
        elif len(list) == 1:
            list_final = list
        # print(list_final)
        return list_final

    def puke顺子判断(list_1):
        list_2 = sorted(list_1)
        n = 0
        # print(list_1)
        # print(list_2)
        # print(type(list_2[n+1]))
        # print(type(list_2[n]+1))
        for i in range(4):
            if list_2[n] + 1 == list_2[n + 1]:
                n += 1
                if n == 4:
                    # print("顺子")
                    return 5

    def puke同花判定重做(list_2):
        for i in range(len(Counter(list_2))):
            if list(Counter(list_2).values())[i] >= 5:
                return list(Counter(list_2).keys())[i]
            else:
                return 1
    def puke同花顺牌型显示(list_1, list_2):
        list_none = []
        n = Rules.puke同花判定重做(list_2)
        if n == 1:
            # print("散牌")
            return 1, n,list_none
        if n != 1:
            list_3 = []
            list_4 = []
            for i in range(len(list_2)):
                if list_2[i] == n:
                    list_3.append(i)
            for i in list_3:
                list_4.append(list_1[i])
            list_3 = []
            for i in range(len(list_4)):
                list_3.append(list_4[i])
            y = Rules.puke大顺子判断(list_3)
            if y[0] != 5:
                for i in range(5):
                    list_none.append(list_3[i])
                return 6, [n,sorted(list_none)], list_none,[n,n,n,n,n]
            if y[0] == 5:
                list_none = y[1]
                return 9, [n,sorted(list_none)], list_none,[n,n,n,n,n]
    def puke大顺子判断(list_1):
        # print(list_1)
        # print(sorted(list_1))
        list_2 = sorted(list_1)
        # print(len(list_2)-1)
        list_none = []
        n = 0
        for i in range(len(list_2) - 1):

            if list_2[i] + 1 == list_2[i + 1]:
                # print(list_2[j])
                list_none.append(list_2[i])
                n += 1
                if n == 4:
                    list_none.append(list_2[i + 1])
                    # print(list_none)
                elif n == 5:
                    del (list_none[4])
                    del (list_none[0])
                    list_none.append(list_2[i + 1])
                    # print(list_none)
                elif n == 6:
                    del (list_none[4])
                    del (list_none[0])
                    list_none.append(list_2[i + 1])
                    # print(list_none)
        if n >= 4:
            return 5, list_none
        else:
            return 1, list_none
# 出牌按钮类
class Iput:
    pass


# 技能按钮类
class Skill:
    pass


# 机器人行为
class Enemy_Beheavy:
    pass


# 背景图片、荷官类
class Woman:
    pass


# 音效类
class Music:
    pass


# 动画特效类
class Flash:
    pass


MainGame().startGame()