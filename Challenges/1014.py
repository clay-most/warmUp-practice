random = {
  "cat": "bob",
  "dog": 23,
  19: 18,
  90: "fish"
}

result = 0 

for each in random.values():
    if type(each) == int:
        result += each
    
print(result)