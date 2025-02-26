import requests
from bs4 import BeautifulSoup

# URL of the website you want to scrape
url = "https://example.com"

# Send a GET request to the webpage
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, "lxml")
    
    #extract text
    text = soup.get_text(separator=" ", strip=True)
    
    print(text)
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
