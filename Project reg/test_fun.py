# import requests
# from bs4 import BeautifulSoup

# proxies = {
#   'https': 'http://127.0.0.1:1080',
# }

# r = requests.get("https://10minutemail.net/", proxies=proxies)
# soup = BeautifulSoup(r.text, "html.parser")
# mail = soup.find("input", attrs={"class" : "mailtext"})
# print(mail)
import re
text = """<html><head>
<meta http-equiv="content-type" content="text/html; charset=windows-1252"></head><body><table id="maillist"><tbody><tr><th>From</th><th>Subject</th><th>Date</th></tr><tr onclick="location='readmail.html?mid=welcome'" style="font-weight: bold; cursor: pointer;"><td>no-reply@10minutemail.net</td><td><a href="https://10minutemail.net/readmail.html?mid=welcome">Hi, Welcome to 10 Minute Mail</a></td><td><span title="2017-05-16 06:14:51 UTC">35 seconds ago</span></td></tr><tr onclick="location='readmail.html?mid=PZcLgE'" style="font-weight: bold; cursor: pointer;"><td>"Facebook" &lt;registration@facebookmail.com&gt;</td><td><a href="https://10minutemail.net/readmail.html?mid=PZcLgE">92071 lÃ&nbsp; mÃ£ xÃ¡c nháº­n Facebook cá»§a báº¡n</a></td><td><span title="2017-05-16 06:15:21">just now</span></td></tr></tbody></table></body></html>"""

m = re.search('([0-9])\d{4}', text)

print(m.group(0))