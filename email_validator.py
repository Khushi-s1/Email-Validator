import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if re.match(pattern, email):
        return True
    else:
        return False

email1 = "khushi.soni.5339@gmail.com"
email2 = "khushi.soni_email.com"

print(is_valid_email(email1))
print(is_valid_email(email2))
