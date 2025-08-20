while True:
    try:
        password = input("Please enter the password: ")    
        assert len(password) >=8
        print("Valid password!!!")
        break
    except AssertionError:
        print("Invalid Password, please try again")
