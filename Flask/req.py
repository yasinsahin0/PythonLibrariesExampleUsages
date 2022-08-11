import requests

url = 'http://127.0.0.1:5001'

def home_req():
    req_url = url + "/"
    response = requests.post(req_url)
    print(response.text)

def var_resp():
    req_url = url + "/NameSurname"
    payload = {'name': 'yasin',
               'surname': 'sahin'}
    response = requests.request("POST", req_url, data=payload)
    print(response.text)


if __name__ == "__main__":
    home_req()
    var_resp()
