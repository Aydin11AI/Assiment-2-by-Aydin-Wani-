#Q6. Write a program in python to create a dictionary of 10 elements and delete item using popitems() function ?s
my_dictionary = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10
}

print("Original dictionary:", my_dictionary)

# Delete items using popitem()
print("\nDeleting items using popitem():")
for _ in range(3):  # Let's delete 3 items
    if my_dictionary:
        removed_item = my_dictionary.popitem()
        print(f"Removed item: {removed_item}")
        print("Updated dictionary:", my_dictionary)
    else:
        print("Dictionary is now empty, cannot pop more items.")
        break

print("\nFinal dictionary:", my_dictionary)

