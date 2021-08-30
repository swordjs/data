import PyPDF4

pdfFile = open('javadoc.pdf', 'rb')

pdfReader = PyPDF4.pdf.PdfFileReader(pdfFile)

o = pdfReader.getOutlines()


# 递归根据item获取title
def loop_get_title(o):
    for item in o:
        # 判断是否是对象
        if isinstance(item, dict):
            print(item.get('/Title'))
            continue
        else:
            # 循环
            loop_get_title(item)

loop_get_title(o)

pdfFile.close()
