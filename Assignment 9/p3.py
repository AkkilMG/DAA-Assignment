


def search(pattern, text):
    pl = len(pattern)
    tl = len(text)
    pattern_hash = sum(ord(pattern[i]) for i in range(pl))
    text_hash = sum(ord(text[i]) for i in range(pl))

    for i in range(tl - pl + 1):
        if pattern_hash == text_hash:
            if pattern == text[i:i+pl]:
                print(f"Pattern found at index: {i}")
                return
        if i < tl - pl:
            text_hash = text_hash - ord(text[i]) + ord(text[i+pl])

    print("Pattern not found in the text")


text = input()
pattern = input()
search(pattern, text)
