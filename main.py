# import urllib.request
import requests
#
# opener = urllib.request.build_opener()
#
# responce = opener.open("https://httpbin.org/get")
#
# print(responce.read())




# res = requests.post("https://httpbin.org/get", data="Test data hello world", headers={"h1": "My title"})
#
# response = requests.get("https://httpbin.org/get")
# print(response.text)

response = requests.get("https://coinmarketcap.com/")
response_text = response.text

coin_list = []

responce_parse = response_text.split("<span>")
for parse_elem1 in responce_parse:
    if parse_elem1.startswith("$"):
        for parse_elem2 in parse_elem1.split("</span>"):
            if parse_elem2.startswith("$") and parse_elem2[1].isdigit():
                coin_list.append(parse_elem2)

btc = coin_list[0]
print('BTC =', btc)