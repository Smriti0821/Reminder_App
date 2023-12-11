from plyer import notification
import time  

notification_title = 'DRINK WATER'  
notification_message = 'Hey Smriti!!! Please drink water.'  

if __name__ == '__main__':
    while True:
        time.sleep(10)
        notification.notify(
            title = notification_title,  
            message = notification_message,  
            app_icon = "alert-bell-notification.ico",  
            timeout = 20,
            toast = True, 
        ) 