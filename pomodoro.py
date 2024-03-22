from tkinter import *
# https://www.youtube.com/watch?v=FpZ70RkUfNs
import math

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text = '00:00')
    title_label.config(text = 'Timer')

u
