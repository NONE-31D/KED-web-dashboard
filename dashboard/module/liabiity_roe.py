import json, math

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

column_dir = {
    'ROE':0, 
    '부채비율':1, 
    '매출액증가율':2, 
    '총자산회전율':3
}

size_dir = {
    "대기업" : "big",
    "중기업" : "middle",
    "소기업" : "small"
}

sector_list = ['건설업', '공공행정, 국방 및 사회보장 행정', '광업', '교육 서비스업', '금융 및 보험업', '농업, 임업 및 어업', '도매 및 소매업', '보건업 및 사회복지 서비스업', '부동산업', '사업시설 관리, 사업 지원 및 임대 서비스업', '수도, 하수 및 폐기물 처리, 원료 재생업', '숙박 및 음식점업', '예술, 스포츠 및 여가관련 서비스업', '운수 및 창고업', '전기, 가스, 증기 및 공기조절 공급업', '전문, 과학 및 기술 서비스업', '정보통신업', '제조업', '협회 및 단체, 수리 및 기타 개인 서비스업']

def showLiabilityAndROE(year, locale, size):
    dirname = "/home/none-31d/KED_visualization/KED_web_project/static/data/finance/"

    # get middle data
    with open(dirname+f"finance_{locale_dir[locale]}_{size_dir[size]}.json", 'r', encoding='euc-kr') as f:
        json_data = json.load(f)
    
    # sector_list = list(json_data.keys())
    roe_list = []
    liability_list = []

    liability_roe_data = dict()
    liability_roe_data['data'] = []
    liability_roe_data['label'] = []


    roe_liable_dict = dict()
    liable_sector_dict = dict()

    nan_cnt = 0
    nan_cnt2 = 0

    for k, v in json_data.items():
        if k not in sector_list:
            continue
        roe = str(v[2017-int(year)][0])
        liable = str(v[2017-int(year)][1])
        if math.isnan(float(roe)):
            roe = "NaN"+str(nan_cnt)
            nan_cnt += 1
        if math.isnan(float(liable)):
            liable = "NaN"+str(nan_cnt2)
            nan_cnt2 += 1
        roe_liable_dict[roe] = liable
        liable_sector_dict[liable] = k
        roe_list.append(roe)
        liability_list.append(liable)
    

    roe_list.sort()
    liability_list.sort()

    for r in roe_list:
        data_row = {'name':r, 'data':[-1 for _ in range(19)]}

        l = roe_liable_dict[r]
        idx = liability_list.index(l)
        data_row['data'][idx] = idx#liable_sector_dict[l]

        liability_roe_data['data'].append(data_row)
    
    liability_roe_data['label'] = liability_list

    return liability_roe_data




# showLiabilityAndROE(2017, "경기", "중기업")
