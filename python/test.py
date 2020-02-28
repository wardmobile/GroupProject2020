from bs4 import BeautifulSoup
import requests
import LinkLibrary



html_content = requests.get("https://www.agillemed.com.br").text
print(html_content)

