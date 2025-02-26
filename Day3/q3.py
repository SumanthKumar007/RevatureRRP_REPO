from ordered_set import OrderedSet
text = "Hello World!"
lower_text = text.lower()
res = {i for i in lower_text if i.isalpha()}
ordered_set = OrderedSet(res)
print(ordered_set)