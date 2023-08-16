
# Standard imports for scrpaing
from requests import get
from bs4 import BeautifulSoup
import os
import pandas as pd




# create the funciton to call for the article dicntionary
def get_blog_articles():
    
    # URL variable
    url = 'https://codeup.edu/blog/'
    
    # credentials to scrape the website
    headers = {'User-Agent': 'Codeup Data Science'} # Some websites don't accept the pyhon-requests default user-agent
    
    # Response from site
    response = get(url, headers=headers)
    
    # Soup-ified response to be able to call what I need
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Making blog variable to esaiser acess the content
    blogs = soup.find_all('h2', {'class': 'entry-title'})
    
    # Create an empty list of links and headlines
    link_list = []
    headline_list = []

    # Loop throught the blogs to retrieve the headline and link
    for div in blogs:
        headline = div.a.text
        headline_list.append(headline)

        link = div.a['href']
        link_list.append(link)
    
    # Create an empty content_list
    content_list = []

    # Loop through linbk_list to obtain the content of the articles
    for url in link_list:
        # Creds
        headers = {'User-Agent': 'Codeup Data Science'}
        # Response
        response = get(url, headers=headers)
        # Soup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        soup = soup.find_all('div', class_='entry-content')
        content_list.append(soup)

    # Create empty list for text
    text_list = []
    
    # Loop through the content_list for content
    for content in content_list:
        
        text = content[0].text.strip()
        text_list.append(text)
    
    article_data = []

    # Extract and store the data in a list of dictionaries
    for headline, article in zip(headline_list, text_list):
        
        article_dict = {
            'title': headline,
            'content': article
        }
        article_data.append(article_dict)# Extract and store the data in a list of dictionaries


    return article_data




def get_news_articles(refresh=False):
    
    if not os.path.isfile('news_articles.csv') or refresh:
        
        url = 'https://inshorts.com/en/read'
        response = get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        categories = ['business', 'sports', 'technology', 'entertainment']

        inshorts = []

        for category in categories:

            cat_url = url + '/' + category
            response = get(url)
            soup = BeautifulSoup(response.content, 'html.parser')

            titles = [span.text for span in soup.find_all('span', itemprop='headline')]
            contents = [div.text for div in soup.find_all('div', itemprop='articleBody')]

            for i in range(len(titles)):

                article = {
                    'title': titles[i],
                    'content': contents[i],
                    'category': category,
                }

                inshorts.append(article)
                
        inshorts_article_df = pd.DataFrame(inshorts)
        
        inshorts_article_df.to_csv('news_articles.csv', index=False)
                
    return pd.read_csv('news_articles.csv')
