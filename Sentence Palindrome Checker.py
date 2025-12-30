# WAP to check sentence palindrome

sentence = input("Enter a sentence: ")

# Remove spaces and punctuation, and convert to lowercase
clean = ""

for ch in sentence:
    if ch.isalnum():   # keeps only letters and numbers
        clean += ch.lower()

# Reverse the cleaned string
rev = clean[::-1]

if clean == rev:
    print("The sentence is Palindrome")
else:
    print("The sentence is NOT Palindrome")
