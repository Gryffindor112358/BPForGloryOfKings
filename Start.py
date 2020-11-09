import xlrd
import index
import data_process
from random_gen import random_gen_anti_hero
from core_algorithm import evaluate_function
from Blue import blue_pick_function,blue_ban_function
from Red import red_pick_function,red_ban_function
from ban import ban

WholeChart,ref = index.get_data('Glory_of_Kings-v4\Glory_of_Kings-v3\Glory_of_Kings-v2\英雄名称.xlsx',0)

#输入红蓝方
print('请输入选边:（蓝方或红方）')
Side=input()

#输入我方与选英雄（输入一个英雄后按回车）
OurSpareHero = []
print('请输入我方预选英雄:')
for x in range(0,15):
	OurSpareHero.append(input()) 
print('输入完毕')
print('我方备选英雄：',OurSpareHero)

#ban
if Side=='蓝方':
    BannedHero=blue_ban_function(OurSpareHero,WholeChart)
elif Side=='红方':
    BannedHero=red_ban_function(OurSpareHero,WholeChart)
print('**********************')
print('双方禁用英雄：',BannedHero)

#pick
if Side=='蓝方':
    OurChosenHero, EnemeyChosenHero=blue_pick_function(OurSpareHero, BannedHero, WholeChart)
elif Side=='红方':
    OurChosenHero, EnemeyChosenHero=red_pick_function(OurSpareHero,BannedHero,WholeChart)