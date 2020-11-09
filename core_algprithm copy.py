import xlrd
import index
import random
import data_process
'''note:
评价函数
输入参数解释：
ourSpareHero：我方备选英雄， 这是一个一维数组，里面包含着0~15个英雄名称，每一个英雄名称为字符串格式
ourChosenHero：我方已选英雄， 一维数组，包含着我们已选的英雄，字符串格式。
enemyChosenHero：敌方已选择英雄， 格式同上
wholeChart:所有数据，畅哥用excel表格生成的数据。

输出参数解释：
选出的英雄,经过评价后选择出的英雄。
newOurSpareHero:我方备选英雄(新),选择英雄后对我方备选英雄数组进行更新，删除已选择英雄分路的英雄。
newOurChosenHero: 我方已选英雄（新）：增加选出的英雄。
'''
#def evaluate_function(ourSpareHero, ourChosenHero, enemyChosenHero,wholeChart):

if __name__=='__main__':



    wholeChart,ref = index.get_data('英雄名称.xlsx',0)
    wholeChart=data_process.process_data(wholeChart)
    ######################################################################
    #调参汇总
    #初始化分数参数
    #winRateFactor: 胜率因子 0.6
    #appearFactor:   登场因子 0.2
    #BanFactor:        ban因子 0.2
    winRateFactor = 0.6
    appearFactor = 0.2
    BanFactor  = 0.2
    #配合参数，将我方已选择英雄ourChosenHero中的英雄中的最佳搭档。当我方选择n名英雄，会有2*n名最佳搭档。
    # 我将这2n个名单构成一个数组，并和ourSpareHero中的名单进行对比，如果有则加companyHeroAddScore分
    companyHeroAddScore = 0.2
    #克制参数，将地方选择
    companyHeroAddScore = 0.2



    ######################################################################

   

#该部分均为初始化操作，实际换成算法是该部分均可省略
#####################################################################
#note: 下面一大部分将来由函数参数ourSpareHero，enemyChosenHero，ourChosenHero三个参数构成替换
    heroBranch=[[],[],[],[],[]]
    for i in range(len(wholeChart)):
        if wholeChart[i]["分路"]=="上路":
            heroBranch[0].append(wholeChart[i])
        elif wholeChart[i]["分路"]=="中路":
            heroBranch[1].append(wholeChart[i])
        elif wholeChart[i]["分路"]=="下路":
            heroBranch[2].append(wholeChart[i])
        elif wholeChart[i]["分路"]=="打野":
            heroBranch[3].append(wholeChart[i])
        elif wholeChart[i]["分路"]=="辅助":
            heroBranch[4].append(wholeChart[i])
        
    #测试用，随机出初始化英雄
       
    #for i in range(len())
    ourChosenHero=[]
    enemyChosenHero=[]
    ourSpareHero=[]
   

    for i in range(3):
        for j in range(7,10):
            ourSpareHero.append(heroBranch[i][j]["英雄名称"])
    

    enemyChosenHero=['鲁班七号','孙悟空']
    ourChosenHero=['盾山','李白']


    print("ourSpaceHero=",ourSpareHero)
    print("enemyChosenHero=",enemyChosenHero)
    print("ourChosenHero=",ourChosenHero)

    #测试所需要数据准备完成
    ##############################################################################

    #最终分数finalHeroScore，最后的评价标准
    finalHeroScore=[]
    
    #初始英雄分数 由胜率，登场率，BAN率构成
    originalHeroScore=[]
    
    #配合己方英雄分数,和己方已选英雄的配合程度
    #note by qzh 在后面会根据ourSpareHero长度重新定义
    companyHeroScore=[]
    
    #克制敌方英雄分数，克制地方英雄分数
    antiEnemyHeroScore=[]
    #note by qzh 在后面会根据ourSpareHero长度重新定义

    #被敌方英雄克制分数，考虑为负数
    EnemyHeroRestrainScore=[]
    #note by qzh 在后面会根据ourSpareHero长度重新定义    
#############################################################################
    #originalHeroScore
    #初始化英雄评分，初始分均为胜率，登场率，BAN率三者的加权求和。
    #note by qzh，对于基本的评分，由胜率，登场率，ban率构成，这个比率均是可以调整的。
    #(附：胜率，ban率，登场率均已归一化)
    #winRateFactor: 胜率因子 0.6
    #appearFactor:   登场因子 0.2
    #BanFactor:        ban因子 0.2
    #所有数值定义均在本文件最上面定义。


    for i in range(len(ourSpareHero)):
        name=ourSpareHero[i]

        heroData = data_process.get_data_from_name(wholeChart,name)
        
        
        #print('herodata',heroData)
        winRateScore = heroData["胜率"]
        #print('胜率',winRateScore)
        appearScore = heroData["登场率"]
        #print('登场率',appearScore)
        BanScore = heroData["ban率"]
        #print('ban率',BanScore)
        whole_score = winRateScore*winRateFactor+appearScore*appearFactor+BanScore*BanFactor
        #print('whole_socre',whole_socre)
        whole_score = round(whole_score,3)
        originalHeroScore.append(whole_score)
        
    print('originalHeroScore',originalHeroScore)
    # 初始化originalHeroScore数据完成
#############################################################################
#companyHeroScore
    # 考虑英雄间配合情况
    # 思路：将我方已选择英雄ourChosenHero中的英雄中的最佳搭档。当我方选择n名英雄，会有2*n名最佳搭档。
    # 我将这2n个名单构成一个数组，并和ourSpareHero中的名单进行对比，如果有则加companyHeroAddScore分（note:这个分值后续调参时候可能会修改），
    # 并将结果存储在companyHeroScore，注意这里需要主要的是，如果在名单里加companyHeroAddScore分，不在计0分，有重叠可以叠加。
    # note by qzh 2020/10/17

    #companyHeroAddScore,这个参数比例可以调节,调参请看文件开头。
    
    companyHero=[]
    #初始化配合分数均为0
    companyHeroScore=[0]*len(ourSpareHero)

    for i in range(len(ourChosenHero)):
        name = ourChosenHero[i]
        heroData = data_process.get_data_from_name(wholeChart,name)
        companyHero.append(heroData['最佳搭档1'])
        companyHero.append(heroData['最佳搭档2'])

    print('companyHero',companyHero)

    for i in range(len(companyHero)):
        for j in range(len(ourSpareHero)):
            if companyHero[i]==ourSpareHero[j]:
                companyHeroScore[i]=companyHeroScore[i]+companyHeroAddScore

    print('companyHeroScore',companyHeroScore)
    #配合分数完成
    ################################################################################
#antiEnemyHeroScore
    #下一步分析克制敌方英雄的关系。
    #思路:敌方选择了n名英雄，相对应的会有3n名克制地方的英雄，由于克制指数的存在，不能再用数组来简单的表示。因此这里我们选择字典
    #来代替。最后的形式为eg:{'夏洛特':0.4}.这样的形式。不过最后仍会整理成为一个数组的形式antiEnemyHeroScore
    
    #初始化克制分数均为0
    antiEnemyHeroScore=[0]*len(ourSpareHero)
    antiKey={}
    for i in range(len(enemyChosenHero)):
        name = enemyChosenHero[i]
        heroData = data_process.get_data_from_name(wholeChart,name)
        if heroData['被克制英雄1'] in antiKey:
            antiKey[heroData['被克制英雄1']]=heroData['被克制指数1']+antiKey[heroData['被克制英雄1']]
        else:
            antiKey[heroData['被克制英雄1']]=heroData['被克制指数1']

        if heroData['被克制英雄2'] in antiKey:
            antiKey[heroData['被克制英雄2']]=heroData['被克制指数2']+antiKey[heroData['被克制英雄2']]
        else:
            antiKey[heroData['被克制英雄2']]=heroData['被克制指数2']

        if heroData['被克制英雄3'] in antiKey:
            antiKey[heroData['被克制英雄3']]=heroData['被克制指数3']+antiKey[heroData['被克制英雄3']]
        else:
            antiKey[heroData['被克制英雄3']]=heroData['被克制指数3']

    #print('antikey',antiKey)
    antiEnemyHeroList = list(antiKey.keys())
   # print('antiEnemyHeroList',antiEnemyHeroList)
    
    for i in range(len(ourSpareHero)):
        if ourSpareHero[i] in antiEnemyHeroList:
            antiEnemyHeroScore[i] = antiKey[ourSpareHero[i]]
    
    print('antiEnemyHeroScore',antiEnemyHeroScore)






    ################################################################################
    #EnemyHeroRestrainScore
    #分析我方备选英雄被敌方克制。思路和上面一致。仍然是从敌方英雄出发，不过最后是分析敌方的克制英雄而不是被克制英雄。
    EnemyHeroRestrainScore=[0]*len(ourSpareHero)
    EnemyHeroRestrainKey={}
    for i in range(len(enemyChosenHero)):
        name = enemyChosenHero[i]
        heroData = data_process.get_data_from_name(wholeChart,name)
        if heroData['克制英雄1'] in antiKey:
            EnemyHeroRestrainKey[heroData['克制英雄1']]=heroData['克制指数1']+EnemyHeroRestrainKey[heroData['克制英雄1']]
        else:
            EnemyHeroRestrainKey[heroData['克制英雄1']]=heroData['克制指数1']

        if heroData['克制英雄2'] in antiKey:
            EnemyHeroRestrainKey[heroData['克制英雄2']]=heroData['克制指数2']+EnemyHeroRestrainKey[heroData['克制英雄2']]
        else:
            EnemyHeroRestrainKey[heroData['克制英雄2']]=heroData['克制指数2']

        if heroData['克制英雄3'] in antiKey:
            EnemyHeroRestrainKey[heroData['克制英雄3']]=heroData['克制指数3']+EnemyHeroRestrainKey[heroData['克制英雄3']]
        else:
            EnemyHeroRestrainKey[heroData['克制英雄3']]=heroData['克制指数3']

   # print('EnemyHeroRestrainkey',EnemyHeroRestrainKey)
    EnemyHeroRestrainList = list(EnemyHeroRestrainKey.keys())
    #print('EnemyHeroRestrainList',EnemyHeroRestrainList)
    
    for i in range(len(ourSpareHero)):
        if ourSpareHero[i] in EnemyHeroRestrainList:
            EnemyHeroRestrainScore[i] = EnemyHeroRestrainKey[ourSpareHero[i]]
    
    print('EnemyHeroRestrainScore',EnemyHeroRestrainScore)

    ##########################################################################################
    #至此，所有参数均获得了：
    #originalHeroScore
    #companyHeroScore
    #antiEnemyHeroScore
    #EnemyHeroRestrainScore
    finalHeroScore=[0]*len(ourSpareHero)
    for i in range(len(ourSpareHero)):
    #note:最后的参数配置也可以调参
        finalHeroScore[i] = originalHeroScore[i]*0.8+companyHeroScore[i]*1+antiEnemyHeroScore[i]*0.8-EnemyHeroRestrainScore[i]*1
        finalHeroScore[i] = round(finalHeroScore[i],3)
    print('finalHeroScore',finalHeroScore)
    
    finalRecommandHero = ourSpareHero[finalHeroScore.index(max(finalHeroScore))]
    print('finalRecommandHero',finalRecommandHero)
    heroData=data_process.get_data_from_name(wholeChart,finalRecommandHero)
    branch = heroData['分路']
    print('branch',branch)
    #接下来为更新自己的ourSpareHero, ourChosenHero
    print('ourSpareHero',ourSpareHero)

    newOurSpareHero=[]

    for i in range(len(ourSpareHero)):
        newOurSpareHero.append(ourSpareHero[i])

    for k in range(len(ourSpareHero)):

        name = ourSpareHero[k]
        heroData = data_process.get_data_from_name(wholeChart ,name)
        if heroData['分路'] == branch:
           newOurSpareHero.remove(name)
    
    print('newOurSpareHero',newOurSpareHero)

    ourChosenHero.append(finalRecommandHero)
    print('newourChosenHero',ourChosenHero)



