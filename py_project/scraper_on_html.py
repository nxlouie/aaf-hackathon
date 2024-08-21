from bs4 import BeautifulSoup
import json

# Step 1: Open and read the HTML file
with open("py_project/azn_identity.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# Step 2: Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, "lxml")

# Step 3: Now you can work with the parsed HTML
print(soup.prettify())  # This will print the formatted HTML content

 # Find all anchor tags with 'href' attributes
articles = soup.find_all('article', href=False)

# print(articles[0])

# Iterate through each article and extract the content

output = []
for i, article in enumerate(articles, start=1):
    title_tag = article.find('a', id=lambda x: x and x.startswith('post-title-'))

    shreddit = article.find('shreddit-post')
    url = shreddit.get('content-href')
    score = shreddit.get('score')
    comments = shreddit.get('comment-count')


    title = title_tag.get_text(strip=True) if title_tag else 'Title not found'
    
    body_tag = article.find('div', id=lambda x: x and x.endswith('-post-rtjson-content'))
    body = body_tag.get_text(separator="\n", strip=True) if body_tag else 'Body content not found'
    
    output.append(f"URL: {url}\n")
    output.append(f"score: {score}\n")
    output.append(f"comments: {comments}\n")
    output.append(f"Article {i}:\n")
    output.append(f"Title: {title}")
    output.append(f"\nBody:\n{body}")
    output.append("\n" + "-"*50 + "\n")
    output.append({
        "article_number": i,
        "title": title,
        "url": url,
        "score": score,
        "comments": comments,
        "body": body
    })
    
json_output = json.dumps(output, indent=4)

print("starting!")
print(json_output)