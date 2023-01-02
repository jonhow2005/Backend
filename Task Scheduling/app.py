import schedule
from schedule import every, repeat
from plyer import notification
import time as tm
from datetime import time, timedelta, datetime

def testJob():
    print("Tested")


@repeat(every(5).seconds, message = "test")
def repeatjob(message):
    print("The message is: ", message)


#schedule.every(3).hours.do(testJob)

#schedule.every().day.at("18:00").do(testJob)

#schedule.every().minute.at(":40").do(testJob)

schedule.every().hour.until(time(11,23,43)).do(testJob)

#schedule.every().hour.until(timedelta(hours=8)).do(testJob)

jobvar1 = schedule.every(1).to(5).seconds.do(testJob)

counter = 0

while True:
    schedule.run_pending()
    tm.sleep
    counter += 1
    if counter == 10:
        schedule.cancel_job(jobvar1)