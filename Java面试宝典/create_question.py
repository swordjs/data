import json

# 获取根目录的filename_save.json
title_list = open("./filename_save.json", 'rb')
title_list_content = title_list.read()

title_dict = json.loads(title_list_content)

# 构建标题和数据库的标签id关联字典
title_tag_map = {
    "一．Java基础": "600cf8b6b2f9d8000147c47b",
    "二．Java Web": "612f7c0f7c33d500014dc304",
    "三．数据库": "612f7cdc9b33ed00017f4363",
    "四. Mybatis框架": "612f7d18ea720b00017d912c",
    "五．Spring框架": "612f7d3dea720b00017d9230",
    "六．SpringMVC框架": "612f7d540d30690001670a12",
    "八.SpringBoot框架": "612f7d9b2a138e00018f2273",
    "九. SpringCloud框架": "612f7dc3ea720b00017d958b",
    "默认精选": "612f7e67e55c2c0001485dd3"
}

# 发布者id
publish_user_id = "605df8968e68f00001e63f0b"

# 专区id，需要用$id包裹一下
area_id = {"$oid": "5fdf56a3e2c1ee0001a52e49"}


# 循环title_dict
for key in title_dict:
    # 判断key是否在字典中，如果在就获取它的tag，不在就使用默认的
    tag_id = ""
    if key in title_tag_map:
        # 获取tagid
        tag_id = title_tag_map[key]
    else:
        tag_id = title_tag_map["默认精选"]

    # 循环题目
    question_list = list(title_dict[key])
    for title in question_list:
        question_content = {
            "title": title,
            "areaID": area_id,
            "publishUserID": publish_user_id,
            "content": "",
            "questionExplanation": [],
            "tagID": [{"$oid": tag_id}],
            "state": "pass",
            "createDate": "2021-09-01T14:02:44.296Z",
            "updateDate": "2021-09-01T14:02:44.296Z",
            "deleteDate": ""
        }
        with open('question_content.json', 'a+') as f:
            json_str = json.dumps(question_content, ensure_ascii=False)
            f.write(json_str)
            f.write('\n')