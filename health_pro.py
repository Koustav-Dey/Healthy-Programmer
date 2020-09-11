from time import time
import time
from pygame import mixer

print("============= Healthy Programmer============ ")
inp = input("   Hit Enter to Start Healty Programmer\n ")


print("\nWaiting ", end="")
list1 = [".", ".", ".", ".", ".", ".", ".", "."]
for i in (list1):

    print(f"{i}", end="")
    time.sleep(1)

init = time()
limit = 10800

if inp == "":

    def music(file, stopper):
        mixer.init()
        mixer.music.load(file)
        mixer.music.play()
        while True:
            a = input("\nIf You Want to Stop (Type : stop) : ")
            if a == stopper:
                mixer.music.stop()
                break

    def lognow(x):
        with open("health_pro.txt", "a") as f:
            f.write(f"\n{x} {datetime.now()}")
            f.close()

    from time import time
    from datetime import datetime
    water = time()
    eyes = time()
    activity = time()
    watersecs = 30*60
    eyessecs = 60*60
    activitysecs = 45*60

    while True:
        from time import time
        if time() - init > limit:
            print("\n\nTime is Over")
            exit(0)
        else:
            if time()-water > watersecs:
                print("\n\nDrinking water Time Sir !!")
                music("some.mp3", "stop")
                water = time()
                lognow("Drank Water at : ")

            if time()-eyes > eyessecs:
                print("\n\nClose Your Eyes Sir !!")
                music("Some.mp3", "stop")
                eyes = time()
                lognow("Eyes Excercise has been Completed at : ")

            if time()-activity > activitysecs:
                print("\n\nHand Excercise Time Sir !!")
                music("some.mp3", "stop")
                activity = time()
                lognow("Excercise has been Completed at : ")

else:
    print("Visit Again !!")
