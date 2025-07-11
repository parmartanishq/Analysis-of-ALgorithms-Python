def naive_search(text, pattern):
    n = len(text)  # Length of the full text
    m = len(pattern)  # Length of the pattern to search

    for i in range(n - m + 1):  # Slide the pattern over the text
        match = True
        for j in range(m):  # Check each character in pattern
            if text[i + j] != pattern[j]:  # If mismatch found
                match = False
                break
        if match:  # If full pattern matches
            print(f"Pattern found at index {i}")

# Main function to take user input
def main():
    print("Naïve String Matching Algorithm")
    
    text = input("Enter the text: ")  # Input the full text
    pattern = input("Enter the pattern to search: ")  # Input the pattern

    if not text or not pattern:
        print("Text and pattern must not be empty.")
        return

    naive_search(text, pattern)

# Run the program
if __name__ == "__main__":
    main()

