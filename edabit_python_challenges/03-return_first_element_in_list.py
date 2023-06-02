def return_first_element_in_list(list_of_numbers):
    if isinstance(list_of_numbers, list):
        if list_of_numbers:
            return list_of_numbers[0]
        else:
            print("That list is empty!")
    else:
        print("Error: Input is not a list of numbers!")

print("The next line should say 1")
list_of_numbers = [1, 2, 3]
print(return_first_element_in_list(list_of_numbers))
print("The next line should say 'That list is empty!")
list_of_numbers = []
print(return_first_element_in_list(list_of_numbers))