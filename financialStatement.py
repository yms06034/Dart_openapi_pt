import requests
import json
import pandas as pd
from datetime import datetime

def data_process(data, year, code, i):
    data_df = data[year][f'{code}'][f'{i}']['list']
    df = pd.DataFrame(data_df)

    df.drop(['rcept_no', 'reprt_code', 'stock_code','fs_div', 'fs_nm', 'sj_div', 'ord', 'currency'], axis=1,inplace=True)
    df['thstrm_amount'] = pd.to_numeric(df['thstrm_amount'].str.replace(',', ''), errors='coerce')

    df.insert(7, '월평균(백만원)', df['thstrm_amount'] // 12)
    df['월평균(백만원)'] = df['월평균(백만원)'] // (1000000)
    df['thstrm_amount'] = df['thstrm_amount'].apply(lambda x: "{:,}".format(x))
    df['월평균(백만원)'] = df['월평균(백만원)'].apply(lambda x: "{:,}".format(x))

    if df.shape[1] == 14:
        df.columns = ["사업 연도", "회사코드", "재무제표명", "계정명", "당기명", "당기일자", "당기금액", "월평균(백만원)","전기명", "전기일자", "전기금액", "전전기명", "전전기일자", "전전기금액"]
        df.drop(["전전기명", "전전기일자", "전전기금액"], inplace=True, axis=1)
    else:
        df.columns = ["사업 연도", "회사코드", "재무제표명", "계정명", "당기명", "당기일자", "당기금액", "월평균(백만원)","전기명", "전기일자", "전기금액", "당기누적금액", "전기누적금액"]
    return df

def start_financialStatement(corp_code):
    reprt_codes = ["11011", "11012", "11013", "11014"]
    years = ["2022", "2023"] 
    statements_result_data = {}  

    mu_url = "https://opendart.fss.or.kr/api/fnlttMultiAcnt.json"
    KEY = "210d7f88b11afefe6715c028448edf2852080412"

    for year in years:
        print("데이터를 가져오고 있습니다.")
        year_data = {}

        for code in reprt_codes:
            for cc in corp_code:
                params = {
                    "crtfc_key": KEY,
                    "corp_code": cc,
                    "bsns_year": year,
                    "reprt_code": code
                }

                response = requests.get(mu_url, params=params)

                if response.status_code == 200:
                    try:
                        data = response.json()
                        year_data.setdefault(code, {})[str(cc)] = data
                    except json.JSONDecodeError as e:
                        print("JSON 디코딩 오류:", e)
                else:
                    print("API 요청에 실패하였습니다. 상태 코드:", response.status_code)

        statements_result_data[year] = year_data
                
    dataframes = {}

    print("데이터를 가져와 정리하고 있습니다.")

    if (statements_result_data['2022'] or statements_result_data['2023']):
        for year in years:
            for idx, code in enumerate(reprt_codes):
                for i in statements_result_data[year][f'{code}']:
                    if (statements_result_data[year][f'{code}'][f'{i}']['status'] == '000'):
        #                 print(statements_result_data[year][f'{code}'][f'{i}']['list'])
                        df = data_process(statements_result_data, year, code, i)
                        print(df)
                        dataframes[f'df_{year}_{code}_{i}'] = df

        combined_dfs = [df for df in dataframes.values()]

        if combined_dfs:
            all_combined_df = pd.concat(combined_dfs, join='outer', ignore_index=True)
            all_combined_df.reset_index(drop=True, inplace=True)
        else:
            all_combined_df = pd.DataFrame()
            
        dt = datetime.now().strftime("%Y-%m-%d_%H%M")
        

        all_combined_df.to_excel(f'단일회사_전체_재무제표_{dt}.xlsx', index=False)
        return 1
    else:
        return 0