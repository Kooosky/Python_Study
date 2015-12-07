import requests

def get_usrdat():
    r=requests.get('https://api.github.com/user',auth=('user','password'))
    return r.json()['created_at']