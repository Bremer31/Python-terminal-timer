import threading
import time



def timer():
    hour = int(input("please enter the how many hours: "))
    minute = int(input("please enter how many minutes: "))
    seconds = int(input("please enter the seconds"))

    real_time = (hour * 3600) + (minute *60 ) + seconds
    if real_time >= 0:
     while real_time > 0:
        time.sleep(1)
        real_time = real_time - 1.0
        hourleft = int(real_time/3600)
        secondleft = int(real_time%60)
        minuteleft=int((real_time-hour*3600)/60)
        #print(real_time- hour*3600)
        print(f"{hourleft}:{minuteleft}:{secondleft}")
        

    
if __name__ == '__main__':
    try:
        timer()
    except KeyboardInterrupt:
        print("Exited[+]")
