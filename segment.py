# step1:擷取tag date cost event
def get_tag_date_cost_event(text: str):
    segment_1 = text.split("]")
    segment_2 = segment_1[0].split("[")
    tag = segment_2[1]
    segment_3 = segment_1[1].split(" $")
    date = segment_3[0]
    segment_4 = segment_3[1].split("-")
    cost = segment_4[0]
    event = ""
    # 若表單裡沒有事件回傳會出錯，故提供一個空字串供放置
    if len(segment_4) > 1:
        event = segment_4[1]
    # 第四刀切下去用len判斷後面還有字符否,如果>1代表該資料有備註
    return tag, date, cost, event


# step2: loading all data
f = open("./CostData.txt", encoding="utf8")
file_data_list = f.readlines()

dict_list = []
for d in file_data_list:
    if d != "\n":
        d = d.strip()
        tag, date, cost, event = get_tag_date_cost_event(d)
        dict_list.append({"tag": tag, "date": date, "cost": cost, "event": event})

max_cost = 0
# 用一個0起始一筆筆比較,假設有更高值就更迭上去
max_tag = ""
max_date = ""
max_event = ""
for d in dict_list:
    if d["event"] == "早餐":
        if int(d["cost"]) > max_cost:
            max_cost = int(d["cost"])
            # d[cost]提取出都是str故需轉型int
            max_tag = d["tag"]
            max_date = d["date"]
            max_event = d["event"]
print(f"[{max_tag}]{max_date} ${max_cost}-{max_event}")
# CMD + OP + L 自動縮排整齊
