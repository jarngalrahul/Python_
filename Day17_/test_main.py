# Beginner OOP - Creating classes and objects
#              - Working with attributes, Class constructors and __init__() function
#              - Adding methods to a class


# Casings- Different style to name variables, functions, etc
# 1.  PascalCase
# 2.  camlCase
# 3.  snake_case
# Normally 1 and 3 are mostly used in python


class User:
    # use 'pass' keyword if you want to define something later(Meh~ I'll do it later 😒)
    # __init__() is a constructor, self is the object being initialised
    def __init__(self, user_id, username):
        print(f"Object {user_id} initialised.")
        self.id = user_id
        self.username = username
        self.default_attribute = 0
        self.followers = 0
        self.following = 0

    def follow(self, user):
        self.following += 1
        user.followers += 1


user_1 = User(1, "Mr. Hagemaru")
user_2 = User(2, "Mr. Hagemaru")

user_1.follow(user_2)
print(user_1.default_attribute)  # output: 0
print(user_1.following)
print(user_1.followers)
