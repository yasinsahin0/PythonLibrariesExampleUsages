import requests

url = 'http://127.0.0.1:5001/'
myobj = {'somekey': 'somevalue'}

x = requests.post(url, json = myobj)

print(x.text)

# Yönlendirme aktif vey pasif, True - False
a = requests.post(url, data = myobj, allow_redirects=True)
print(a.text)