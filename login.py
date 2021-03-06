import requests
import re
from urllib import parse

def status(url):
	global flag
	try:
		html = requests.get(url, timeout = 1).text
	except requests.exceptions.Timeout:
		print("You have been connected")
	else:
		return html


resp = status('http://123.123.123.123')
referer = ''
qs = ''
p1 = re.compile("='(.*?)'</script>")
p2 = re.compile("jsp\?(.*?)'</script>")

if resp != None:
	referer = re.findall(p1, resp)
	qs = re.findall(p2,resp)

qstr = "".join(qs)
qstr = parse.quote(qstr)
referer2 = "".join(referer)

header = {
	'Host': '202.118.253.94:8080',
	'Connection': 'keep-alive',
	'Content-Length': '649',
	'Origin': 'http://202.118.253.94:8080',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
	'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'Accept': '*/*',
	'Referer': referer2,
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'zh-CN,zh;q=0.9'
}
# ID and password
postdata = {
	'userId':'',
	'password':'',
	'service':'',
	'queryString': qstr,
	'operatorPwd':'',
	'operatorUserId':'',
	'validcode':'',
	'passwordEncrypt':'false'
}

r = requests.post('http://202.118.253.94:8080/eportal/InterFace.do?method=login', data = postdata, headers = header)

resp2 = r.text

if 'success' in resp2:
	print("Connect successfully")
else:
	print("Connect failed")
