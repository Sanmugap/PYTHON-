import re;
def text_match(text):
    patterns='^[a-zA-Z0-9_]*$'
    if re.search(patterns,text):
        return 'found a match!'
    else:
        return('not matched!')
def end_num(string):
    text=re.compile(r".*[0-9]$")
    if text.match(string):
        return "true"
    else:
        return "false"
def email_match(email):
    regex='^\w+([\-]?\\w+)*@\w+([\-]?\w+)*(\.\w{2,3})+$'
    if (re.search(regex,email)):
        return "valid email!"
    else:
        return ("not valid!")
inp=(str(input('Enter the string want to check:')))
print(text_match(inp))
inp=(str(input('Enter the string ended with number to check:')))
print(end_num(inp))
user_mail=input('Enter your email id:')
print(email_match(user_mail))
