import time
import os

def countdown_timer(minutes):
    seconds = minutes * 60
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1

    print('Time is up!')
    # 播放提示音
    os.system('say "Time is up!"')

# 使用方式
countdown_timer(25) # 倒数25分钟
