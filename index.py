import xlrd
import data_process
##该函数返回result和ref
##result是将excel表格内容变为由字典组成的list变量
##ref是dict值，为参考关系，可由该变量查找对应英雄的条目在result中的位置，如result[dict['夏洛特']]
def get_data(filename, sheetnum):
    dir_case = filename
    data = xlrd.open_workbook(dir_case)
    table = data.sheets()[sheetnum]
    nor = table.nrows
    nol = table.ncols
    result = []
    ref = {}
    for i in range(1,nor):
        data_row = {}
        for j in range(nol):
            title = table.cell_value(0,j)
            value = table.cell_value(i,j)
            data_row[title] = value
        result.append(data_row)
        ref[table.cell_value(i,0)] = i - 1
        

    return result,ref

# if __name__=='__main__':
#     result,ref = get_data('英雄名称.xlsx',0)
#     #print(result)
#
#     #print(ref)
#     print(result[0])
#