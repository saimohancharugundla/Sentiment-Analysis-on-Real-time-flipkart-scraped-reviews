This project is based on Natural Language Processing in which sentiment prediction and analysis on real-time scraped flipkart reviews(without labels)
You need some basic requirements for implementing this in your env.They are
1.0 = scikit-learn
2.0 = TextBlob
3.0 = nltk
4.0 = pandas
5.0 = emoji

I had uploaded two files here the file named SentimentGithub.ipynb is what makes you clear understanding and differentiate of how textblob is useful for labelling the data and how badly the random placement of labels.
Generally we do sentiment analysis on labelled data.Here we dont have labelled data(realtime scraped data) so How I transform the unlabelled to label data without going into deeper like using clustering algorithms.
I used sklearn's tfidf vectorizerfor vectorizing the data and build classification model using logistic regression on how likely the predicted labels are correct.

We generally notice comments and ratings of the product in ecommerce sites.If we look closer we will notice bad rating even for positive comment. So, I realized the sentiment analysis should be done based on comment rather than rating!Ofcourse ratings will be useful for company to showcase the product but deeper its a trap.

In sentimentanalysis.ipynb file sentiment is predicted on both comments and review columns. Just minimal in changes in the code (replacing review with comments) can be better for sentiment analysis using review section

**Note: In the reviews file I had scraped reviews from flipkart website which had the classes mentioned. Sometimes the classes would change since flipkart follows automation process to get ware of any bots. So kindly change the classes if you notice any errors** and you could contribute to code by your PR

You could notice above some of the datasets created with flipkartreviews.py file code.