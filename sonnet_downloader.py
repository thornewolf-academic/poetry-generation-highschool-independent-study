import requests
from bs4 import BeautifulSoup

BASE_SONNET_URI = "http://www.shakespeares-sonnets.com/sonnet/"


def get_sonnets_from_website(n: int):
    uri = f"{BASE_SONNET_URI}{n}"
    response = requests.get(uri)
    page_body = response.text
    soup = BeautifulSoup(page_body, "html.parser")
    sonnet_body = soup.find(id="sonnettext")
    assert sonnet_body is not None
    sonnet_body_list = sonnet_body.find_all("em")  # type: ignore
    sonnet_body_list = [em.text for em in sonnet_body_list]
    sonnet_body = "\n".join(sonnet_body_list)
    return sonnet_body


def download_sonnets():
    sonnets = get_sonnets_from_website(0)
    with open("sonnets.txt", "w") as f:
        f.write(sonnets)


def fetch_local_sonnets():
    with open("sonnets.txt", "r") as f:
        sonnets = f.read()
    return sonnets


if __name__ == "__main__":
    download_sonnets()
