import pandas as pd
import requests
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

def scrape():
    browser = Browser('chrome', executable_path=ChromeDriverManager().install(), headless=False)

    browser.visit("https://redplanetscience.com/")

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    news_title = soup.find("div", class_="content_title").get_text()
    print(news_title)

    news_p = soup.find("div", class_="article_teaser_body").get_text()
    print(news_p)

    #visit url in splinter
    browser.visit("https://spaceimages-mars.com/")

    #set variables again for new URL
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    #get featured image address and save to featured_image_url variable
    base_url = "https://spaceimages-mars.com/"
    featured_image_url = base_url + soup.find("img", class_="headerimage fade-in")["src"]
    print(featured_image_url)


    #use pandas to scrape table from web page
    tables = pd.read_html("https://galaxyfacts-mars.com/")
    print(tables)

    # get table from list
    df = tables[1]
    df

    # convert to html string
    html_table = df.to_html(index=False, header=False, classes="table-striped")
    print(html_table)

    #visit url in splinter
    #url = "https://marshemispheres.com/cerberus.html"
    url = "https://marshemispheres.com/"
    browser.visit(url)

    #set variables again for new URL
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # create list to store dictionaries
    hemisphere_image_urls = []
    # create list to store links
    link_list = []
    #find all div tags with class description and iterate over them
    for div in soup.findAll("div", attrs={"class":"description"}):
        #find all hyperlinks
        links_list = div.findAll("a")
        #iterate over hyperlinks
        for link in links_list:
            #get the url
            href = link['href']
            #turn url into full url
            full_link = url+ href
            #append url to list
            link_list.append(full_link)

    #print url list to check
    print(link_list)


    # iterate over links in link list
    for link in link_list:
        url = link
        browser.visit(url)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        #find all divs with class downloads
        for div in soup.findAll("div", attrs={"class": "downloads"}):
            base_url = "https://marshemispheres.com/"
            #find links with text Original and take href
            img_url = base_url + div.find("a", text="Sample")["href"]
            #find h2 and get text from h2
            h2 = soup.find("h2").get_text()
            # remove word Enhanced
            title = h2.replace("Enhanced","")
            #remove whitespace at end
            title = title.rstrip()
            #create dictionary to hold results
            title_img_dict = {
            "title": title,
            "img_url": img_url
            }
            #append dictionary to list of dictionaries
            hemisphere_image_urls.append(title_img_dict)

    #check list of dictionaries
    print(hemisphere_image_urls)

    scrape_data = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "table": html_table,
        "image_urls": hemisphere_image_urls
    }


    return(scrape_data)
