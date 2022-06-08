import string
import random

def randomWord(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for i in range(size))

def mailcopier(number, orginalmail, location):
    for x in range(int(number)):
        mail2 = orginalmail.replace("@gmail.com", "")
        mail = mail2 + "+" + randomWord() + "@gmail.com"
        file = open(location, "a")
        file.write(mail)
        file.write("\n")
        file.close()
    print("[+] Copied!")