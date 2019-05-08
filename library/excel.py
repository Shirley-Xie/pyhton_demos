xlrd:
#打开excel文件
data=xlrd.open_workbook('data.xlsx')     
#获取第一张工作表（通过索引的方式）
table=data.sheets()[0] 
#data_list用来存放数据
data_list=[]    
#将table中第一行的数据读取并添加到data_list中
data_list.extend(table.row_values(0))
#打印出第一行的全部数据
for item in data_list:
    print item



xlwt:

data=xlwt.Workbook()
table=data.add_sheet('name', cell_overwrite_ok=True)
table.write(0,0,u'呵呵')

data.save('test.xls')


在原有的表单上加字段
oldwb = xlrd.open_workbook(gConst['xls']['filename'], formatting_info=True)
newwb = copy(oldwb)
newws = newwb.get_sheet(0)

newws.write(1,2,"value1")
newwb.save(gConst['xls']['fileName']);
