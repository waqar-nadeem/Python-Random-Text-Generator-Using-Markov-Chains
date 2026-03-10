import random
import sys
import re

def build_chain(text, n=2):
    words = re.findall(r'\b\w+\b', text.lower())
    chain = {}
    for i in range(len(words) - n):
        key = tuple(words[i:i+n])
        next_word = words[i+n]
        chain.setdefault(key, []).append(next_word)
    return chain, words

def generate_text(chain, words, length=50, n=2):
    start_index = random.randint(0, len(words) - n - 1)
    state = tuple(words[start_index:start_index+n])
    result = list(state)
    for _ in range(length - n):
        options = chain.get(state)
        if not options:
            break
        next_word = random.choice(options)
        result.append(next_word)
        state = tuple(result[-n:])
    return " ".join(result)

def main():
    if len(sys.argv) < 2:
        print("Usage: python markov_generator.py input.txt")
        return
    with open(sys.argv[1], "r", encoding="utf-8") as f:
        text = f.read()
    chain, words = build_chain(text)
    generated = generate_text(chain, words)
    print(generated)

if __name__ == "__main__":
    main()
