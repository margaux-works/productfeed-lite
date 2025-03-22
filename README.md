# productfeed-lite

A simple Python script that simulates the first step of a product feed cleaner.  
It fetches real product data from an open API, enriches it with custom logic, and exports a cleaned version.

---

## What does it do?

- Fetches product data from the [FakeStore API](https://fakestoreapi.com/).
- Cleans and enriches each product:
  - Capitalizes product titles
  - Removes unnecessary spaces from descriptions
  - Flags products as `"is_expensive"` if price > 100
  - Adds a `"rating_label"` based on the product’s customer rating:
    - `>= 4.5` → `"Excellent product"`
    - `4.0 - 4.49` → `"Great product"`
    - `3.0 - 3.99` → `"Good product"`
    - `2.0 - 2.99` → `"Average product"`
    - `< 2.0` → `"Poor product"`
- Saves the output to `cleaned_feed.json`

---

## Tech Stack

- Python 3
- [requests](https://pypi.org/project/requests/) (HTTP client)
- JSON module (built-in)

---

## How to run it

### 1. Install dependencies

If you’re using a virtual environment:

```bash
pip install -r requirements.txt
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 1. Run the script

```bash
python productfeed-lite.py
```

### 3. Output

The enriched product feed will be saved to:

```bash
cleaned_feed.json
```

## Why this project?

- To practice with Python!
- Work with APIs and product feed data
- Structure and enrich raw data
- Apply business logic to classification
- Simulate real-world use cases like product catalog optimization‚
