import tkinter as tk
from datetime import datetime, timedelta

running = False
start_time = None
accumulated_time = timedelta()


def start():
    global running, start_time

    if not running:
        start_time = datetime.now()
        running = True
        update()
        print(f'Stopwatch started at: {start_time}')

def stop():
    global running, start_time, accumulated_time

    if running:
        stop_time = datetime.now()
        accumulated_time += (stop_time - start_time)
        running = False
        print(f'Total time: {accumulated_time}')

def reset():
    global running, start_time, accumulated_time

    if running:
        running = False
    start_time = None
    accumulated_time = timedelta()
    timer.config(text='00:00:00')

def update():
    global running, start_time, accumulated_time

    if running:
        real_time = ((datetime.now() - start_time)+accumulated_time)
        # El objetivo de esta parte (linea 33 a 37) era mostrar 2 decimales de los ms, pero cuando los ms eran 00, el '.' desaparecía y el split() moría al no haber un indice [1], entonces para poder manejar correctamente los ms, tuve que hacer una condicional que haga que cuando los ms fueran 00 (linea 36), agregabamos un string '.00' para que el '.' no desaparezca.
        texto_parts = str(real_time).split('.') 
        if len(texto_parts) == 2:
            texto = (texto_parts[0]+'.'+texto_parts[1][:2])
        else:
            texto = texto_parts[0]+'.00'
        timer.config(text=texto)
        stopwatch.after(50, update)

stopwatch = tk.Tk()
stopwatch.title('Goofy Ahh Stopwatch')

title = tk.Label(stopwatch, text='STOPWATCH OWO')
title.pack()

timer = tk.Label(stopwatch, text='00:00:00', font=('Arial', 40))
timer.pack()

start_button = tk.Button(stopwatch, text='START', command=start)
start_button.pack()

stop_button = tk.Button(stopwatch, text='STOP', command=stop)
stop_button.pack()

reset_button = tk.Button(stopwatch, text='RESET', command=reset)
reset_button.pack()

stopwatch.mainloop()
