import json
import pandas as pd
import requests
import xmltodict
import os, os.path
import sys
import numpy as np

# Taken from https://stackoverflow.com/a/600612/119527
def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc: # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else: raise

def safe_open_w(path):
    ''' Open "path" for writing, creating any parent directories as needed.
    '''
    mkdir_p(os.path.dirname(path))
    return open(path, 'w')

cpc_df = pd.read_excel('CPC Location Data.xlsx', sheetname='CareNet Matched EINs')

print(sys.argv)
years = [sys.argv[1]]

for year in years:
    with open('index_'+str(year)+'.json') as data_file:
        data = json.load(data_file)
    json_columns = ['EIN', 'DLN', 'OrganizationName', 'ObjectId']
    index_df = pd.DataFrame(data = {'EIN': [row['EIN'] for row in data['Filings' + str(year)]],
                                'DLN': [row['DLN'] for row in data['Filings' + str(year)]],
                                'OrganizationName': [row['OrganizationName'] for row in data['Filings' + str(year)]],
                                'ObjectId': [row['ObjectId'] for row in data['Filings'+ str(year)]]})

    index_df.set_index('EIN', inplace=True)

    cpc_len = len(cpc_df)
    for i, row in cpc_df.iterrows():
        try:
            ein = str(int(row['Scraped EIN']))
            oid = index_df.loc[ein]['ObjectId']
            r = requests.get("https://s3.amazonaws.com/irs-form-990/"+oid+"_public.xml")
            data = xmltodict.parse(r.content)
            with safe_open_w("990/" + ein + "/"+"990_"+str(year)+".json") as f:
                f.write(json.dumps(data))
            print(str(year) + " - " + str(i) + "/" + str(cpc_len))
        except:
            pass
    break
