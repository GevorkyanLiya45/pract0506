import tkinter as tk

running = False
hours, minutes, seconds, milliseconds = 0, 0, 0, 0

def update_time():
    global running, hours, minutes, seconds, milliseconds
    if running:

        milliseconds += 1
        
        if milliseconds >= 100:
            milliseconds = 0
            seconds += 1
            
        if seconds >= 60:
            seconds = 0
            minutes += 1
            
        if minutes >= 60:
            minutes = 0
            hours += 1

        time_string = f"{hours:02d}:{minutes:02d}:{seconds:02d}:{milliseconds:02d}"
        label_time.config(text=time_string)
        
        root.after(10, update_time)

def start():
    global running
    if not running:
        running = True
        update_time()

def pause():
    global running
    running = False

def reset():
    global running, hours, minutes, seconds, milliseconds
    running = False
    hours, minutes, seconds, milliseconds = 0, 0, 0, 0
    label_time.config(text="00:00:00:00")

root = tk.Tk()
root.title("Секундомер")
root.geometry("350x180")
root.resizable(False, False) 

label_time = tk.Label(root, text="00:00:00:00", font=("Courier New", 32, "bold"), fg="#1A237E")
label_time.pack(pady=25)

frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

btn_start = tk.Button(frame_buttons, text="Старт", command=start, bg="#4CAF50", fg="white", font=("Arial", 11, "bold"), width=9)
btn_start.grid(row=0, column=0, padx=8)

btn_pause = tk.Button(frame_buttons, text="Пауза", command=pause, bg="#FF9800", fg="white", font=("Arial", 11, "bold"), width=9)
btn_pause.grid(row=0, column=1, padx=8)

btn_reset = tk.Button(frame_buttons, text="Сброс", command=reset, bg="#F44336", fg="white", font=("Arial", 11, "bold"), width=9)
btn_reset.grid(row=0, column=2, padx=8)

root.mainloop()