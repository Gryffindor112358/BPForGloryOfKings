import index


###################################
#function:数据归一化，统一归一化到0~1
#time: 2020/10/17
#author : qzh
####################################


def process_data(wholeChart):  # 输入原始表格，输出数据归一化的表格。
    #胜率
    temp=[]
    for i in range(len(wholeChart)):
        temp.append(wholeChart[i]['胜率'])
    max_temp=max(temp)
    for i in range(len(temp)):
        wholeChart[i]['胜率']=round(temp[i]/max_temp,3)

    #登场率
    temp=[]
    for i in range(len(wholeChart)):
        temp.append(wholeChart[i]['登场率'])
    max_temp=max(temp)
    for i in range(len(temp)):
        wholeChart[i]['登场率']=round(temp[i]/max_temp,3)

    #ban率
    temp=[]
    for i in range(len(wholeChart)):
        temp.append(wholeChart[i]['ban率'])
    max_temp=max(temp)
    for i in range(len(temp)):
        wholeChart[i]['ban率']=round(temp[i]/max_temp,3)

    #克制指数1
    temp=[]
    for i in range(len(wholeChart)):
        temp.append(wholeChart[i]['克制指数1'])
    max_temp=max(temp)
    for i in range(len(temp)):
        wholeChart[i]['克制指数1']=round(temp[i]/max_temp,3)

    #克制指数2
    temp=[]
    for i in range(len(wholeChart)):
        temp.append(wholeChart[i]['克制指数2'])
    max_temp=max(temp)
    for i in range(len(temp)):
        wholeChart[i]['克制指数2']=round(temp[i]/max_temp,3)

    #克制指数3
    temp=[]
    for i in range(len(wholeChart)):
        temp.append(wholeChart[i]['克制指数3'])
    max_temp=max(temp)
    for i in range(len(temp)):
        wholeChart[i]['克制指数3']=round(temp[i]/max_temp,3)

    #被克制指数1
    temp=[]
    for i in range(len(wholeChart)):
        temp.append(wholeChart[i]['被克制指数1'])
    max_temp=max(temp)
    for i in range(len(temp)):
        wholeChart[i]['被克制指数1']=round(temp[i]/max_temp,3)

    #被克制指数2
    temp=[]
    for i in range(len(wholeChart)):
        temp.append(wholeChart[i]['被克制指数2'])
    max_temp=max(temp)
    for i in range(len(temp)):
        wholeChart[i]['被克制指数2']=round(temp[i]/max_temp,3)

    #被克制指数3
    temp=[]
    for i in range(len(wholeChart)):
        temp.append(wholeChart[i]['被克制指数3'])
    max_temp=max(temp)
    for i in range(len(temp)):
        wholeChart[i]['被克制指数3']=round(temp[i]/max_temp,3)

    #被克制指数2
    temp=[]
    for i in range(len(wholeChart)):
        temp.append(wholeChart[i]['被克制指数2'])
    max_temp=max(temp)
    for i in range(len(temp)):
        wholeChart[i]['被克制指数2']=round(temp[i]/max_temp,3)

    return wholeChart

#####################
#函数功能：由名称获得该英雄的数据
#eg: get_data_from_name(wholeChart,'夏洛特')
def get_data_from_name(wholeChart,name):
    for i in range(len(wholeChart)):
        if name==wholeChart[i]['英雄名称']:
            return wholeChart[i]
   
    return 'error,please check it again'

# if __name__=='__main__':
#     WholeChart,ref = index.get_data('Glory_of_Kings-v4\Glory_of_Kings-v3\Glory_of_Kings-v2\英雄名称.xlsx',0)
#     WholeHero=get_whole_hero_name(WholeChart)
#     print(WholeHero)





    