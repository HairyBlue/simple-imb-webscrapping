from bs4 import BeautifulSoup as bs
import requests

headers = {
        "User-Agent": "Windows 10-based PC using Edge browser Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"
}

url = "https://www.imdb.com/chart/top/"

try:
    source = requests.get(url, headers=headers)
    source.raise_for_status()

    soup = bs(source.text, "html.parser")
    list = soup.find("ul", role="presentation").find_all("h3")

    if list: 
        extract_list = []

        for h3 in list:
            extract_list.append(h3.get_text())
        print("top 250 movies in IMB webites\n")
        for text in extract_list:
            print(text)
except Exception as e:
    print(e)