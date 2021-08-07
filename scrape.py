import requests
from bs4 import BeautifulSoup
import smtplib
import time

page = 1
links = []
subtext = []
while page != 3:
	url = f"https://news.ycombinator.com/news?p={page}"
	res = requests.get(url)
	soup = BeautifulSoup(res.text, 'html.parser')
	links = links + soup.select('.storylink')
	subtext = subtext + soup.select('.subtext')
	page += 1


def send_mail(hnlist):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('taraasik@gmail.com', 'eyomymdwubalwdvg')
    
    subject = 'Hacker Daily News'
    
    body = 'Find the latest breaking news here: \n\n'

    i=1

    for dict in hnlist:
   	    title = dict.get('title')
   	    link = dict.get('link')
   	    votes = dict.get('votes')
   	    body += f'{i}: {title}, {link}, {votes} \n'
   	    i += 1

    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        'taraasik@gmail.com',
        'taraasik@gmail.com',
        msg.encode("utf-8")
    )
    
    print('HEY EMAIL HAS BEEN SENT!')
    server.quit()


def sort_stories_by_votes(hnlist):
	return send_mail(sorted(hnlist, key = lambda k:k['votes'], reverse=True))
	


def create_custom_hn(links, subtext):
	hn = []
	for index, item in enumerate(links):
		title = item.getText()
		href = item.get('href', None)
		vote = subtext[index].select('.score')
		if len(vote):
			points = int(vote[0].getText().replace(' points', ''))
			if points > 99:
				hn.append({'title': title, 'link': href, 'votes': points})
	return sort_stories_by_votes(hn)

   
while(True):
    create_custom_hn(links, subtext)
    time.sleep(86400) #check the news every day