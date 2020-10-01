fruits = [("apple", "red"), ("banana", "yellow"),
          ("tomato", "red"), ("avacado", "green")]

# def hash_fn(string):
#     encoded = string.encode()
#     result = 0
#     for byte in encoded:
#         result+=byte
#     return result

# hash_list = [None] * 4

# hash_Value = (hash_fn("apple"))

# index_Value = hash_Value % len(hash_list)

# hash_list[index_Value] = ("apple","red")

# print(fruits)
# print(hash_list)

hash_list = [None] * len(fruits)
for fruit in fruits:
    key = fruit[0]
    value = fruit[1]
    def hash_fn(key):
        encoded = key.encode()
        result = 0
        for byte in encoded:
            result += byte
        return result
    hash_Value = (hash_fn(key))
    index_Value = hash_Value % len(hash_list)
    hash_list[index_Value] = (key, value)
print (hash_list)