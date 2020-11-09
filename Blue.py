import xlrd
import index
import random
from data_process import process_data
from core_algorithm import evaluate_function,update
from random_gen import random_gen_anti_hero
from ban import ban,ban_enemy

def blue_ban_function(OurSpareHero,WholeChart):
    BannedHero=[]
    BlueBannedHero=[]
    RedBannedHero=[]

    #蓝方一ban
    print('**********************')
    print('蓝方一ban')
    RecommandBanHero1=ban(OurSpareHero, BlueBannedHero, RedBannedHero, WholeChart)
    print('RecommandBanHero1: ', RecommandBanHero1)
    print('请输入我方一ban英雄：')
    BlueBannedHero1=input()
    BlueBannedHero.append(BlueBannedHero1)
    BannedHero.append(BlueBannedHero1)
    print('我方已ban英雄：',BlueBannedHero)
    print('敌方已ban英雄：',RedBannedHero)

    #红方一ban
    print('**********************')
    print('红方一ban')
    RedBan1=ban_enemy(BlueBannedHero, RedBannedHero,WholeChart)
    print('红方禁用英雄: ', RedBan1)
    RedBannedHero.append(RedBan1)
    BannedHero.append(RedBan1)
    print('我方已ban英雄：',BlueBannedHero)
    print('敌方已ban英雄：',RedBannedHero)

    #蓝方二ban
    print('**********************')
    print('蓝方二ban')
    RecommandBanHero2=ban(OurSpareHero, BlueBannedHero, RedBannedHero, WholeChart)
    print('RecommandBanHero2: ', RecommandBanHero2)
    print('请输入我方二ban英雄：')
    BlueBannedHero2=input()
    BlueBannedHero.append(BlueBannedHero2)
    BannedHero.append(BlueBannedHero2)
    print('我方已ban英雄：',BlueBannedHero)
    print('敌方已ban英雄：',RedBannedHero)

    #红方二ban
    print('**********************')
    print('红方二ban')
    RedBan2=ban_enemy(BlueBannedHero, RedBannedHero,WholeChart)
    print('红方禁用英雄: ', RedBan2)
    RedBannedHero.append(RedBan2)
    BannedHero.append(RedBan2)
    print('我方已ban英雄：',BlueBannedHero)
    print('敌方已ban英雄：',RedBannedHero)
    
    return BannedHero 




def blue_pick_function(OurSpareHero, BannedHero, WholeChart):
    ########
    #首先进行数据总表的初始化
    ########
    WholeChart= process_data(WholeChart) 

    ########
    #初始我方已选英雄与敌方已选英雄都是空表
    ########
    OurChosenHero = []
    EnemyChosenHero = []


    ######
    #蓝方一选
    ######
    print('**********************')
    print('蓝方一选')
    RecommandHero1,OurSpareHero= evaluate_function(OurSpareHero, OurChosenHero, EnemyChosenHero,WholeChart)
    print('RecommandHero1: ', RecommandHero1)
    print('请输入我方一选英雄：')
    BlueChosenHero1=input()
    OurSpareHero, OurChosenHero=update(BlueChosenHero1,OurSpareHero,OurChosenHero,WholeChart)
    print('我方已选英雄：',OurChosenHero)
    print('敌方已选英雄：',EnemyChosenHero)
    

    #######
    #红方一二选, 随机函数运行一次更新一次敌方已选英雄
    #######
    print('**********************')
    print('红方一二选')
    EnemyHero1, EnemyChosenHero = random_gen_anti_hero(WholeChart,EnemyChosenHero,OurChosenHero)   
    EnemyHero2, EnemyChosenHero = random_gen_anti_hero(WholeChart,EnemyChosenHero,OurChosenHero)
    i = 0
    while i < len(OurSpareHero):
        if OurSpareHero[i] in EnemyChosenHero:
            del OurSpareHero[i]
        i = i+1
    print('敌方选用英雄：',EnemyHero1,EnemyHero2)
    print('我方已选英雄：',OurChosenHero)
    print('敌方已选英雄：',EnemyChosenHero)

    ######
    #蓝方二三选
    ######
    print('**********************')
    print('蓝方二选')
    RecommandHero2,OurSpareHero= evaluate_function(OurSpareHero, OurChosenHero, EnemyChosenHero,WholeChart)
    print('RecommandHero2: ', RecommandHero2)
    print('请输入我方二选英雄：')
    BlueChosenHero2=input()
    OurSpareHero, OurChosenHero=update(BlueChosenHero2,OurSpareHero,OurChosenHero,WholeChart)
    print('蓝方三选')
    RecommandHero3,OurSpareHero= evaluate_function(OurSpareHero, OurChosenHero, EnemyChosenHero,WholeChart)
    print('RecommandHero3: ', RecommandHero3)
    print('请输入我方三选英雄：')
    BlueChosenHero3=input()
    OurSpareHero, OurChosenHero=update(BlueChosenHero3,OurSpareHero,OurChosenHero,WholeChart)
    print('我方已选英雄：',OurChosenHero)
    print('敌方已选英雄：',EnemyChosenHero)

    #######
    #红方三四选, 随机函数运行一次更新一次敌方已选英雄
    #######
    print('**********************')
    print('红方三四选')
    EnemyHero3, EnemeyChosenHero = random_gen_anti_hero(WholeChart,EnemyChosenHero,OurChosenHero)
    EnemyHero4, EnemeyChosenHero = random_gen_anti_hero(WholeChart,EnemyChosenHero,OurChosenHero)
    #for i in range(len(OurSpareHero)): 
    #    if OurSpareHero[i] in EnemyChosenHero:
    #        del OurSpareHero[i]
    while i < len(OurSpareHero):
        if OurSpareHero[i] in EnemyChosenHero:
            del OurSpareHero[i]
        i = i+1
    print('敌方选用英雄：',EnemyHero3,EnemyHero4)
    print('我方已选英雄：',OurChosenHero)
    print('敌方已选英雄：',EnemyChosenHero)

    #######
    #蓝方四五选
    #######
    print('**********************')
    print('蓝方四选')
    RecommandHero4,OurSpareHero= evaluate_function(OurSpareHero, OurChosenHero, EnemyChosenHero,WholeChart)
    print('RecommandHero4: ', RecommandHero4)
    print('请输入我方四选英雄：')
    BlueChosenHero4=input()
    OurSpareHero, OurChosenHero=update(BlueChosenHero4,OurSpareHero,OurChosenHero,WholeChart)
    print('蓝方五选')
    RecommandHero5,OurSpareHero= evaluate_function(OurSpareHero, OurChosenHero, EnemyChosenHero,WholeChart)
    print('RecommandHero5: ', RecommandHero5)
    print('请输入我方五选英雄：')
    BlueChosenHero5=input()
    OurSpareHero, OurChosenHero=update(BlueChosenHero5,OurSpareHero,OurChosenHero,WholeChart)
    print('我方已选英雄：',OurChosenHero)
    print('敌方已选英雄：',EnemyChosenHero)

    #######
    #红方五选, 随机函数运行一次更新一次敌方已选英雄
    #######
    print('**********************')
    print('红方五选')
    EnemyHero5, EnemeyChosenHero = random_gen_anti_hero(WholeChart,EnemyChosenHero,OurChosenHero)
    print('敌方选用英雄：',EnemyHero5)

    print('**********************')
    print('我方最终阵容：', OurChosenHero)
    print('敌方最终阵容：', EnemeyChosenHero)

    return OurChosenHero, EnemeyChosenHero


if __name__=='__main__':
    WholeChart,ref = index.get_data('Glory_of_Kings-v4\Glory_of_Kings-v3\Glory_of_Kings-v2\英雄名称.xlsx',0)
    OurSpareHero =['狂铁', '梦奇', '铠', '杨玉环', '女娲', '干将莫邪', '李元芳', '后羿', '狄仁杰','鲁班大师','瑶','蔡文姬','李白','韩信','孙悟空']
    BannedHero=blue_ban_function(OurSpareHero,WholeChart)
    OurChosenHero, EnemeyChosenHero = blue_pick_function(OurSpareHero, BannedHero, WholeChart)
    print(BannedHero)
    print(OurChosenHero)
    print(EnemeyChosenHero)
    



    