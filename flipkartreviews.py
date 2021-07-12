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
	#this snippet is to find the right url with product-reviews keyword in it
	req = rq.get(url,headers=headers)
	soup = BeautifulSoup(req.text,'html.parser')
	for t in soup.findAll('a',attrs={'href':re.compile("/product-reviews/")}):
		q = t.get('href')
		link.append(q)
		for i in link:
			if re.search("LSTMOB[A-Z]|[0-9]|[A-Z][0-9]|[0-9][A-Z]|[0-9][A-Z]*|[A-Z][0-9]*",i):
				ln = i
		l = "https://www.flipkart.com{}".format(ln)	
	print("Processing..!!")
	#now crawl through the new url found
	req=rq.get(l,headers=headers)
	new_link = BeautifulSoup(req.text,"html.parser")
	page_sec = new_link.find("div",attrs={"class":"_2MImiq _1Qnn1K"})
	num_array= re.findall(r'[0-9]+',page_sec.span.text)
	i = 1
	j = max(num_array) #since we get char of num(eg:Page 1 of 31).Try to add it into list and get large number as assumption of the reviews pages are upto that large number
	j = int(j)
	print("Found the url:"+l)
	print(j)
	product_name = new_link.find('div',attrs={'class':'_2s4DIt _1CDdy2'}).text
	for i in range(i,j+1):
		re_page = rq.get(l+"&page="+str(i),headers=headers)
		soup = BeautifulSoup(re_page.text,'html.parser')
		print("\nLoading reviews for page {}\n".format(i))
		for r in soup.findAll('p',attrs={'class':'_2-N8zT'}):
			review.append(r.text)
			
		print("Loading ratings for page {}\n".format(i))
		for r in soup.findAll('div',attrs={'class':'_3LWZlK _1BLPMq'}):
			rating.append(r.text)
		print("Loading comments for page {}\n".format(i))
		for r in soup.findAll('div',attrs={'class':'t-ZTKy'}):
			comment.append(r.text)
		

	print(len(review))
	print(len(rating))
	print(len(comment))
	a = {"Rating":rating,"Review":review,"Comments":comment}
	df = (pd.DataFrame.from_dict(a,orient='index')).transpose()
	
	df.to_csv('{}.csv'.format(product_name),index=False,header=True,encoding='utf-8')
	print("Successfully loaded the data!!")
except ConnectionError:
	print("Aborted!Poor internet connection")
