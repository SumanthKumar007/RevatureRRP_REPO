def count_vowels(str):
    count = 0
    for letter in str:
        if letter in "aeiouAEIOU":
            count+=1
    return count
print(count_vowels("Sumanth Kumar"))