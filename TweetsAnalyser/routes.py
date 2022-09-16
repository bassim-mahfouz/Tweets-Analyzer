from TweetsAnalyser import app
from flask import render_template,request
import TweetsAnalyser.modules.tweeter as sntwitter
import pandas as pd
import itertools

@app.route('/')
@app.route('/home')
def home_page():
        #items = Item.query.filter_by(owner=None)
        #owned_items = Item.query.filter_by(owner=current_user.id)
    data= pd.DataFrame(itertools.islice(sntwitter.TwitterSearchScraper(
'"#nft"').get_items(),100000))
    tweets=data[['user','rawContent','hashtags']]
    print(data.columns)
    print(tweets)
    return render_template('home.html',tweets=tweets)
        # items=items, purchase_form=purchase_form, owned_items=owned_items, selling_form=selling_form

