import requests
from bs4 import BeautifulSoup
from random import randint
from linereader import dopen
import re
import time

proxies = {
		'https': 'http://127.0.0.1:1080'
}
cookies_10minutemails = ''

def random_info(i):
	if i == 0:
		f_firstname = dopen('random\\ho.txt')
		return f_firstname.getline(randint(1, f_firstname.count('\n')))
	elif i == 1:
		f_lastname = dopen('random\\ten-nam.txt')
		return f_lastname.getline(randint(1, f_lastname.count('\n')))
	elif i == 2:
		f_lastname = dopen('random\\ten-nu.txt')
		return f_lastname.getline(randint(1, f_lastname.count('\n')))
	elif i == 3:
		return randint(1, 28)
	elif i == 4:
		return randint(1, 12)
	elif i == 5:
		return randint(1970, 2000)
def get_mailacc():
	re = requests.get("https://10minutemail.net/", proxies=proxies)
	soup = BeautifulSoup(re.text, "html.parser")
	mail = soup.find("input", attrs={"class" : "mailtext"})['value']
	global cookies_10minutemails
	cookies_10minutemails = re.cookies
	return mail
def get_mailverify():
	global cookies_10minutemails
	rev = requests.get("https://10minutemail.net/mailbox.ajax.php", proxies=proxies, cookies=cookies_10minutemails)
	while (rev.text).find("Facebook") == -1:
		rev = requests.get("https://10minutemail.net/mailbox.ajax.php", proxies=proxies, cookies=cookies_10minutemails)
		time.sleep(1)
	number_verify = re.search("([0-9])\d{4}", rev.text)
	return number_verify.group(0)
while 1:
	headers = {"Upgrade-Insecure-Requests": "1"}
	s = requests.session()
	r = s.get('https://mbasic.facebook.com/reg', proxies=proxies)
	cookies = r.cookies
	soup = BeautifulSoup(r.text, "html.parser")

	lsd = soup.find("input", attrs={"name" : "lsd"})['value']
	reg_instance = soup.find("input", attrs={"name" : "reg_instance"})['value']
	reg_impression_id = soup.find("input", attrs={"name" : "reg_impression_id"})['value']

	mail = get_mailacc()

	payload = {
			"lsd": lsd,
			"cpp": 2,
			"reg_instance": reg_instance,
			"submission_request": "true",
			"i": "",
			"helper": "",
			"reg_impression_id": reg_impression_id,
			"field_names%5B%5D": ["firstname", "reg_email__", "sex", "birthday_wrapper", "reg_passwd__"],
			"lastname": random_info(randint(1, 2)),
			"firstname": random_info(0), 
			"reg_email__": mail,
			"sex": randint(1, 2),
			"birthday_day": random_info(3),
			"birthday_month": random_info(4),
			"birthday_year": random_info(5),
			"reg_passwd__": "qwerty456",
	};

	# print(payload)

	r = s.post('https://mbasic.facebook.com/reg', payload, proxies=proxies, cookies=cookies, headers=headers)
	
	r = s.get('https://mbasic.facebook.com/confirmemail.php', proxies=proxies)


	soup = BeautifulSoup(r.text, "html.parser")

	if soup.find("a", attrs={"class" : "t u"}):
		file_acc = open('C:/Users/Admin/acc.txt', 'w', encoding='utf-8')
		file_acc.write(mail + "|qwerty456|")
	elif soup.find("input", attrs={"name" : "photo_input"}):
		print("Checkpoint image !! ")
	elif soup.find("input", attrs={"value" : "code_sms"}):
		print("Check number phone! ")
	elif soup.find("input", attrs={"name" : "login"}):
		print('Wrong information !! ')
		continue
	else:
		number_verify = get_mailverify()
		fb_dtsg = soup.find("input", attrs={"name" : "fb_dtsg"})['value']
		payload = {
				"fb_dtsg": fb_dtsg,
				"c": number_verify,
		}
		r = s.post('https://mbasic.facebook.com/confirmemail.php', payload, proxies=proxies, headers=headers)
		file_acc = open('C:/Users/Admin/acc.txt', 'w', encoding='utf-8')
		file_acc.write(mail + "|qwerty456|")
		print("Check mail! ")
	print(mail)
