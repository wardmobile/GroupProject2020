_version__ = "0.2"
__status__ = "Development"
__owners__ = "Ben Ward 100486362";

from bs4 import BeautifulSoup
import requests
import LinkLibrary


class WebScraper:
    def __init__(self):
        self.__link_library = LinkLibrary.LinkLibrary()

    def run(self):
        print("Im Running :D")
        counter = self.__link_library.get_count()
        for i in range(0, counter - 1, 1):  # for every link loaded
            print("getting link number : " + str(i))
            temp_link = self.__link_library.get_link(i)  # get the link
            print("getting html from :" + temp_link)
            text = requests.get("https://www.agillemed.com.br").text  # gets html from specif
            #do somthing here instead of print

if __name__ == "__main__":
    service = WebScraper()
    service.run()
