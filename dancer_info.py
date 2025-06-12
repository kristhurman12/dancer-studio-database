def dancer_info():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    age = int(input("Enter age: "))

    full_name = first_name + " " + last_name

    print("\nDancer Info:")
    print("Name:", full_name)
    print("Age:", age)

    return {
        "name": full_name,
        "age": age
    }
dancer = dancer_info()