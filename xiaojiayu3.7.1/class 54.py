import urllib.request
import urllib.parse
import json


content = input('请输入需要翻译的内容：')
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
data = {}
data['i'] = content
data['from'] = 'AUTO'
data['to'] = 'AUTO'
data['smartresult'] = 'dict'
data['client'] =  'fanyideskweb'
data['salt'] = '1542164931694'
data['sign'] = 'ca2647671274cf2d655b14b2b3136f6e'
data['doctype'] = 'json'
data['version'] = '2.1'
data['keyfrom'] = 'fanyi.web'
data['action'] = 'FY_BY_CLICKBUTTION'
data['typoResult'] = 'false'
data = urllib.parse.urlencode(data).encode('utf-8')

response = urllib.request.urlopen(url,data)
html = response.read().decode('utf-8')

#print(html)

target = json.loads(html)
print(target['translateResult'][0][0]['tgt'])

