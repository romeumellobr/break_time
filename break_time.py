import webbrowser
import time

#set variables
loops = 3
counter = 0

#print time.ctime()
print("This program started on %s" % time.ctime())
while(counter < loops ):
    #Delay 10 seconds
    time.sleep(10)
    #Open Sara Niemietz YouTube Channel
    webbrowser.open("https://www.youtube.com/channel/UC9E6r0GuQ7d6G6esolVc5gg")
    counter = counter + 1
