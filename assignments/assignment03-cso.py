import requests
#take relevant table id from cso - https://data.cso.ie/table/FIQ02
cso_table_id = 'FIQ02'
restApi_url = f'https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/{cso_table_id}/JSON-stat/2.0/en'

cso_response = requests.get(restApi_url)
if cso_response.status_code == 200:
    with open('cso.json', 'w') as file:
        file.write(cso_response.text)
else:
    print(f'Unable to fetch details from CSO: {cso_response.status_code}')