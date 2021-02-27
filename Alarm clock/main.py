from tkinter import *
import datetime
import time
import winsound

#Todo root Interface or GUI
root = Tk()
root.title("Alarm Clock")
root.geometry("600x600")
root.configure(bg='#808080')

#Todo The Variables we require to set the alarm(initialization):
hour = StringVar()
mint = StringVar()
sec = StringVar()

#Todo title
time_format = Label(root, text="Enter time in 24 hour format!", fg="yellow", bg="black", font=("Helevetica", 20, "bold"))
time_format.place(x=160, y=40)

addTime = Label(root, text="Hour \t Min  \t Sec", bg="gray", font=("Helevetica", 20, "bold"))
addTime.place(x=180, y=100)

#Todo Hour, Minutes, Secound
hourTime = Entry(root, textvariable=hour, bg="#ffffff", width=20, bd=6)
hourTime.place(x=180, y=140)
minTime = Entry(root, textvariable=mint, bg="#ffffff", width=20, bd=6)
minTime.place(x=280, y=140)
secTime = Entry(root, textvariable=sec, bg="#ffffff", width=12, bd=6)
secTime.place(x=400, y=140)

#Todo My Alaram
class MY_Alarm:
    def Alarm(Set_alarm_timer):
        while True:
            time.sleep(1)
            current_time = datetime.datetime.now()
            now = current_time.strftime("%H:%M:%S")
            date = current_time.strftime("%d/%m/%Y")
            print("The Set Date is:", date)
            print(now)
            if now == Set_alarm_timer:
                print("Time to Wake up")
            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
            break

#Todo Actual time
def Actual_time():
    Set_alarm_timer = f"{hour.get()}:{mint.get()}:{sec.get()}"
    MY_Alarm.Alarm(Set_alarm_timer)


#Todo main
if __name__ == '__main__':
    MY_Alarm
    Actual_time()
    submit = Button(root, text="Set Alarm", fg="#000000", bg="blue", bd=6,  font=("Helevetica", 12, "bold"), command=Actual_time)
    submit.place(x=300, y=200)

root.mainloop()
