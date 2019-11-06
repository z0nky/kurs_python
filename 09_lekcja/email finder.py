def emailfinder():
    if email.find('@') == -1:
        return ('Email should include "@".')
    else:
        try:
            emaillist.index(email)
            return (email, 'is on the list')
        except ValueError:
            return ('Email not found.')

email = input('Enter emain you want to find: ')
emaillist = ['abc@gmail.com', 'xyz@gmail']
print(emailfinder())
