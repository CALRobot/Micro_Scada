import tkinter as tk

def create_clock_frame(parent):
    clock_frame = tk.LabelFrame(parent, text="Clock")
    clock_frame.pack(pady=10)
    timer_label = tk.Label(clock_frame, text="Timer: 500 ms")
    timer_label.pack()
    led_clock = tk.Canvas(clock_frame, width=30, height=30)
    led_clock.pack(side=tk.LEFT, padx=5)
    led_clock.led = led_clock.create_oval(5, 5, 25, 25, fill="gray")
    return led_clock
	