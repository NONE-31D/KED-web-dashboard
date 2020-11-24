import json

locale_dir = {
    "강원":1, 
    "경기":2,
    "경남":3, 
    "경북":4, 
    "광주":5, 
    "대구":6,
    "대전":7, 
    "부산":8, 
    "서울":9, 
    "세종":10, 
    "울산":11, 
    "인천":12, 
    "전남":13, 
    "전북":14,
    "제주":15, 
    "충남":16, 
    "충북":17}

def showFinance(locale, sector):
    dirname = "/home/none-31d/KED_visualization/KED_web_project/static/data/finance/"

    # get middle data
    with open(dirname+f"finance_{locale_dir[locale]}_middle.json", 'r', encoding='euc-kr') as f:
        mid_json_data = json.load(f)

    # get small data
    with open(dirname+f"finance_{locale_dir[locale]}_small.json", 'r', encoding='euc-kr') as f:
        small_json_data = json.load(f)

    finance_json_data = dict()

    finance_json_data['label'] = []
    finance_json_data['small'] = []
    finance_json_data['mid'] = []

    for i in range(3, 8):
        date_str = "201%d"%(i)
        finance_json_data['label'].append(date_str)
        

    for data_list in small_json_data[sector]:
        finance_json_data['small'].append(data_list[1])

    for data_list in mid_json_data[sector]:
        finance_json_data['mid'].append(data_list[1])

    return finance_json_data

showFinance("경기", "건설업")