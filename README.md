# Web Scraping
![Header Beautiful Soup](readme-header.jpg)

## Outline

I combined the use of PyMongo and Beautiful Soup to scrape a website and store the data in a Mongo database.

Then I used Flask and Bootstrap to render a webpage which pulled the stored scraped results from the Mongo Database.

## Issues
The challenge was extremely difficult I was ready to give up when trying to figure out how to loop and scrape and hemisphere images.


## Mars Facts table
The instructions for the assignment specified to scrape the Mars Facts table, however in the example html render image it shows the Mars-Earth Comparison table.

There were 2 tables on the page.

I used the the table with just the Mars Facts.

## Working HTML scrape screenshot
Below is the result of clicking the scrape button. You can see the content successfully changes based on the dynamic content that changed on the original pages that were scraped.
### Scrape 1
![Scrape 1](Missions_to_Mars/screenshots/scrape-1.png)

### Scrape 2
![Scrape 2](Missions_to_Mars/screenshots/scrape-2.png)

## Customisation

* bootstrap to make the page suitable for viewing on different devices.
* theme from bootswatch for some customisation.
