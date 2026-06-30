class User:

    course = "Software Engineering 101"
    students = 0

    def __init__(self, email, username):
        self.email = email
        self.username = username
        self.isOnline = False
        User.students += 1
        pass

    # instance methods must have self as the first param.
    def login(self):
        self.isOnline = True
        print(f"{self.username} has logged in.")

    def get_profile(self):
        return f"User: {self.username} | Email: {self.email}"
    
    @classmethod
    def get_instance_count(cls):
        print(f"There are currently {cls.students} enrolled")

    @staticmethod
    def create(username, email):
        return User(email, username)
    

# Creating an instance from a class
user1 = User("eddie@gmail.com", "Eddie__")
user2 = User("karimi@yahoo.com", "Karimi_Yahoo")

user1.login()
user2.login()

print(user2.get_profile())
print(user1.get_profile())

print(User.course)
print(User.students)

user3 = User.create("a@b.com", "username")
print(User.students)
