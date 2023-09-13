import requests
import json
import pandas as pd
import math

from datetime import datetime

def data_processing(data, year, code):
    if data[year][code]['status'] == '000': 
        data_df = data[year][code]['list']
        df = pd.DataFrame(data_df)
        df.drop(['rcept_no', 'reprt_code', 'fs_div', 'fs_nm', 'sj_div', 'ord', 'currency'], axis=1,inplace=True)

        df['thstrm_amount'] = pd.to_numeric(df['thstrm_amount'].str.replace(',', ''), errors='coerce')

        df.insert(8, '월평균(백만원)', df['thstrm_amount'] // (12 if code == '11011' else 6 if code == '11012' else 3))
        df['월평균(백만원)'] = df['월평균(백만원)'] // (1000000)
        df['thstrm_amount'] = df['thstrm_amount'].apply(lambda x: "{:,}".format(x))
        df['월평균(백만원)'] = df['월평균(백만원)'].apply(lambda x: "{:,}".format(x))

        if df.shape[1] == 15:
            df.columns = ["사업 연도", "회사코드", "종목코드", "재무제표명", "계정명", "당기명", "당기일자", "당기금액", "월평균(백만원)","전기명", "전기일자", "전기금액", "전전기명", "전전기일자", "전전기금액"]
            df.drop(["전전기명", "전전기일자", "전전기금액"], inplace=True, axis=1)
        else:
            df.columns = ["사업 연도", "회사코드", "종목코드", "재무제표명", "계정명", "당기명", "당기일자", "당기금액", "월평균(백만원)","전기명", "전기일자", "전기금액", "당기누적금액", "전기누적금액"]
        return df
    else:
        empty_df = {}
        df = pd.DataFrame(empty_df)
        return df


def start_multipleMajorAccounts(corp_code):
    total_list = []
    batch_size = 100

    for i in range(0, len(corp_code), batch_size):
        batch_100 = corp_code[i:i+batch_size]
        total_list.append(batch_100)

    count = math.ceil(len(total_list) / 100)

    start_num = 1

    reprt_code = ["11011", "11012", "11013", "11014"] # 보고서 전부 불러오기
    years = ["2022", "2023"] # 2022, 2023 연도 데이터 

    result_data = {}  
    KEY = "210d7f88b11afefe6715c028448edf2852080412"
    mu_url = "https://opendart.fss.or.kr/api/fnlttMultiAcnt.json" # API url

    for i in range(count):
        for re_i in years:
            for re in reprt_code:
                params = {
                    "crtfc_key": KEY,
                    "corp_code": total_list[i],
                    "bsns_year": re_i,
                    "reprt_code": re
                }

                response = requests.get(mu_url, params=params)

                if response.status_code == 200:
                    try:
                        data = response.json()
                        result_data.setdefault(re_i, {})[re] = data
                    except json.JSONDecodeError as e:
                        print("JSON 디코딩 오류:", e)
                else:
                    print("API 요청에 실패하였습니다. 상태 코드:", response.status_code)

        dataframes = {}

        for year in years:
            for code in reprt_code:
                df = data_processing(result_data, year, code)
                if not df.empty:
                    dataframes[f'df_{year}_{code}'] = df

                    
        combined_dfs = [df for df in dataframes.values()]
                    
        if combined_dfs:
            all_combined_df = pd.concat(combined_dfs, join='outer', ignore_index=True)
            all_combined_df.reset_index(drop=True, inplace=True)
        else:
            all_combined_df = pd.DataFrame()

        print("출력 number : ",start_num)
        now = datetime.now().strftime("%Y%m/%d_%H:%M:%S")
        all_combined_df.to_excel(f'다중회사_주요계정_{start_num}_{now}.xlsx', index=False)
        start_num += 1
        
    return 1
