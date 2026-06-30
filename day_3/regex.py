import re

# request for data to be validated
username_to_test = str(input("What is the generated username? "))

# regex pattern to test (allow only alphanumeric and underscores)
username_pattern = r"^[\w_]+$"

# confirm patterns match
match_found = re.match(username_pattern, username_to_test)

# log results
if match_found:
    print("Username is valid")
else:
    print("Check your username and try again")


### TODO: Practice, Practice and more Practice