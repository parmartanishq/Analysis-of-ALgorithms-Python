def rabin_karp(text, pattern):
    d = 256  # Total characters in ASCII
    q = 101  # A prime number to avoid collisions and overflows
    n = len(text)
    m = len(pattern)

    pattern_hash = 0
    text_hash = 0
    h = 1

    # Calculate the value of h = pow(d, m-1) % q
    for i in range(m - 1):
        h = (h * d) % q

    # Calculate hash value for pattern and first window of text
    for i in range(m):
        pattern_hash = (d * pattern_hash + ord(pattern[i])) % q
        text_hash = (d * text_hash + ord(text[i])) % q

    # Slide the pattern over the text one character at a time
    for i in range(n - m + 1):
        # If hash values match, then check characters one by one
        if pattern_hash == text_hash:
            if text[i:i + m] == pattern:
                print(f"Pattern found at index {i}")

        # Calculate hash for the next window of text
        if i < n - m:
            text_hash = (d * (text_hash - ord(text[i]) * h) + ord(text[i + m])) % q
            if text_hash < 0:
                text_hash = text_hash + q

# Main program: get input from the user
text = input("Enter the text: ")
pattern = input("Enter the pattern to search for: ")

# Call the Rabin-Karp search function
rabin_karp(text, pattern)
