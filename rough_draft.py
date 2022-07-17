from threading import Thread
from time import sleep

STUDY_TIME = 1 # 1500 # 25 MIN
SHORT_BREAK = 1 # 300 # 5 MIN
LONG_BREAK = 1 # 1200 # 20 MIN

# THIS IS AN IDEA OF HOW WE WILL IMPLEMENT OUR BOT POMODORO
def main() :
    print("Running....")
    thread = Thread(target = pomodoro)
    thread.start()
    
    while(True) :
        sleep(1)
        print("Running")



def pomodoro() :
    for i in range(3) :
        print("Study")
        sleep(STUDY_TIME) # may need to change to work on mutible bots at once later...
        print("Break")
        sleep(SHORT_BREAK)
    
    print("Study")
    sleep(STUDY_TIME)
    print("Break")
    sleep(LONG_BREAK)
    print("Would you like to keep studying [y/n]: ")
    userInput = input()
    if userInput == 'y' : pomodoro()

main()