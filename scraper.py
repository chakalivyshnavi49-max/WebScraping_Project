import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

# Website URL
url = "http://quotes.toscrape.com"

# Send request
response = requests.get(url)

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Find all quotes
quotes = soup.find_all("div", class_="quote")

# Empty list
data = []

# Current time
current_time = datetime.now()

# Loop through quotes
for quote in quotes:

    text = quote.find("span", class_="text").text
    author = quote.find("small", class_="author").text

    tags = quote.find_all("a", class_="tag")
    tag_list = [tag.text for tag in tags]

    data.append({
        "Quote": text,
        "Author": author,
        "Tags": ", ".join(tag_list),
        "Quote_Length": len(text),
        "Scraped_Time": current_time
    })

# Create DataFrame
df = pd.DataFrame(data)

# Print first 5 rows
print(df.head())

# Save CSV
df.to_csv("quotes.csv", index=False, encoding="utf-8-sig")

# Save Excel file
df.to_excel("quotes.xlsx", index=False)

print("Scraping completed successfully!")
print("Files saved as quotes.csv and quotes.xlsx")