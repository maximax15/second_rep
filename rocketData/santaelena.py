from requests import Session
from bs4 import BeautifulSoup
from requests_html import HTMLSession

url = "https://www.santaelena.com.co/"




def get_addresses(url, session):
    with session.get(url) as response:
        text = response.text
        soup = BeautifulSoup(text, "html.parser")
        addresses =  soup.select("div.elementor-element > div.elementor-widget-container > div.elementor-text-editor.elementor-clearfix > p > br")

        return [address.text for address in addresses]
				




def main(url):
    with Session() as session:
        with session.get(url) as response:
            text = response.text
            soup = BeautifulSoup(text, "html.parser")
            links = soup.select(
                "ul.sub-menu.elementor-nav-menu--dropdown > li.menu-item.menu-item-type-post_type.menu-item-object-page > a.elementor-sub-item"
            )
            lst = [link.attrs["href"] for link in links]
            lst_links = lst[0:5]
            for el in lst_links:
                print(get_addresses(el, session))

main(url)
