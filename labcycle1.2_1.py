def word_count(str):
    word=str.split()
    count=dict()

    for word in word:
       if word in count:
           count[word]=count[word]+1
       else:
           count[word]=1
    return count
print("occurence of each word:")
print(word_count('happy be happy'))