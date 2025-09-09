#WAP to enter 3 subject marks and add one by one in dictionary with subject name as a key
dictionary = {}
physics = int(input("enter physics marks"))
dictionary.update({"physics":physics})

chemistry = int(input("enter chemistry marks"))
dictionary.update({"chemisry":chemistry})

maths = int(input("enter maths marks:"))
dictionary.update({"maths":maths})

print(dictionary)