import PyPDF4
import json

pdfFile = open('javadoc.pdf', 'rb')

pdfReader = PyPDF4.pdf.PdfFileReader(pdfFile)

o = pdfReader.getOutlines()

# 判断是否是汉字


def is_chinese(uchar):
    if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
        return True
    else:
        return False


menu_list = dict({})
# 递归根据item获取title


def loop_get_title(o):
    for item in o:
        # 判断是否是对象
        if isinstance(item, dict):
            # 获取title
            title = item.get('/Title')
            # 判断title的第一个是否是汉字，一，二，如果是就是一级标题，给字典设置一个默认空数组
            if is_chinese(title[0]) & (title not in menu_list):
                menu_list[title] = []
            # 获取对象的最后一个key（就是此item的父级）
            # print(menu_list.keys())
            menu_list_keys = list(menu_list.keys())
            last_key = menu_list_keys[menu_list_keys.__len__() - 1]
            menu_list[last_key].append(item.get("/Title"))
            continue
        else:
            # 循环
            loop_get_title(item)

# 首次调用循环方法
loop_get_title(o)
pdfFile.close()

print("目录:", menu_list)

# pdf的目录有很多不规整的地方，部分地方开发者手工处理了，存在此文件夹下的filename_save文件中，如果你想要重新生成，就调用下面这个生成函数
def create_title_json():
    with open('filename.json', 'w', encoding="utf-8") as f:
        f.write(json.dumps(menu_list, ensure_ascii=False))
        f.close()

