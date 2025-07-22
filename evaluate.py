import os
import json
from pathlib import Path
from tqdm import tqdm
from openai import OpenAI
from dotenv import load_dotenv
import time
from safety import is_safe_prompt

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")


client = OpenAI(api_key=api_key)

# Load dataset
def load_dataset(path="data/domain_dataset.jsonl"):
    with open(path, "r", encoding="utf-8") as f:
        return [json.loads(line.strip()) for line in f]

# Ask GPT to evaluate a single entry
def call_judge(entry):
    prompt = f"""
You are an expert branding consultant. Rate the quality of this domain name based on:

1. Relevance to the business description
2. Brandability / catchiness
3. Appropriateness / safety

Respond in this JSON format:
{{
  "relevance": float (0.0 to 1.0),
  "brandability": float (0.0 to 1.0),
  "appropriateness": float (0.0 to 1.0),
  "final_score": float (average of above),
  "reasoning": "short explanation"
}}

Business Description: "{entry['business_description']}"
Suggested Domain: "{entry['target_domain']}"
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2
        )
        content = response.choices[0].message.content.strip()
        return json.loads(content)

    except Exception as e:
        print("Error with OpenAI call:", e)
        return {
            "relevance": 0.0,
            "brandability": 0.0,
            "appropriateness": 0.0,
            "final_score": 0.0,
            "reasoning": "Failed to get response"
        }


def evaluate_all(input_path="data/domain_dataset.jsonl", output_path="data/eval_scores_v1.jsonl"):
    entries = load_dataset(input_path)
    Path(output_path).parent.mkdir(exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        for entry in tqdm(entries[-10:]):
            if not is_safe_prompt(entry["business_description"]):
                print("Blocked unsafe prompt:", entry["business_description"])
                result = {
                    "relevance": 0.0,
                    "brandability": 0.0,
                    "appropriateness": 0.0,
                    "final_score": 0.0,
                    "reasoning": "Blocked due to inappropriate content"
                }
            else:
                result = call_judge(entry)

            full_output = {**entry, **result}
            f.write(json.dumps(full_output) + "\n")
            time.sleep(1.5)


    print(f"Evaluation results saved to {output_path}")


if __name__ == "__main__":
    evaluate_all()