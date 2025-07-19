import requests
from bs4 import BeautifulSoup

# URL of the news website
URL = "https://www.bbc.com/news"

# Send a GET request
response = requests.get(URL)

# Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find all headline elements
    headlines = soup.find_all('h2')
    
    # Extract text and filter duplicates
    titles = []
    for h in headlines:
        text = h.get_text(strip=True)
        if text and text not in titles:
            titles.append(text)

    # Save to a file
    with open("headlines.txt", "w", encoding="utf-8") as file:
        for title in titles:
            file.write(title + "\n")

    print(f"{len(titles)} headlines saved to headlines.txt")
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)
