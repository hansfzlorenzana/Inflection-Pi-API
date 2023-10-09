import json
from curl_cffi import requests
import re
from proxies import fetch_proxy
from time import sleep
from httpx import Client


class Pi:

  def __init__(self, cookie: str, proxy: bool=False):

    if proxy == True:
        proxies = fetch_proxy()
        for p in range(len(proxies)):
            try:
                self.client = Client(timeout=180, proxies= {"http://": f"{proxies[p]}"})
                print(f"Connection established with {proxies[p]}")
                break
            except:
                print(f"Connection failed with {proxies[p]}. Trying {p+1}/{len(proxies)} ...")
                sleep(1)
    else:
        self.client = Client(timeout=180)
    self.cookie = cookie

  def send_message(self, prompt):

    payload = json.dumps({"text": prompt})

    url = "https://pi.ai/api/chat"

    headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0',
            'Accept-Language': 'en-US,en;q=0.7',
            'Referer': 'https://pi.ai/api/chat',
            'Content-Type': 'application/json',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'Connection': 'keep-alive',
            'Cookie': f'{self.cookie}'
    }

    response = requests.post( url, headers=headers, data=payload,impersonate="chrome110",timeout=500)
    decoded_data = response.content.decode("utf-8")

    decoded_data = re.sub('\n+', '\n', decoded_data).strip()
    data_strings = decoded_data.split('\n')
    completions = []

    for data_string in data_strings:
        # Check if the string starts with 'data:'
        if data_string.startswith('data:'):
            # Extract the JSON data part
            json_str = data_string[6:].strip()
            try:
                data = json.loads(json_str)
                if 'text' in data:
                    completions.append(data['text'])
            except json.JSONDecodeError:
                # Handle invalid JSON here (skip or log the error)
                pass

    answer = ''.join(completions)

    return answer