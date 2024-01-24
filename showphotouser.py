import requests

chat_id = "6581896306"
urlp = "https://t.me/elhyba"
url = f"https://api.telegram.org/bot6635986173:AAH0Veius7B7-o6m4_lxWiMeW1ahqZqZ-o4/getChat?chat_id={chat_id}"

req = requests.get(url).json()
print(req)
