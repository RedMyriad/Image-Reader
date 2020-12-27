"""
Author: Francisco
Purpose: Reads text data from image
Possible future updates: Add backslashes to program automatically, file not found error messages,
Add more statistics
Future Project Idea: Chrome extension that checks a page for bad-words and gives page a score
"""

import cv2
import pytesseract

# Introduce user to program


# Ask for file to be read
#file = input("Enter the full path for the file (Caution: Enter Backslashes Twice): ")

# Give user assurances
print("Disclaimer: No file checking has been done for this program.")
print("Doing Computer Magic....")
print()

# Point to Tesseract installation
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

print()
print("Welcome to Image Reader")

while True:
    prompt = input("\nEnter the full path for the file (Caution: Enter Backslashes Twice): ")
    try:
        img = cv2.imread(prompt)
        cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        # Give user assurances
        print("Doing Computer Magic....")
        print()
    except:
        print("Wrong file or file path")
    else:
        break




# Send file in for reading
#img = cv2.imread(file)
#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


sentence = []   # Holds individual sentences found
wordCount = 0   # Holds total word count for image
puncCount = 0   # Holds total punctuation count for image


for word in (pytesseract.image_to_string(img)):
    if word == "\n" or word == "-":
        # Program prints a ton of empty space that may be found in image so skipping that data
        # Hyphens are skipped as those are used to indicate the word goes on to next line but
        # the computer reads the entire page as one long line of characters so it is not needed.
        continue
    elif word == ".":
        puncCount += 1
        if sentence[0] == " ":
            sentence.pop(0)
            wordCount -= 1
        for words in sentence:
            if words.isalnum():
                print(words, end="")
            else:
                if words.isspace():
                    print(words, end="")
                else:
                    puncCount += 1
                    print(words, end="")
        sentence.clear()
        print()
    else:
        if word.isspace():
            wordCount += 1
        sentence.append(word)

# Print page statistics
print("Image Statistics:")
print("")
print(f'Words: {wordCount}')
print(f'Punctuation: {puncCount}')