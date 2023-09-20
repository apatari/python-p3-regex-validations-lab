import re

# NOTE: There are only a few tests included, so multiple solutions will work.
# Feel free to encourage students to find oversights and add tests to this lab!

name = r"[A-Z][A-Za-z'-]+(\s[A-Z]\D*)*"
name_regex = re.compile(name)

phone_number = r"\d{10}|(\(*\d{3}\)*(\-|\s)?(\d{3}(\-|\s)*)?\d{4})"
phone_regex = re.compile(phone_number)

email_address = r"[a-z][a-z\d]*(\.[a-z\d]+)*@[a-z]+\.[a-z]+"
email_regex = re.compile(email_address)
