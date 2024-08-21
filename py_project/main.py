from scraper import get_post_links_from_subreddit
from llm import summarize

if __name__ == '__main__':
    val = input("Enter your value: ")

    print("fetching links...")
    output = get_post_links_from_subreddit(val)
    print("summarizing...")
    summary = summarize(output)
    print(summary[0].text)