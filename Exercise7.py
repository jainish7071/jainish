#  Healthy programmer
# 9am - 5am
# Water - water.mp3  (3.5liters)  - Drank - log
# Eyes - eye.mp3 -every 30min - EyDone - log
# Physical activity - physical.mp3 - every 45min - ExDone

#rules - use pygame module to play audio

import time
from pygame import mixer

def playWater():
    mixer.init()
    mixer.music.load("Water.mp3")
    mixer.music.play(100)
    if(input("Enter \"Drank\" if you drank the one glass of water").capitalize()=="Drank"):
        mixer.music.stop()
        with open("Water.txt", "a") as f:
            f.write(f"You Drank Water at -----> {time.asctime(time.localtime(time.time()))}")
        return
    time.sleep(120)
def playEyes():
    mixer.init()
    mixer.music.load("Eyes.mp3")
    mixer.music.play(100)
    if(input("Enter \"Eydone\" if you done with your eye movment").capitalize()=="Eydone"):
        mixer.music.stop()
        with open("EyExercise.txt", "a") as f:
            f.write(f"the Exercise is done at -----> {time.asctime(time.localtime(time.time()))}")
        return
    time.sleep(120)
def playPhysical():
    mixer.init()
    mixer.music.load("Physical.mp3")
    mixer.music.play(100)
    if(input("Enter \"Exdone\" if you done with your physical Exercise").capitalize()=="Exdone"):
        mixer.music.stop()
        with open("PhysicalExercise.txt","a") as f:
            f.write(f"Physical Exercise is done at -----> {time.asctime(time.localtime(time.time()))}")
        return
    time.sleep(120)

while(True):
    AM9TIME_Water = 540
    AM9TIME_Eye = 540
    AM9TIME_Phy = 540
    AllDayTime = time.localtime(time.time()).tm_hour
    while(AllDayTime>=9 and AllDayTime<=17):
        AllDayTime = time.localtime(time.time()).tm_hour
        TIME = time.localtime(time.time())
        TimeInMinut = TIME.tm_hour*60 + TIME.tm_min
        WaterTime = TimeInMinut - AM9TIME_Water
        EyeTime = TimeInMinut - AM9TIME_Eye
        PhysicalTime = TimeInMinut - AM9TIME_Phy
        WCondition = (WaterTime==25.00)
        EyCondition = (EyeTime==30.00)
        ExCondition = (PhysicalTime==45.00)
        if(WCondition):
            playWater()
            AM9TIME_Water = TimeInMinut
        if(EyCondition):
            playEyes()
            AM9TIME_Eye = TimeInMinut
        if(ExCondition):
            playPhysical()
            AM9TIME_Phy = TimeInMinut


