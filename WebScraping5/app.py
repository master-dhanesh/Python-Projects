import requests
from bs4 import BeautifulSoup as bs
import webbrowser
try:
    github_user = input("Input Github User: ")
    url = 'https://github.com/' + github_user + '/'
    r = requests.get(url)
    soup = bs(r.content, 'html.parser'  )
    profile_image = soup.find('img',{'class': 'avatar avatar-user width-full border color-bg-default'})['src']
    webbrowser.open(profile_image)
    print(profile_image)
except Exception as e:
    print(f"Wrong User Name: {e}")

