# LLM Domain Name Generator – AI Engineer Homework

This project implements a simple LLM-based domain name generator with a strong focus on evaluation, edge case handling, and content safety. The goal was to simulate an iterative improvement cycle using GPT-based evaluation and synthetic data generation.

---

## ✅ What’s Included

### 1. Synthetic Dataset
- 500+ examples of business descriptions with generated domain names.
- Dataset created via a randomized script covering various business types, tones, and locations.

### 2. LLM-as-a-Judge Evaluation
- Built a structured GPT-based evaluator to score each domain on:
  - Relevance
  - Brandability
  - Appropriateness
- Each entry is rated and saved in `data/eval_scores_v1.jsonl`.

### 3. Edge Case Discovery
- Injected inappropriate, unethical, and sensitive business prompts.
- Evaluated LLM behavior on these.
- Analyzed failure cases (e.g., adult content, violence, illegal intent).

### 4. Safety Filtering
- Added keyword-based content guardrails (`safety.py`).
- Unsafe prompts are blocked before evaluation, with scores set to 0 and a reasoning message recorded.

---

## ⚠️ What Was Skipped (Time Constraints)

- ❌ No fine-tuning of an open-source LLM (e.g., LLaMA, Mistral)
- ❌ No LoRA / full model training
- ❌ No API deployment (FastAPI or Streamlit)
- ❌ No Jupyter notebook report or plots

The project was developed over a short time window, so I prioritized core evaluation logic, reproducibility, and safety coverage over model training or frontend/API polish.

---

## 🧠 Discussion Readiness

I’m happy to walk through:
- How I generated the dataset
- How the evaluator and scoring prompt work
- How I identified and blocked edge cases
- What I would add or improve in a second phase (fine-tuning, real-time API, model comparison)

---

## 🔧 Requirements

- Python 3.10+
- `openai`, `python-dotenv`, `tqdm`
- Set your OpenAI API key in a `.env` file:  
  `OPENAI_API_KEY=sk-...`

---

## ✅ Run the Project

```bash
# 1. Generate dataset
python generate_dataset.py

# 2. Evaluate (GPT-based scoring)
python evaluate.py

# 3. (Optional) Add edge cases
python append_edge_cases.py



📂 Output Files

- data/domain_dataset.jsonl – 500+ business/domain pairs

- data/eval_scores_v1.jsonl – GPT scoring + blocked results