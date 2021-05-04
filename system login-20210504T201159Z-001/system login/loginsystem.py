global dict_user = []

def input_password():
    Password = input('Enter your password: ')
    return Password

def input_user():
    Username = input('Enter the Username: ')
    return Username

def printing_invalid(invalid):
    print("Invalid {}".format(invalid))

def checking_user(Username,Password,dict_user):
    if (Username,Password) in dict_user:
        print('valid')
        return False
    else:
        print('invalid')
        return True

def check(Username,Password,true_false,dict_user):
    while true_false:
        true_false = checking_user(Username,Password,dict_user)
        if true_false:
            Username = input_user()
            Password = input_password()

def validation_password(create_username,create_password):
    for x in create_password:
        if not x.isalnum():
            printing_invalid(create_password)
            create_password = input_password()
            validation_password(create_username,create_password)
            return 0
        continue
    dict_user.append((create_username,create_password))
    print("created")

def validation_username(create_username):
    if '@' in create_username:
        list_validation_username = create_username.split('@')
        if list_validation_username[0].isalnum():
            create_password = input('Create your password')
            validation_password(create_username,create_password)
        else:
            printing_invalid(create_username)
            create_username = input_user()
            validation_username(create_username)

    else:
        printing_invalid(create_username)
        create_username = input_user()
        validation_username(create_username)

def main_program():
    yes_no = input('Do you already exist or not,press y/n: ')
    yes_no = yes_no.lower()
    true_false = True
    if yes_no == 'y':
        Username = input_user()
        Password = input_password()
        check(Username,Password,true_false,dict_user)
    else : 
        create_username = input('Create you username: ')
        validation_username(create_username)

main_program()
