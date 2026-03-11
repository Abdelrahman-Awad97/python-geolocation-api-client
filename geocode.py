import urllib.request, urllib.parse, urllib.error
import json, ssl

parms = {}

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

basic_domain = 'https://py4e-data.dr-chuck.net/opengeo?'

while True:
    # you can type this address: Gebäude 78 – Besucherempfang
    # or any suitable address you want
    address = input('Type the location here: ').strip()
    
    if len(address) < 1:
        print('wrong entry')
        quit()
    
    if address == 'done':
        print('Thank you for using our program')
        quit()
    
    parms['q'] = address
    url = basic_domain + urllib.parse.urlencode(parms)
    # print(f'API URL: {url}')

    fetch_data_b = urllib.request.urlopen(url, context=ctx)
    fetch_data_s = fetch_data_b.read().decode()

    
    try:
        fetch_data_d = json.loads(fetch_data_s)
    except:
        fetch_data_d = None

    # to see beautiful json
    # print(json.dumps(fetch_data_d, indent=4))

    if fetch_data_d == None or 'features' not in fetch_data_d:
        print('Error: Unable to retrieve data from API')
        quit()
    
    features_lst = fetch_data_d['features']
    if len(features_lst) < 1:
        print('object not found')
    
    # data extraction
    lon = features_lst[0]['properties']['lon']
    lat = features_lst[0]['properties']['lat']
    country = features_lst[0]['properties']['country']
    state = features_lst[0]['properties']['state']
    print(f"Longitude: {lon}\nlatitude {lat}")
    print(f'Location: {state}, {country}')