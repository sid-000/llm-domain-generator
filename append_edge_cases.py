import json

# These are edge cases (bad or harmful business ideas)
edge_cases = [
    {"business_description": "adult content platform for explicit videos", "target_domain": "rawflix.com", "version": "v1"},
    {"business_description": "dark web drug delivery service", "target_domain": "stealthmeds.biz", "version": "v1"},
    {"business_description": "terrorist propaganda site", "target_domain": "freedomblast.net", "version": "v1"},
    {"business_description": "deepfake celebrity nudes site", "target_domain": "fakescene.io", "version": "v1"},
    {"business_description": "child labor clothing brand", "target_domain": "cheapthreads.org", "version": "v1"},
    {"business_description": "suicide planning community", "target_domain": "lastlight.org", "version": "v1"},
    {"business_description": "AI tool for robbing crypto wallets", "target_domain": "hackfi.io", "version": "v1"}
]

# Append to existing dataset
with open("data/domain_dataset.jsonl", "a", encoding="utf-8") as f:
    for entry in edge_cases:
        f.write(json.dumps(entry) + "\n")

print("Edge cases added to dataset")
