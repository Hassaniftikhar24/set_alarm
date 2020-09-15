# Task: Write a python function to play a sound and print a message at a set time
# Inputs: Time to set the alarm, sound file to play, displaying the message


import sched
import winsound as wn
import time


def set_alarm_wakeup(time_alarm, file_alarm, message):
    s = sched.scheduler(time.time, time.sleep)
    s.enterabs(time_alarm, 1, print, argument=(message,))
    s.enterabs(file_alarm, 1, wn.PlaySound(), argument=(file_alarm, wn.SND_FILENAME))
    print('time set for :', time.asctime(time.localtime(time_alarm)))
    s.run()
