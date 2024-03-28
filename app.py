import time
import sqlite3
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

# Create/connect to the database
conn = sqlite3.connect('price_data.db')
c = conn.cursor()

# Create table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS prices
             (product text, amazon_price real, google_price real)''')

def insert_into_db(product, amazon_price, google_price):
    c.execute("INSERT INTO prices VALUES (?, ?, ?)", (product, amazon_price, google_price))
    conn.commit()

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        product = request.form['product']

        url = "https://price-analytics.p.rapidapi.com/search-by-term"

        payload = {
            "source": "google",
            "country": "in",
            "values": product
        }
        headers = {
            "content-type": "application/x-www-form-urlencoded",
            "X-RapidAPI-Key": "b3d1423e7bmsh64ac78ee3adc8ddp10ef9djsn48535059df90",
            "X-RapidAPI-Host": "price-analytics.p.rapidapi.com"
        }
        
        response = requests.post(url, data=payload, headers=headers)

        googleid = response.json()['job_id']

        payload = {
            "source": "amazon",
            "country": "in",
            "values": product
        }

        response = requests.post(url, data=payload, headers=headers)

        amzid = response.json()['job_id']

        # Amazon
        time.sleep(120)

        url = f"https://price-analytics.p.rapidapi.com/poll-job/{googleid}"

        headers = {
            "X-RapidAPI-Key": "b3d1423e7bmsh64ac78ee3adc8ddp10ef9djsn48535059df90",
            "X-RapidAPI-Host": "price-analytics.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers)

        result = response.json()
        print(result)
        
        amazon_price = result["results"][0]['content']['offers'][0]['price']
        # amz_url = result["results"][0]['content']['offers'][0]['url']
        # print(amz_url)
        amz_url = None

        # Google
        url = f"https://price-analytics.p.rapidapi.com/poll-job/{amzid}"
        
        
        
        response = requests.get(url, headers=headers)
        

        result = response.json()
        

        google_price = result["results"][0]['content']['offers'][0]['price']
        # google_url = result["results"][0]['content']['offers'][0]['url']
        google_url = None
        # Insert data into the database
        # insert_into_d
        # 
        # 
        #b(product, amazon_price, google_price)
        
        finalUrl = None
        if amazon_price < google_price:
            finalUrl = amz_url
        else:
            finalUrl = google_url

        return render_template('index.html', amazon_price=amazon_price, google_price=google_price,final_url=finalUrl)
    return render_template('index.html', amazon_price=None, google_price=None, final_url=None)

if __name__ == '__main__':
    app.run(debug=True)
