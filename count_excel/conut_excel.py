import xlrd


class CollectExcel:
    """
    file_name: 读取的excel名称
    sheet_name: 读取的excel的sheet栏[-
    """

    def read_task_file(self,task_file):
        file = xlrd.open_workbook(task_file)
        sheet_name = file.sheet_names()
        sheet = file.sheet_by_name(sheet_name[0])
        task_time = {}
        for i in range(1,sheet.nrows):
            status = sheet.cell(i,3).value
            if status == "已完成":
                task_time [sheet.cell(i,0).value]= sheet.cell(i,1).value
        return task_time

    def read_iteration_file(self,iteration_file):
        file = xlrd.open_workbook(iteration_file)
        sheet_name = file.sheet_names()
        sheet = file.sheet_by_name(sheet_name[0])
        all =[]
        for i in range(1,sheet.nrows):
            if "story" in  sheet.cell(i,0).value():
                story = {sheet.cell(i,0).value:{}}
                tester = {sheet.cell(i,0).value:sheet.cell(i,3)}
                pm = {sheet.cell(i,0).value:sheet.cell(i,4)}
                all.append(story)
            if "task" in sheet.cell(i,0):
                pass







if __name__ == "__main__":
    # print( CollectExcel().read_task_file("任务表.xls"))
    print(CollectExcel().read_iteration_file("需求表.xls"))