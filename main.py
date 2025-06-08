from curl_cffi import requests

url = "https://multichain-api.birdeye.so/solana/trader_token?sort_by=trade&sort_type=desc&offset=0&limit=10&type=1D&tokenAddress=A7uv3n1By5UNEa8UJqeCjGyLqHkMnkS1NP6K67VZBqd3&include_bot=true"

payload = {}
headers = {
  'accept': 'application/json, text/plain, */*',
  'accept-language': 'en-US,en;q=0.9',
  'agent-id': '893fe12f-ef4f-4c32-9514-36a3d0471748',
  'dnt': '1',
  'origin': 'https://birdeye.so',
  'priority': 'u=1, i',
  'referer': 'https://birdeye.so/',
  'sec-ch-ua': '"Not?A_Brand";v="99", "Chromium";v="130"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-site',
  'token': 'undefined',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
