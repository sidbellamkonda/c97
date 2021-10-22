name=input("Please introduce yourself:")
characterCount=0
wordCount=1
for i in name:
    characterCount+=1
    if (i == ' '):
        wordCount+=1
print('Number of Words:')
print(wordCount)
print('Number of Characters:')
print(characterCount)