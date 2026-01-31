import requests
import os

os.makedirs("../scraped_data/www.gutenberg.org", exist_ok=True)

print("Requesting Webpage...")

#77817
for i in range(1,77817+1):
    r = requests.get("https://www.gutenberg.org/cache/epub/"+str(i)+"/pg"+str(i)+".txt")
    
    with open("../scraped_data/www.gutenberg.org/book"+str(i)+".txt", "w", encoding="utf-8") as f:
        f.write(r.text)