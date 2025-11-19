import os
import string
from collections import Counter

def text_extractor(file_path, num_of_keywords = 10):
    if(os.path.exists(file_path)):
        if(os.path.isfile(file_path)):
            with open (file_path, "r", encoding = 'utf-8') as f:
                text = f.read()
                text = text.lower()
                text = text.translate(str.maketrans('', '', string.punctuation))
                words = text.split()

                word_count = Counter(words)

                keywords = word_count.most_common(num_of_keywords)

                print(f"Extracted Keywords from {file_path} are:\n")
                for word, count in keywords:
                    print(f"{word} --> {count} Occurrences")
        else:
            print("Not a File")
    else:
        print(f"File does not Exist at {file_path}")

number_of_keywords = 5
test_file = "test.txt"

if not os.path.exists(test_file):
    with open(test_file, 'w', encoding='utf-8') as f:
        f.write("Digital literacy plays a pivotal role in empowering individuals to achieve better academic results by providing them with the necessary skills to navigate the digital landscape. In addition to mastering the tools and technologies, it fosters critical thinking and problem-solving abilities, equipping students to tackle complex challenges in an increasingly digitalized world. ")

if __name__ == "__main__":
    text_extractor(test_file, number_of_keywords)
        