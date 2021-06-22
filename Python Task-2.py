"""
A bank has implemented criteria for determining whether the transaction passwords typed by customers of the bank are valid or not.

The following are the criteria for checking the transaction password:

1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
3. At least 1 letter between [A-Z]
4. At least 1 character from [*#+@]
5. Minimum length of transaction password: 4
6. Maximum length of transaction password: 6
7. No space is allowed

Write a program that will accept a sequence of comma-separated transaction passwords and will check them according to the bank's criteria. Passwords that match the criteria
are to be printed, each separated by a comma.

"""


def password(raw_input):
    raw_split = raw_input.split(',')
    raw_filter = []
    raw_result = ''
    for i in raw_split:
        if 4 <= len(i) <= 6 and (' ' not in i):
            raw_filter.append(i)
    for f in raw_filter:
        raw_result += f + ','
    return raw_result[:-1]


print(password('Abc@1,a B1#,2w3E*,2We#3345'))
