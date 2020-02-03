import requests

res = requests.get('https://northstar.changtu.com/ippool/random').json()
ip = res.get('data').get('ip')
port = res.get('data').get('port')
print(ip + port)