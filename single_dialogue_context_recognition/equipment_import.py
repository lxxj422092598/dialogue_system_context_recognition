import xlrd
import MySQLdb

db = MySQLdb.connect(host="localhost", user="root", passwd="w123123456", db="xiaoduo")
c = db.cursor()
db.set_character_set('utf8')
c.execute('SET NAMES utf8;')
c.execute('SET CHARACTER SET utf8;')
c.execute('SET character_set_connection=utf8;')

ExcelFile = xlrd.open_workbook(r'E:\学习资料\烟草局设备信息管理\阎良区局计算机设备信息登记表.xlsx')
sheet = ExcelFile.sheet_by_index(0)
#打印sheet的名称，行数，列数
print(sheet.name, sheet.nrows, sheet.ncols)
#获取整行或者整列的值

for i in range(3, sheet.nrows):
    if(sheet.row_values(i) != ['', '', '', '', '', '', '', '', '', '', '', '', '', '']):
        print(sheet.row_values(i))
        try:
            sql = """INSERT INTO tbl_equipments(BRAND,CONFIGURE_TIME,DEPARTMENT,USER,CPU,RAM,ROM,OS,BROWSER,OFFICE_SOFTWARE,USED_FOR,IP_ADDRESS,MAC_ADDRESS,REGION)
               VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')""" % \
              (sheet.row_values(i)[1], sheet.row_values(i)[2], sheet.row_values(i)[3], sheet.row_values(i)[4], sheet.row_values(i)[5], sheet.row_values(i)[6],
               sheet.row_values(i)[7], sheet.row_values(i)[8], sheet.row_values(i)[9], sheet.row_values(i)[10], sheet.row_values(i)[11], sheet.row_values(i)[12],
               sheet.row_values(i)[13], '阎良')
            c.execute(sql)
            db.commit()
            rs = c.fetchall()
        except Exception as err:
            print(sql)
            print(err)
            db.rollback()
