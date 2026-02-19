class User():
    def __init__(self, user_identifier, name, email, password):
        self.id = user_identifier
        self.name = name
        self.email = email
        self.password = password

users = {
    "example_user_1": User("example_user_1", "John Doe", "example@example.com", "secretpassword"),
    "example_user_2": User("example_user_2", "Jane Doe", "example2@example.com", "secretpassword2")
    }


#This for loop shows how to loop through the values of users dictionary(User objects) and print their names(values of name properties).
print("Names of user objects in the users dictionary: ")
for i in users.values():
    print(i.name)

#This is a list comprehension that check the values of users dictionary(User objects) and print email(value of email property).
print("Email that you are look for: ")
x = [i for i in users.values() if i.email == "example2@example.com"]
print(x[0].email)

# This is a generator expression. It iterates over Values in users dictionary and checks if "email" property is equal to the given one.
# Afterward it gives back the user instance.
user = next((i for i in users.values() if i.email == "example2@example.com"), None)
print(f"The name of user you look for with this email addres is: {user.name}")