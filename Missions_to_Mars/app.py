from flask import Flask, render_template, redirect
import pymongo
import scrape_mars

app = Flask(__name__)

# Connect to PyMongo DB
client = pymongo.MongoClient('mongodb://localhost:27017')

# Connect to a database. Will create one if not already available.
db = client.mars_db

@app.route("/")
def index():
    # Find record of data from the mongo database
    listings = db.scrape.find_one()
    
    # Return template and data
    return render_template("index.html", listings=listings)

@app.route("/scrape")
def scrape():
    #Run the scrape function from scrape_mars
    scrape_data = scrape_mars.scrape()
    
    # Update Monogo database using 
    db.scrape.update({}, scrape_data, upsert=True)

    #Redirect back to home page
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
