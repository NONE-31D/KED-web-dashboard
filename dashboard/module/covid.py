import json


def showCovid(period):
    file_name = "/home/none-31d/KED_visualization/KED_web_project/static/data/covid19.json"

    with open(file_name, 'r') as f:
        json_data = json.load(f)

    covid_json_data = dict()

    createDt = []
    natDefCnt= []
    natDeathCnt = []
    natDeathRate = []

    for idx, data in enumerate(json_data):
        if idx == period:
            break
        # createDt : 날짜,  natDefCnt : 일일확진자수, natDeathCnt : 일일사망자수, natDeathRate : 사망율
        createDt.append(data['createDt'][:10])
        natDefCnt.append(data['natDefCnt'])

        natDeathCnt.append(data['natDeathCnt'])
        natDeathRate.append(round(float(data['natDeathRate']), 2))

    covid_json_data['createDt'] = createDt
    covid_json_data['natDefCnt'] = natDefCnt
    covid_json_data['natDeathCnt'] = natDeathCnt
    covid_json_data['natDeathRate'] = natDeathRate
    covid_json_data['today_natDefCnt'] = natDefCnt[0]
    covid_json_data['today_natDeathCnt'] = natDeathCnt[0]
    covid_json_data['change_value'] = natDefCnt[0] -natDefCnt[1]

    return covid_json_data