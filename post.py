from curl_cffi import requests

def post_request(repetitions):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'agent-id': '893fe12f-ef4f-4c32-9514-36a3d0471748',
        'cf-be': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3Mjc4NTQ0NjcsImV4cCI6MTcyNzg1NDc2N30.zrgztgSR-yFGd9zO2_gUIl0jcOfnLYr33IxeoeR5hmg',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://birdeye.so',
        'page': 'find_trades',
        'priority': 'u=1, i',
        'referer': 'https://birdeye.so/',
        'sec-ch-ua': '"Not?A_Brand";v="99", "Chromium";v="130"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    }

    json_data = {
        'offset': 0,
        'limit': 20,
        'export': False,
        'page': 'find_trades',
    }

    for _ in range(repetitions):
        response = requests.post('https://multichain-api.birdeye.so/solana/amm/txs/token', headers=headers, json=json_data)
        print(response.status_code)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"offset":0,"limit":20,"export":false,"page":"find_trades"}'
#response = requests.post('https://multichain-api.birdeye.so/solana/amm/txs/token', headers=headers, data=data)

post_request(10)