import os
from lib.operate_excel_data import OperateExcel
from utils.settings import CASES_PATH,BASE_PATH,DATA_PATH


def build_case():
    """根据yaml文件生成用例
    file_path_list: 所有文件的路径
    data_list:文件路径列表
    """
    file_path_list = [os.path.join(filepath, f) for filepath, dir, files in os.walk(DATA_PATH) for f in files]
    case_list = []
    for path in file_path_list:
        filepath = os.path.dirname(path)   # 返回文件路径
        file = os.path.basename(path)  # 返回文件名
        cases_path = path.replace(BASE_PATH,"")
        if file.endswith('.xlsx'):
            sheet_list = OperateExcel(cases_path).get_excel_sheet()
            for sheet in sheet_list:
                class_name = "Test_" + sheet
            # 打开base_case.txt文件，并命名为data_fil
                with open(os.path.join(CASES_PATH, 'Base_case.text'), 'r', encoding='utf-8') as data_file:
                    py_content = data_file.read() % {
                        'case_path': cases_path,
                        'file_name': file,
                        'sheet_name': sheet,
                        'class_name': class_name,
                    }
                    py_file_name = class_name.lower() + '.py'
                    case_list.append(py_file_name)
                    create_case_path = filepath.replace("data", "case", 1)
                    if os.path.exists(create_case_path):
                        pass
                    else:
                        os.mkdir(create_case_path)
                with open(os.path.join(create_case_path, py_file_name), 'w', encoding='utf-8') as py_file:
                    py_file.write(py_content)
    return case_list



