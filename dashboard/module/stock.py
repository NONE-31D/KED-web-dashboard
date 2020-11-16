import FinanceDataReader as fdr
import datetime, json

from datetime import datetime
from datetime import timedelta

def showStock(keyword, period):
    stock_list = {'KOSPI':'KS11', 'DJI':'DJI', 'JP225':'JP225', \
              'STOXX50':'STOXX50', 'HSI':'HSI', 'CSI300':'CSI300', \
              'UK100':'UK100', 'DE30':'DE30', 'FCHI':'FCHI'}
    file_name = f"/home/none-31d/KED_visualization/KED_web_project/static/data/stock/{stock_list[keyword]}_{period}.json"

    with open(file_name, 'r') as f:
        json_data = json.load(f)

    return json.dumps(json_data)


    # print(keyword, stock_list[keyword])
    # df = fdr.DataReader(stock_list[keyword], (datetime.today()-timedelta(days=period)).strftime('%Y-%m-%d'))
    # df = df.drop(['Open', 'High', 'Low', 'Volume'], axis=1)
    # # df_js = df.to_json()
    # # print(df_js) # JSON Data, 맨 뒤에 데이터가 최신꺼임

    # date_index = [d.to_pydatetime().strftime("%Y-%m-%d") for d in df.index.tolist()]
    # data = df['Close'].tolist()
    # data_change = df['Change'].tolist()
    # # print(data_changesss)
    # stock_json_data = dict()
    # stock_json_data['keyword'] = keyword
    # stock_json_data['date'] = date_index
    # stock_json_data['stock_data'] = data
    # stock_json_data['last_data'] = data[-1]

    # return stock_json_data

showStock('KOSPI', 180)