import requests
try:
    first_url='http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsList'
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
    }
    ids=[]
    for page in range(1,20):
        data1={
        'on':'true',
        'page': str(page),
        'pageSize':'15',
        'productName':'',
        'conditionType':'1',
        'applyname':'',
        'applysn':'',
        }
        r= requests.post(first_url,headers=headers,data=data1)
        r_json=r.json()
     #   print(r_json)
        for dic in r_json['list']:
            ids.append(dic['ID'])
        # print(ids)
    detail_url='http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsById'
    for _id in ids:
        data2={
            'id':_id,
        }
        response= requests.post(detail_url, headers = headers, data = data2)
        response_json=response.json()
        response_text=response.text
        with open('化妆品信息.text','a') as f:
            f.write(response_text)
            f.close()
       # print(response_json)
    print('over!!!')



except Exception as err:
    print(err)