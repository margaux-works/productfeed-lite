import requests
import json

# fetch data from FakeStore API
response = requests.get("https://fakestoreapi.com/products")
products = response.json() 

# clean and enrich data with expensive price
cleaned_products = []

for p in products:
    clean = {
        "id": p["id"],
        "title": p["title"].strip().title(),
        "price": p["price"],
        "is_expensive": p["price"] > 100,
        "category": p["category"],
        "description": p["description"].strip(),
    }
    cleaned_products.append(clean)

# save to JSON file
with open("cleaned_feed.json", "w") as f:
    json.dump(cleaned_products, f, indent=2)

# confirmation
print(f"{len(cleaned_products)} product(s) were cleaned and saved to new file cleaned_feed.json")

