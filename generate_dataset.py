import random
import json
from pathlib import Path

# Word pools
adjectives = ["fresh", "organic", "modern", "quick", "green", "cozy", "global", "smart", "vintage", "techie"]
business_types = [
    "coffee shop", "bookstore", "fitness center", "AI startup", "pet grooming",
    "vegan bakery", "law firm", "real estate agency", "toy store", "car dealership"
]
locations = [
    "downtown", "by the lake", "in Silicon Valley", "on Main Street", "in a small town",
    "in NYC", "in LA", "near the airport", "in Chicago", "in Texas"
]

# Domain suffixes
tlds = [".com", ".net", ".org", ".io", ".biz"]

# Basic domain name constructor
def generate_domain(business_name: str) -> str:
    name = business_name.lower().replace(" ", "")
    return name + random.choice(tlds)

# Build one sample
def generate_entry() -> dict:
    adj = random.choice(adjectives)
    btype = random.choice(business_types)
    loc = random.choice(locations)

    description = f"{adj} {btype} {loc}"
    domain = generate_domain(description)

    return {
        "business_description": description,
        "target_domain": domain,
        "adjective": adj,
        "business_type": btype,
        "location": loc,
        "version": "v1"
    }

# Main function to generate dataset
def generate_dataset(n=500, output_path="data/domain_dataset.jsonl"):
    Path("data").mkdir(exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        for _ in range(n):
            entry = generate_entry()
            f.write(json.dumps(entry) + "\n")

    print(f"Dataset with {n} entries saved to {output_path}")

# Run if script is called
if __name__ == "__main__":
    generate_dataset()
