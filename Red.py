import xlrd
import index
import random
from data_process import process_data
from core_algorithm import evaluate_function,update
from random_gen import random_gen_anti_hero
from ban import ban,ban_enemy

def red_ban_function(OurSpareHero,WholeChart):
    BannedHero=[]
    BlueBannedHero=[]
    RedBannedHero=[]

    #蓝方一ban
    print('**********************')
    print('蓝方一ban')
    BlueBan1=ban_enemy(BlueBannedHero, RedBannedHero,WholeChart)
    print('蓝方禁用英雄: ', BlueBan1)
    BlueBannedHero.append(BlueBan1)
    BannedHero.append(BlueBan1)
    print('我方已ban英雄：',RedBannedHero)
    print('敌方已ban英雄：',BlueBannedHero)

    #红方一ban
    print('**********************')
    print('红方一ban')
    RecommandBanHero1=ban(OurSpareHero, RedBannedHero, BlueBannedHero, WholeChart)
    print('RecommandBanHero1: ', RecommandBanHero1)
    print('请输入我方一ban英雄：')
    RedBannedHero1=input()
    RedBannedHero.append(RedBannedHero1)
    BannedHero.append(RedBannedHero1)
    print('我方已ban英雄：',RedBannedHero)
    print('敌方已ban英雄：',BlueBannedHero)

    #蓝方二ban
    print('**********************')
    print('蓝方二ban')
    BlueBan2=ban_enemy(BlueBannedHero, RedBannedHero,WholeChart)
    print('蓝方禁用英雄: ', BlueBan2)
    BlueBannedHero.append(BlueBan2)
    BannedHero.append(BlueBan2)
    print('我方已ban英雄：',RedBannedHero)
    print('敌方已ban英雄：',BlueBannedHero)

    #红方二ban
    print('**********************')
    print('红方二ban')
    RecommandBanHero2=ban(OurSpareHero, RedBannedHero, BlueBannedHero, WholeChart)
    print('RecommandBanHero2: ', RecommandBanHero2)
    print('请输入我方二ban英雄：')
    RedBannedHero2=input()
    RedBannedHero.append(RedBannedHero2)
    BannedHero.append(RedBannedHero2)
    print('我方已ban英雄：',RedBannedHero)
    print('敌方已ban英雄：',BlueBannedHero)
    
    return BannedHero 

def red_pick_function(OurSpareHero, BannedHero, WholeChart):
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
    EnemyHero1, EnemyChosenHero = random_gen_anti_hero(WholeChart,EnemyChosenHero,OurChosenHero)
    i = 0
    while i < len(OurSpareHero):
        if OurSpareHero[i] in EnemyChosenHero:
            del OurSpareHero[i]
        i = i+1
    print('敌方选用英雄：',EnemyHero1)
    print('我方已选英雄：',OurChosenHero)
    print('敌方已选英雄：',EnemyChosenHero)

    #######
    #红方一二选
    #######
    print('**********************')
    print('红方一选')
    RecommandHero1,OurSpareHero= evaluate_function(OurSpareHero, OurChosenHero, EnemyChosenHero,WholeChart)
    print('RecommandHero1: ', RecommandHero1)
    print('请输入我方一选英雄：')
    RedChosenHero1=input()
    OurSpareHero, OurChosenHero=update(RedChosenHero1,OurSpareHero,OurChosenHero,WholeChart)
    print('红方二选')
    RecommandHero2,OurSpareHero= evaluate_function(OurSpareHero, OurChosenHero, EnemyChosenHero,WholeChart)
    print('RecommandHero2: ', RecommandHero2)
    print('请输入我方二选英雄：')
    RedChosenHero2=input()
    OurSpareHero, OurChosenHero=update(RedChosenHero2,OurSpareHero,OurChosenHero,WholeChart)
    print('我方已选英雄：',OurChosenHero)
    print('敌方已选英雄：',EnemyChosenHero)
    
    #######
    #蓝方二三选, 随机函数运行一次更新一次敌方已选英雄
    #######
    print('**********************')
    print('蓝方二三选')
    EnemyHero2, EnemeyChosenHero = random_gen_anti_hero(WholeChart,EnemyChosenHero,OurChosenHero)
    EnemyHero3, EnemeyChosenHero = random_gen_anti_hero(WholeChart,EnemyChosenHero,OurChosenHero)
    while i < len(OurSpareHero):
        if OurSpareHero[i] in EnemyChosenHero:
            del OurSpareHero[i]
        i = i+1
    print('敌方选用英雄：',EnemyHero2,EnemyHero3)
    print('我方已选英雄：',OurChosenHero)
    print('敌方已选英雄：',EnemyChosenHero)

    #######
    #红方三四选
    #######
    print('**********************')
    print('红方三选')
    RecommandHero3,OurSpareHero= evaluate_function(OurSpareHero, OurChosenHero, EnemyChosenHero,WholeChart)
    print('RecommandHero3: ', RecommandHero3)
    print('请输入我方三选英雄：')
    RedChosenHero3=input()
    OurSpareHero, OurChosenHero=update(RedChosenHero3,OurSpareHero,OurChosenHero,WholeChart)
    print('红方四选')
    RecommandHero4,OurSpareHero= evaluate_function(OurSpareHero, OurChosenHero, EnemyChosenHero,WholeChart)
    print('RecommandHero4: ', RecommandHero4)
    print('请输入我方四选英雄：')
    RedChosenHero4=input()
    OurSpareHero, OurChosenHero=update(RedChosenHero4,OurSpareHero,OurChosenHero,WholeChart)
    print('我方已选英雄：',OurChosenHero)
    print('敌方已选英雄：',EnemyChosenHero)

    #######
    #蓝方四五选, 随机函数运行一次更新一次敌方已选英雄
    #######
    print('**********************')
    print('蓝方四五选')
    EnemyHero4, EnemeyChosenHero = random_gen_anti_hero(WholeChart,EnemyChosenHero,OurChosenHero)
    EnemyHero5, EnemeyChosenHero = random_gen_anti_hero(WholeChart,EnemyChosenHero,OurChosenHero)
    while i < len(OurSpareHero):
        if OurSpareHero[i] in EnemyChosenHero:
            del OurSpareHero[i]
        i = i+1
    print('敌方选用英雄：',EnemyHero4,EnemyHero5)
    print('我方已选英雄：',OurChosenHero)
    print('敌方已选英雄：',EnemyChosenHero)

    #######
    #红方五选
    #######
    print('**********************')
    print('红方五选')
    RecommandHero5,OurSpareHero= evaluate_function(OurSpareHero, OurChosenHero, EnemyChosenHero,WholeChart)
    print('RecommandHero5: ', RecommandHero5)
    print('请输入我方五选英雄：')
    RedChosenHero5=input()
    OurSpareHero, OurChosenHero=update(RedChosenHero5,OurSpareHero,OurChosenHero,WholeChart)

    print('**********************')
    print('我方最终阵容：', OurChosenHero)
    print('敌方最终阵容：', EnemeyChosenHero)

    return OurChosenHero, EnemeyChosenHero
    
if __name__=='__main__':
    OurSpareHero =['狂铁', '梦奇', '铠', '杨玉环', '女娲', '干将莫邪', '李元芳', '后羿', '狄仁杰','鲁班大师','瑶','蔡文姬','李白','韩信','孙悟空']
    BannedHero=['鲁班七号','孙悟空','盾山','镜']