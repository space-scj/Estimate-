import tkinter as tk
from tkinter import ttk
import sqlite3

conn=sqlite3.connect("mydata.db")

WIDTH = 800
HEIGHT = 600

rooms = []


lf=12

class application(tk.Tk):
	def __init___(self):
		super().__init__()

class room():
	def __init__(self,x1,y1,x2,y2,name,length,width,height):
		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2
		self.name = name
		self.length = length
		self.width = width
		self.height = height

def get_count():
	i = 0
	for rom in range(len(rooms)):
		i+=1
	return i
		
	
def drawrect(event):
	count = get_count()
	x,y = event.x,event.y
	x1,y1, = x+(lf*12),y+(lf*12)
	rm = room(x,y,x1,y1,f"Room {count}",(x1-x)//12,(y1-y)//12,8)
	name = f"Room {count}"
	canvas.create_rectangle(x,y,x1,y1,outline="blue")
	canvas.create_text(x+(6*lf),y+(6*lf),text=name)
	rooms.append(rm)
	for rom in rooms:
		print(rom.name)

def dragdraw(event):
	
	
	 
app = application()
app.title("Estimate+")
app.grid_rowconfigure(1,weight=1)
app.grid_columnconfigure(1,weight=1)
app.geometry(f"{WIDTH}x{HEIGHT}")
lblit = tk.Label(text="Estimate item")
lblit.grid(column=0,row=0)
itemsel = tk.Listbox()
itemsel.grid(column=0,row=1,sticky="nsew")
canvas = tk.Canvas(background="white")
canvas.grid(column=1,row=1,sticky="nsew")

canvas.bind("<Button-1>",drawrect)




app.mainloop()

