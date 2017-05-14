import requests
from bs4 import BeautifulSoup
from random import randint
from linereader import dopen


def random_info(i):
	if i == 1:
		with dopen('random\\ten-nam.txt') as f_firstname:
			return f_firstname.getline(randint(1, f_firstname.count('\n')))
	if i == 2:
		with dopen('random\\ho.txt') as f_firstname:
			return f_firstname.getline(randint(1, f_firstname.count('\n')))

r = requests.get('https://mbasic.facebook.com/reg')
soup = BeautifulSoup(r.text, "html.parser")
f = open('C:/Users/Admin/Desktop/test.html', 'w', encoding='utf-8')

# value = soup.fillAll('input', attrs={'name': 'lsd'})[0].get_text()

lsd = soup.find("input", attrs={"name" : "lsd"})['value']
reg_instance = soup.find("input", attrs={"name" : "reg_instance"})['value']
reg_impression_id = soup.find("input", attrs={"name" : "reg_impression_id"})['value']

payload = {
		"lsd": lsd,
		"cpp": 2,
		"reg_instance": reg_instance,
		"submission_request": "true",
		"i": "",
		"helper": "",
		"reg_impression_id": reg_impression_id,
		"field_names%5B%5D": "firstname",
		"field_names%5B%5D": "reg_email__",
		"field_names%5B%5D": "se x",
		"field_names%5B%5D": "birthday_wrapper",
		"field_names%5B%5D" :"reg_passwd__",
		"lastname": random_info(1),
		"firstname": , 
		"reg_email__": ,
		"sex": ,
		"birthday_day": ,
		"birthday_month": ,
		"birthday_year": ,
		"reg_passwd__": ,
		"submit": ,
};

r = requests.post('https://mbasic.facebook.com/reg', payload)

f.write(r.text)
