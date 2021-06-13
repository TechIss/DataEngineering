import time
import schedule

def alarm():
    print("Biep!")

schedule.every().minute.at(':01').do(alarm)

while True:
    schedule.run_pending()
    time.sleep(1)
    