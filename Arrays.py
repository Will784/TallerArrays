list_1d = ["Python", "Java", "C++", "JavaScript", "PHP"]
print("One-dimensional list")
print("Original list:", list_1d)
print()


list_2d = [
    ["Apple", "Pear", "Grape"],
    ["Dog", "Cat", "Parrot"],
    ["Red", "Green", "Blue"]
]
print("Two-dimensional list (3x3 matrix)")
for row in list_2d:
    print(row)
print()


second_element = list_1d[1]
print("Access to the second element")
print("Second element of the list (index 1):", second_element)
print()


element_row2col2 = list_2d[1][1]
print("Access to second row and second column")
print("Element at row 2, column 2 (indices [1][1]):")
print()


print("Insertion at position 3")
print("List before inserting:", list_1d)
list_1d.insert(2, "Estructura de datos")
print("List after inserting:", list_1d)
print()


print("Deletion at third row and third column")
print("Matrix before deleting:")
for row in list_2d:
    print(row)

deleted_element = list_2d[2][2]
list_2d[2][2] = None

print("\nDeleted element:", deleted_element)
print("\nMatrix after deleting:")
for row in list_2d:
    print(row)
print()


print("Search for 'Estructura de datos")
found_index = list_1d.index("Estructura de datos")
print(f"'Estructura de datos' is found at index: {found_index}")
print()


print("Search in the second row")
searched_value = "Cat"
second_row = list_2d[1]

found_column = second_row.index(searched_value)

print(f"Searched value: '{searched_value}'")
print("Row (position 2, index 1)")
print(f"Column found: position {found_column + 1}, index {found_column}")
print(f"Verified element: list_2d[1][{found_column}] = {list_2d[1][found_column]}")
