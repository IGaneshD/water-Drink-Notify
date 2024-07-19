import time
from plyer import notification


if __name__=="__main__":
        while True:
            notification.notify(
            title="Hey Buddy!, Drink Water!",
            message="It's time to stay hydrated and drink some water. Daily Intake should be 3L",
            timeout=10,  # Notification stays for 10 seconds
            app_icon = "Iconsmind-Outline-Glass-Water.ico",
            )
            time.sleep(60*30)  # Notify every half hour

# to run this task in background use ' pythonw.exe main.py '