import random, string

character=list(string.ascii_letters+string.digits+string.punctuation)
random.shuffle(character)

def password_generator():

    length=int(input('Please enter number of characters : '))

    password=[]

    for x in range(length):
        password.append(random.choice(character))
    
    password="".join(password)

    print(password)

    quit()

password_generator()
