'''
    根据bp规则，禁用英雄环节:蓝方4楼-红方4楼-蓝方5楼-红方5楼
    因此根据已知己方备选英雄，己方已ban英雄和敌方已ban英雄可给出一个建议ban的英雄

    该函数的整体规则如下：
    首先选出克制我方英雄的列表
    接着在该名单中去除我方的备选英雄，己方已ban英雄和敌方已ban英雄，对剩余英雄进行分析
    由胜率、出场率、ban率和被克制指数综合计算，取得分最高的英雄ban掉
'''


import index
from data_process import get_data_from_name,process_data
import data_process
import random


def ban(ourSpareHero, ourbanHero, enemybanHero, wholeChart):
    ##ban英雄备选名单
    to_ban_list = []
    to_ban_list_score = []


    ##胜率比重
    winRateFactor = 0.6
    ##出场率比重
    appearFactor = 0.2
    ##ban率比重
    BanFactor = 0.2


    ##ban英雄备选名单中去除我方英雄备选名单，我方已ban名单以及对方已ban名单
    wholeChart = data_process.process_data(wholeChart)
    for i in range(len(ourSpareHero)):
        #print(ourSpareHero[i])
        HeroData = data_process.get_data_from_name(wholeChart, ourSpareHero[i])
        #print(HeroData)
        if (HeroData['被克制英雄1'] not in to_ban_list) and (HeroData['被克制英雄1'] not in ourSpareHero):
            to_ban_list.append(HeroData['被克制英雄1'])
            to_ban_list_score.append(HeroData['被克制指数1'])
        if (HeroData['被克制英雄2'] not in to_ban_list) and (HeroData['被克制英雄2'] not in ourSpareHero):
            to_ban_list.append(HeroData['被克制英雄2'])
            to_ban_list_score.append(HeroData['被克制指数2'])
    #print(to_ban_list)
    #print(ourbanHero)
    if len(ourbanHero)!=0:
        for i in range(len(ourbanHero)):
            if ourbanHero[i] in to_ban_list:
                del to_ban_list_score[(to_ban_list.index(ourbanHero[i]))]
                del to_ban_list[(to_ban_list.index(ourbanHero[i]))]
                
    if len(enemybanHero)!=0:
        for i in range(len(enemybanHero)):
            if enemybanHero[i] in to_ban_list:
                del to_ban_list_score[(to_ban_list.index(enemybanHero[i]))]
                del to_ban_list[(to_ban_list.index(enemybanHero[i]))]

    if '艾琳' in to_ban_list:
        tmp = to_ban_list.index('艾琳')
        del to_ban_list_score[tmp]
        del to_ban_list[tmp]
    #print(to_ban_list)
    ##to_ban_list中英雄待ban的综合评分
    banScore = []

    for i in range(len(to_ban_list)):
        HeroData = data_process.get_data_from_name(wholeChart, to_ban_list[i])
        #print('Herodata',HeroData)
        winRateScore = HeroData['胜率']
        #print('胜率',winRateScore)
        appearScore = HeroData["登场率"]
        # print('登场率',appearScore)
        BanScore = HeroData["ban率"]
        Score1 = winRateScore*winRateFactor + appearScore*appearFactor + BanScore*BanFactor
        Score2 = to_ban_list_score[i]
        banScore.append(0.7*Score1+0.3*Score2)

    max_score = max(banScore)
    # print(banScore)
    loc = banScore.index(max_score)
    # print(loc)

    return to_ban_list[loc]

def ban_enemy(ourbanHero, enemybanHero,wholeChart):
    to_ban_list = []
    for i in range(len(wholeChart)):
        to_ban_list.append(wholeChart[i]['英雄名称'])

    for i in range(len(ourbanHero)):
        if ourbanHero[i] in to_ban_list:
            del to_ban_list[to_ban_list.index(ourbanHero[i])]
    for i in range(len(enemybanHero)):
        if enemybanHero[i] in to_ban_list:
            del to_ban_list[to_ban_list.index(enemybanHero[i])]

    loc = random.randint(0,len(to_ban_list))
    return to_ban_list[loc]

if __name__=='__main__':
    wholeChart, ref = index.get_data('Glory_of_Kings-v4\Glory_of_Kings-v3\Glory_of_Kings-v2\英雄名称.xlsx',0)
    ourSpareHero =['狂铁', '梦奇', '铠', '杨玉环', '女娲', '干将莫邪', '李元芳', '后羿', '狄仁杰','鲁班大师','瑶','蔡文姬','李白','韩信','孙悟空']
    ourbanHero = []
    enemybanHero = []
    ban_hero = ban(ourSpareHero,ourbanHero,enemybanHero,wholeChart)

    # HeroData = data_process.get_data_from_name(wholeChart, '阿轲')
    # winRateScore = HeroData['胜率']
    # print('胜率',winRateScore)

    #print(ban_hero)



