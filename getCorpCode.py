import requests
import io
import zipfile
import xmltodict
import pandas as pd

def get_corpcode_start():
    KEY = "210d7f88b11afefe6715c028448edf2852080412"
    url = "https://opendart.fss.or.kr/api/corpCode.xml"

    params = {
        "crtfc_key": KEY
    }

    resp = requests.get(url, params=params)

    f = io.BytesIO(resp.content)
    zfile = zipfile.ZipFile(f)

    xml = zfile.read("CORPCODE.xml").decode("utf-8")
    dict_data = xmltodict.parse(xml)

    data = dict_data['result']['list']
    corp_code_df = pd.DataFrame(data)
    corp_code_df.drop(columns=['stock_code', 'modify_date'], inplace=True)

    corp_code_df.to_excel("회사코드.xlsx", index=False)
    
    return 1