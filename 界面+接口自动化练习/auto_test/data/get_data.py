import xlrd

# wb = xlrd.open_workbook("info.xls")
# table = wb.sheet_by_index(0)
# table = wb.sheet_by_name("Sheet1")
#
# r = table.row_values(0)
# print(r)
# c = table.col_values(1)
# print(c[2])
# g = table.cell(0,0)
# print(g)

class excel_data():
    def sheet1(self,s,n):
        try:
            wb = xlrd.open_workbook(r"D:\python_work\auto_test\data\info.xls")
            table = wb.sheet_by_index(s-1)
            r = table.row_values(n-1)
            return r
        except IOError:
            return "Excel文件打开失败"

if __name__ == '__main__':
    e = excel_data()
    print(e.sheet1(1,1))

