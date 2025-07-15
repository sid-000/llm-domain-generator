import random
import json
from pathlib import Path

# Word pools
adjectives = ["fresh", "organic", "modern", "quick", "green", "cozy", "global", "smart", "vintage", "techie"]
business_types = ["coffee shop", "bookstore", "fitness center", "AI startup", "pet grooming", "vegan bakery", "law firm", "real estate agency", "toy store", "car dealership"]
locations = ["downtown", "by the lake", "in Silicon Valley", "on Main Street", "in a small town", "in NYC", "in LA", "near the airport", "in Chicago", "in Texas"]

# Domain suffixes
tlds = [".com", ".net", ".org", ".io", ".biz"]

# Function to generate domain name
def generate_domain(business_name: str) -> str:
    return business_name.lower().replace(" ", "") + random.choice(tlds)

# Generate a single entry
def generate_entry() -> dict:
    adj = random.choice(adjectives)
    btype = random.choice(business_types)
    loc = random.choice(locations)

    description = f"{adj} {btype} {loc}"
    domain = generate_domain(description)

    return {
        "business_description": description,
        "target_domain": domain
    }

# Generate N samples and write to file
def generate_dataset(n=500, output_file="data/domain_dataset.jsonl"):
    Path("data").mkdir(exist_ok=True)

    with open(output_file, "w", encoding="utf-8") as f:
        for _ in range(n):
            sample = generate_entry()
            f.write(json.dumps(sample) + "\n")

    print(f"✅ Generated {n} samples to {output_file}")

# Entry point
if __name__ == "__main__":
    generate_dataset()

