import requests
import json

register = 'https://cit-home1.herokuapp.com/api/register'
check = 'https://cit-home1.herokuapp.com/api/check_me'
text = json.dumps({'First name':'Eduard','Last name':'Smirnykh'})
head = {'content-type':'application/json'}

getch=requests.get(check)
print(getch.json())