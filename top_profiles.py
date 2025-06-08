from curl_cffi import requests

url = "https://multichain-api.birdeye.so/solana/trader_profile_v2/social/top_profiles"


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
data = data['data']
# print(data['data'])
# whale = data['data']['topWhale']
for i in range(len(data['topAirdrop'])):
    # print(data['topAirdrop'][i])
    wallet = data['topAirdrop'][i]['wallet']
    vol = data['topAirdrop'][i]['todayVolume']
    print(f'Airdrop wallet: {wallet} > {vol}')

for i in range(len(data['topWhale'])):
    # print(data['topWhale'][i])
    wallet = data['topWhale'][i]['wallet']
    vol = data['topWhale'][i]['todayVolume']
    print(f'Whale wallet: {wallet} > {vol}')