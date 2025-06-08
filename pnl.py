from curl_cffi import requests

url = "https://multichain-api.birdeye.so/solana/trader_profile_v2/leaderboard/gnl?type=gainers&time=7D"
url_top_profiles = "https://multichain-api.birdeye.so/solana/trader_profile_v2/social/top_profiles"


payload = {}
headers = {
  'Host': 'multichain-api.birdeye.so',
  'Accept': '*/*',
  'Access-Control-Request-Method': 'GET',
  'Access-Control-Request-Headers': 'agent-id,cf-be,token',
  'Origin': 'https://birdeye.so',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.71 Safari/537.36',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-site',
  'Sec-Fetch-Dest': 'empty',
  'Referer': 'https://birdeye.so/',
  'Accept-Encoding': 'gzip, deflate, br',
  'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
  'Priority': 'u=1, i'
}

response = requests.request("GET", url, headers=headers, data=payload)

# print(response.text)
data = response.json()
gnl = data['data']['items']
for i in range(len(gnl)):
    pnl7d = gnl[i]['pnl7D']
    addy = gnl[i]['address']
    print(f'profit: {pnl7d} > {addy}' )
