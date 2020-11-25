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
    
size_dir = {
    "대기업" : "big",
    "중기업" : "middle",
    "소기업" : "small"
}


def showCorperation(year, sector, size):
    # 31 ulsan 49 jeju 48 south Gyeongsang 45 North Jeolla  44 South Chungcheong 47 North Gyeongsang
    # 46 South Jeolla 41 Gyeonggi 43 North Chungcheong 42 Gangwon 27 Daegu  11 Seoul  50 Sejong
    # 29 Gwangju  28 Incheon 30 Daejeon 26 Busan

    dirname = "/home/none-31d/KED_visualization/KED_web_project/static/data/corperation/"

    data1 = {
        "kr-42" : [],
        "kr-41" : [],
        "kr-48" : [],
        "kr-47" : [],
        "kr-29" : [],
        "kr-27" : [],
        "kr-30" : [],
        "kr-26" : [],
        "kr-11" : [],
        "kr-50" : [],
        "kr-31" : [],
        "kr-28" : [],
        "kr-46" : [],
        "kr-45" : [],
        "kr-49" : [],
        "kr-44" : [],
        "kr-43" : []
    }

    corperation_json_data = dict()

    locale_list = list(locale_dir.keys())

    for idx, items in enumerate(data1.items()):
        k, _ = items
        with open(dirname+f"corperation_{locale_dir[locale_list[idx]]}_{size_dir[size]}.json", 'r', encoding='euc-kr') as f:
            json_data = json.load(f)
        
        if sector not in json_data.keys():
            corperation_json_data[k] = 0
            continue

        if int(year) == 2017:
            json_data = json_data[sector][:12]
        elif int(year) == 2016:
            json_data = json_data[sector][12:24]
        elif int(year) == 2015:
            json_data = json_data[sector][24:36]
        elif int(year) == 2014:
            json_data = json_data[sector][36:48]
        elif int(year) == 2013:
            json_data = json_data[sector][48:]
            
        total = 0
        for val in json_data:
            total += val
        corperation_json_data[k] = total

    return corperation_json_data

# showCorperation(2017, "건설업", "중기업")



