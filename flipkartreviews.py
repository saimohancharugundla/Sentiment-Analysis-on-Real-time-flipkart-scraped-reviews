from bs4 import BeautifulSoup
import requests as rq
import pandas as pd
import re
import xlsxwriter
rating=[]
review = []
comment= []
link=[]
num_array=[]
url= input("Enter URL:")
try:
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
	req = rq.get(url,headers=headers)
	soup = BeautifulSoup(req.text,'html.parser')
	for t in soup.findAll('a',attrs={'href':re.compile("/product-reviews/")}):
		q = t.get('href')
		link.append(q)
		for i in link:
			if re.search("LSTMOB[A-Z]|[0-9]|[A-Z][0-9]|[0-9][A-Z]|[0-9][A-Z]*|[A-Z][0-9]*",i):
				ln = i
		l = "https://www.flipkart.com{}".format(i)	
	print("Processing..!!")
	req=rq.get(l,headers=headers)
	new_link = BeautifulSoup(req.text,"html.parser")
	page_sec = new_link.find("div",attrs={"class":"_2zg3yZ _3KSYCY"})
	num_array= re.findall(r'[0-9]+',page_sec.span.text)
	i = 1
	j = max(num_array)
	j = int(j)
	product_name = new_link.find('div',attrs={'class':'o9Xx3p _1_odLJ'}).text
	while i <= j:
		re_page = rq.get(l+"&page="+str(i),headers=headers)
		soup = BeautifulSoup(re_page.text,'html.parser')
		
		for r in soup.findAll('p',attrs={'class':'_2xg6Ul'}):
			review.append(r.text)
		
		for r in soup.findAll('div',attrs={'class':'hGSR34 E_uFuv'}):
			rating.append(r.text)
		
		for r in soup.findAll('div',attrs={'class':'qwjRop'}):
			comment.append(r.text)
		i+=1

	print(len(review))
	print(len(rating))
	print(len(comment))
	a = {"Rating":rating,"Review":review,"Comments":comment}
	df = (pd.DataFrame.from_dict(a,orient='index')).transpose()
	
	df.to_csv('{}.csv'.format(product_name),index=False,header=True,encoding='utf-8')
	print("Successfully loaded the data!!")
except ConnectionError:
	print("Aborted!Poor internet connection")
