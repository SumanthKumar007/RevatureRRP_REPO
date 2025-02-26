users = [("Alice", 25, "New York"), ("Bob", 17, "Los Angeles"), ("Charlie", 30,
"Chicago")]
keys = [i[0] for i in users if i[1]>18]
values = [i[1] for i in users if i[1]>18]
dict_list = {k:v for (k, v) in zip(keys, values)}
print(dict_list)