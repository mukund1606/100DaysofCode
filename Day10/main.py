
# Classes are PascalCase -> FirstLetterOfEveryWordIsCapitalized
# Constructor -> part of the class that is called when you create an instance of the class
# Uses special function __init__(method)
# self -> refers to the instance of the class
class User:

    def __init__(self, user_id, username):
        # Attributes
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    # Methods
    def follow(self, user):
        user.followers += 1
        self.following += 1


# Create an instance of the class
user_1 = User(123, "johndoe")
user_2 = User(456, "jane")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
