import requests
import os

os.makedirs("books", exist_ok=True)

print("Requesting Webpage...")

for i in range(1,77817):
    r = requests.get("https://www.gutenberg.org/cache/epub/"+str(i)+"/pg"+str(i)+".txt")
    
    with open("books/book"+str(i)+".txt", "w", encoding="utf-8") as f:
        f.write(r.text)