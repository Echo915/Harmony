import secrets, string 

from plyer import notification
# Secrets is a python library for creating random characters for secrets such as passwords.

def generatePassword():
    # Makes a list of all letters and digits using the string library
    characters = string.ascii_letters + string.digits
    while True:
        # Selects 10 random characters from the characters list and combines them into a single string (password)
        password = "".join(secrets.choice(characters) for i in range(10))
        # Checks that password contains at least one uppercase, one lowercase, and 3 digits
        if (any(c.islower() for c in password) and any(c.isupper() for c in password) and sum(c.isdigit() for c in password) >= 3):
            return password

notification_title = "Greetings"
notification_message = "Hello World!"

notification.notify(
    title = notification_title,
    message = notification_message,
    ticker = "hello world",
    app_icon = None,
    app_name = "Harmony",
    timeout = 10,
    toast = False,
)
