import xlrd
import index
import random
import data_process
# note:
#input: 处理过的表格：wholeChart （type(list))
#          敌方英雄：enemyChosenHero（type(list))
#          我方英雄 ：ourChosenHero（type(list))
#output:随机生成的英雄 字符串
#             敌方英雄： 更新后的enemyChosenHero（type(list))
def random_gen_anti_hero(wholeChart,enemyChosenHero,ourChosenHero):
    heroBranch=[[],[],[],[],[]]
    for i in range(len(wholeChart)):
        if wholeChart[i]["分路"]=="上路":
            heroBranch[0].append(wholeChart[i]['英雄名称'])
        elif wholeChart[i]["分路"]=="中路":
            heroBranch[1].append(wholeChart[i]['英雄名称'])
        elif wholeChart[i]["分路"]=="下路":
            heroBranch[2].append(wholeChart[i]['英雄名称'])
        elif wholeChart[i]["分路"]=="打野":
            heroBranch[3].append(wholeChart[i]['英雄名称'])
        elif wholeChart[i]["分路"]=="辅助":
            heroBranch[4].append(wholeChart[i]['英雄名称'])


    for i in range(len(enemyChosenHero)):
        name = enemyChosenHero[i]
        heroData = data_process.get_data_from_name(wholeChart,name)   
        if heroData['分路']== "上路":  
            heroBranch[0].remove(name)
        if heroData['分路']== "中路":  
            heroBranch[1].remove(name)
        if heroData['分路']== "下路":  
            heroBranch[2].remove(name)
        if heroData['分路']== "打野":  
            heroBranch[3].remove(name)
        if heroData['分路']== "辅助":  
            heroBranch[4].remove(name)

    for i in range(len(ourChosenHero)):
        name = ourChosenHero[i]
        heroData = data_process.get_data_from_name(wholeChart,name)   
        if heroData['分路']== "上路":  
            heroBranch[0].remove(name)
        if heroData['分路']== "中路":  
            heroBranch[1].remove(name)
        if heroData['分路']== "下路":  
            heroBranch[2].remove(name)
        if heroData['分路']== "打野":  
            heroBranch[3].remove(name)
        if heroData['分路']== "辅助":  
            heroBranch[4].remove(name)

    #print('heroBranch',heroBranch)
    anti_hero_branch=[]

    for i in range(len(enemyChosenHero)):
        name = enemyChosenHero[i]
        heroData = data_process.get_data_from_name(wholeChart,name)
        anti_hero_branch.append(heroData['分路'])
    #print('敌方已选分路：', anti_hero_branch)

    if '上路' not in anti_hero_branch:
        hero = random.choice(heroBranch[0])

    elif '中路' not in anti_hero_branch:
       hero= random.choice(heroBranch[1])
    elif '下路' not in anti_hero_branch:
        hero =random.choice(heroBranch[2])
    elif '打野' not in anti_hero_branch:
        hero = random.choice(heroBranch[3])
    elif '辅助' not in anti_hero_branch:
        hero =  random.choice(heroBranch[4])

    #print('antihero',hero)
    #print('branch',data_process.get_data_from_name(wholeChart,hero)['分路'])
    enemyChosenHero.append(hero)
    #print('敌方已选英雄：', enemyChosenHero)
    return hero, enemyChosenHero

if __name__=='__main__':
    wholeChart,ref = index.get_data('Glory_of_Kings-v2\英雄名称.xlsx',0)
    wholeChart=data_process.process_data(wholeChart)
    enemyChosenHero=['鲁班七号','孙悟空']
    ourChosenHero=['盾山','李白']
    hero,enemyenemyChosenHero=random_gen_anti_hero(wholeChart,enemyChosenHero,ourChosenHero)
    print(enemyenemyChosenHero)

