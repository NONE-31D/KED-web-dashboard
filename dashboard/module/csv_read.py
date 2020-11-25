import pandas as pd

keyword_dir = {
    "finance" : "주요 재무비율",
    "prealert" : "조기경보등급",
    "employment" : "종업원현황",
    "corperation" : "신설법인현황",
    "stoppage" : "휴업자 현황",
    "closing" : "폐업자 현황"
}

def readCSVData(keyword):
    dir_name = "/home/none-31d/KED_visualization/KED_web_project/static/csv/"
    data = pd.read_csv(f"{dir_name}{keyword}.csv", encoding='euc-kr')
    column_name = data.columns.tolist()
    total_len = len(data)
    csv_name = keyword_dir[keyword]
    csv_data =  data.values.tolist()

    data_dict = {
        "column_name" : column_name,
        "total_len" : total_len,
        "csv_name" : csv_name,
        "csv_data" : csv_data
    }

    return data_dict

# readCSVData("employment")