from flask import Flask, render_template, redirect
import os
import pymongo
import scrape_mars


MONGODB = os.environ.get('MONGODB')
MONGOUSERPASS = os.environ.get('MONGOUSERPASS')


app = Flask(__name__)

# Connect to PyMongo DB
client = pymongo.MongoClient(f'mongodb+srv://{MONGOUSERPASS}@{MONGODB}')

# Connect to a database. Will create one if not already available.
db = client.mars_db

## if no collections in database then run scrape function
count = db.scrape.count_documents({})
print(f"{count} collections in {db}")

if db.scrape.count_documents({}) == 0:

    #Run the scrape function from scrape_mars
    scrape_data = scrape_mars.scrape()
    
    #Update Monogo database using 
    db.scrape.update({}, scrape_data, upsert=True)

@app.route("/")
def index():
    # Find record of data from the mongo database
    listings = db.scrape.find_one()
    
    # Return template and data
    return render_template("index.html", listings=listings)

@app.route("/scrape")
def scraper():
    #Run the scrape function from scrape_mars
    scrape_data = scrape_mars.scrape()
    
    # Update Monogo database using 
    db.scrape.update({}, scrape_data, upsert=True)

    #Redirect back to home page
    return redirect("/", code=302)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)