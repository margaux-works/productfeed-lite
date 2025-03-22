import requests
import json

# fetch data from FakeStore API
response = requests.get("https://fakestoreapi.com/products")
products = response.json() 

# clean and enrich data with expensive price
cleaned_products = []

for p in products:
    rate = p["rating"]["rate"]
    
    if rate >= 4.5:
        rating_label = "Excellent product"
    elif rate >= 4.0:
        rating_label = "Great product "
    elif rate >= 3.0:
        rating_label = "Good product "
    elif rate >= 2.0:
        rating_label = "Average product "
    else:
        rating_label = "Bad product "

    clean = {
        "id": p["id"],
        "title": p["title"].strip().title(),
        "price": p["price"],
        "is_expensive": p["price"] > 100,
        "category": p["category"],
        "description": p["description"].strip(),
        "rating_label": rating_label,
    }
    cleaned_products.append(clean)

# save to JSON file
with open("cleaned_feed.json", "w") as f:
    json.dump(cleaned_products, f, indent=2)

# confirmation
print(f"{len(cleaned_products)} product(s) were cleaned and saved to new file cleaned_feed.json")

