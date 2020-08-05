import webbrowser
import bs4
import requests
import logging

# webbrowser.open("https://github.com/imravishar?tab=stars")

logger = logging.getLogger(__name__)
starred_repos = []

# Get all stared repo links
url = "https://github.com/imravishar?tab=stars"


def get_soup(url):
    res = requests.get(url)
    res.raise_for_status()
    return bs4.BeautifulSoup(res.text, "html.parser")


def get_stared_repos(soup):
    all_repos = soup.select("div.col-12.d-block.width-full.py-4.border-bottom")
    return list(map(lambda repo: f"https://github.com{repo.select('a')[0]['href']}", all_repos))


def next_page(soup):
    for pages_link in soup.find_all('a', {'class': 'btn btn-outline BtnGroup-item'}):
        if pages_link.text == "Next":
            return pages_link


while True:
    soup = get_soup(url)
    starred_repos = starred_repos + get_stared_repos(soup)
    next_link = next_page(soup)
    if not next_link:
        break
    url = next_link['href']

print(f"Total count= {len(starred_repos)} \n")
print("\n".join(starred_repos))
