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

def showEmployment(locale, year, size):
    dirname = "/home/none-31d/KED_visualization/KED_web_project/static/data/employment/"

    # get middle data
    with open(dirname+f"employment_{locale_dir[locale]}_{size_dir[size]}.json", 'r', encoding='euc-kr') as f:
        json_data = json.load(f)
    
    employment_json_data = dict()

    employment_json_data['label'] = list(json_data.keys())
    employment_json_data['label'][-2] = "제조업 (단위:3)"
    employment_json_data['new'] = [0 for _ in range(20)]
    employment_json_data['retiree'] = [0 for _ in range(20)]
    
    for idx, label in enumerate(employment_json_data['label']):
        if len(label) > 10:
            employment_json_data['label'][idx] = label[:10]+'...'


    for idx, values in enumerate(json_data.items()):
        i, v = values
        if int(year) == 2017:
            v = v[:12]
        elif int(year) == 2016:
            v = v[12:]
        for val in v:
            employment_json_data['new'][idx] += val[1] 
            employment_json_data['retiree'][idx] += val[2]
    
    employment_json_data['new'][-2] /= 3
    employment_json_data['retiree'][-2] /= 3

    for idx, newee in enumerate(employment_json_data['new']):
        employment_json_data['new'][idx] = int(newee)

    for idx, retiree in enumerate(employment_json_data['retiree']):
        employment_json_data['retiree'][idx] = int(retiree)

    return employment_json_data
    
# showEmployment("경기", 2017, "중기업")