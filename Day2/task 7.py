def count_words(str):
    count=0
    str= str.split(" ")
    for word in str:
        count+=1
    return count
print(count_words("sumanth kumar valluru"))