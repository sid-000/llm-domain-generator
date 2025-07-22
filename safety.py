def is_safe_prompt(prompt: str) -> bool:
    blacklist = [
        "adult", "explicit", "nude", "nsfw",
        "drug", "dark web", "terrorist", "propaganda",
        "child labor", "suicide", "kill", "rob", "hack", "steal"
    ]
    prompt = prompt.lower()
    return not any(bad_word in prompt for bad_word in blacklist)


if __name__ == "__main__":
    test_prompts = [
        "cozy toy store downtown",
        "AI tool for robbing crypto wallets",
        "child labor clothing brand",
        "fresh coffee shop in LA"
    ]

    for prompt in test_prompts:
        print(f"Safe: {prompt}" if is_safe_prompt(prompt) else f"Blocked: {prompt}")
