import requests
from bs4 import BeautifulSoup

def get_post_links_from_subreddit(subreddit_url):
    # Send a GET request to the web page
    response = requests.get(subreddit_url)

    # Parse the web page content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all anchor tags with 'href' attributes
    articles = soup.find_all('article', href=False)

    # Iterate through each article and extract the content
    for i, article in enumerate(articles, start=1):
        title_tag = article.find('a', id=lambda x: x and x.startswith('post-title-'))
        title = title_tag.get_text(strip=True) if title_tag else 'Title not found'
        
        body_tag = article.find('div', id=lambda x: x and x.endswith('-post-rtjson-content'))
        body = body_tag.get_text(separator="\n", strip=True) if body_tag else 'Body content not found'
        
        print(f"Article {i}:\n")
        print("Title:", title)
        print("\nBody:\n", body)
        print("\n" + "-"*50 + "\n")

get_post_links_from_subreddit("https://www.reddit.com/r/aznidentity/new/")