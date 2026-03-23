"""Comprehensions are a concise way to create lists, sets, dictionaries, and generators in python using single line of code"""

tea_flavors = ["honey tea", "iced tea", "ginger tea", "iced lemon tea"]

iced_tea_flavors = [tea for tea in tea_flavors if "iced" in tea]
print(iced_tea_flavors)