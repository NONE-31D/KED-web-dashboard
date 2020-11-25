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

def showPreAlert(year, locale, size, sector):
    dirname = "/home/none-31d/KED_visualization/KED_web_project/static/data/pre_alert/"

    # get middle data
    with open(dirname+f"pre_alert_{locale_dir[locale]}_{size_dir[size]}.json", 'r', encoding='euc-kr') as f:
        json_data = json.load(f)

    alert_json_data = dict()
    alert_json_data['label'] = ['정상', '관심', '관찰1', '관찰2', '관찰3', '휴업', '부도', '폐업']


    alert_json_data['data'] = [0 for _ in range(8)]

    # cut by year

    if int(year) == 2017:
        json_data = json_data[sector][:12]
    elif int(year) == 2016:
        json_data = json_data[sector][12:24]
    elif int(year) == 2015:
        json_data = json_data[sector][24:]


    for d in json_data:
        for i in range(8):
            alert_json_data['data'][i] += d[i]

    return alert_json_data

# showPreAlert(2017, "경기", "중기업", "건설업")