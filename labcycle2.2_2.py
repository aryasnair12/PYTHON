def longest(list2):
    max=0

    for i in list2:
         if(len(i)>max):
             max=len(i)
             temp=i
    print("the word with longest length is",temp,max)


list1=["apple","orange","mulberry","grapes"]
longest(list1)