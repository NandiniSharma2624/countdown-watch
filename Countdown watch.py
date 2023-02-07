import tkinter as tk
running = False
hours= 0
seconds = 0
minutes = 0
#stp = 0
#funtion for start the countdown
def start():
  global running
  if not running:
    update()
    running = True
'''
#funtion for stop the countdown
def stop():
    global stp
    stp = 1
'''
#funtion for pause the countdown
def pause():
  global running
  if running:
    countdown_label.after_cancel(update_time)
    running = False

#funtion for reset the countdown
def reset():
  global running
  if running:
    countdown_label.after_cancel(update_time)
    running= False
  #reseting variables to 0
  global hours , minutes , seconds 
  hours = 0
  minutes = 0
  seconds = 0
  countdown_label.config(text='00.00.00')

#funtion for update the countdown
def update():
  global hours , minutes , seconds 
  seconds += 1
  if seconds == 60:
    minutes +=1
    seconds = 0
  if minutes == 60:
    hours += 1
    minutes = 0
  hours_string = f'{hours}' if hours > 9 else f'0{hours}'
  minutes_string = f'{minutes}' if minutes > 9 else f'0{minutes}' 
  seconds_string = f'{seconds}' if seconds > 9 else f'0{seconds}'
  countdown_label.config(text=hours_string + ':' + minutes_string + ':' + seconds_string)
  global update_time
  update_time = countdown_label.after(1000, update)

# Code for the window of the countdown
top = tk.Tk()
top.geometry('485x220') # geometry used to size the window
top.title('Countdown_Watch') #for providing the title 

#label to displaying the time on window
countdown_label = tk.Label(text='00.00.00', font=('Rosewood Std Fill',80))
countdown_label.pack()

#for the buttons(start, stop, reset, pause) on the window
Start_button = tk.Button(text='Start', height=5, width=7, font=('Rosewood Std Fill',20), command=start , bg='green')
Start_button.pack(side=tk.LEFT)
Pause_button = tk.Button(text='Pause', height=5, width=7, font=('Rosewood Std Fill',20), command=pause , bg='yellow')
Pause_button.pack(side=tk.LEFT)
Reset_button = tk.Button(text='Reset', height=5, width=7, font=('Rosewood Std Fill',20), command=reset , bg='blue')
Reset_button.pack(side=tk.LEFT)
Stop_button = tk.Button(text='Stop', height=5, width=7, font=('Rosewood Std Fill',20), command=top.quit , bg='red')
Stop_button.pack(side=tk.LEFT)
top.mainloop()
