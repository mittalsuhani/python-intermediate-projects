from difflib import SequenceMatcher

with open('demo1.txt', 'r') as file1, open('demo2.txt', 'r') as file2:
    text1 = file1.read()
    text2 = file2.read()    
similarity = SequenceMatcher(None, text1, text2).ratio()
print(f'Similarity: {similarity:.2%}')



