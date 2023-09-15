# Handles Notifications
from plyer import notification
from datetime import datetime

notification_title = "Greetings"
notification_message = "Hello World!"

def sendNotification(notification_title, notification_message):
    notification.notify(
        title = notification_title,
        message = notification_message,
        app_icon = None,
        timeout = 10,
        toast = False,
    )

print(datetime.now())