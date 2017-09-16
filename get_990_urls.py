import requests
import json
import csv
import pandas 

einsList = pandas.read_csv('data/incomplete_ein_list.csv');

einsList = einsList[pandas.notnull(einsList['ein'])]
einsList['url'] = ""
einsList['return_type'] = ""

for index, row in einsList.iterrows():
    ein =  int(row[1])
    print "getting url for " + str(ein)
    try:
        r = requests.get('http://irs-xml-search.herokuapp.com/search?ein=' + str(ein))
        rjson = json.loads(r.text)
        einsList.loc[index, 'url']  = rjson[0]['url']
        einsList.loc[index, 'return_type']  = rjson[0]['RETURN_TYPE']
    except:
        print "Error grabbing " + str(ein)


einsList = einsList[pandas.notnull(einsList['url'])]
einsList = einsList[pandas.notnull(einsList['return_type'])]

einsList.to_csv('data/eins_url.csv')
