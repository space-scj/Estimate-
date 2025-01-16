import tkinter as tk
from tkinter import ttk
import sqlite3

conn=sqlite3.connect("mydata.db")

WIDTH = 800
HEIGHT = 600

rooms = []
selected = []

lf=12

class application(tk.Tk):
	def __init___(self):
		super().__init__()

class room():
	def __init__(self,x1,y1,x2,y2,name,length,width,height,color,rect,rectname):
		self.color = color
		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2
		self.name = name
		self.length = length
		self.width = width
		self.height = height
		self.rect = rect
		self.rectname = rectname


def get_count():
	i = 0
	for rom in range(len(rooms)):
		i+=1
	return i

class drawable():
	def __init__(self,toggle):
		self.toggle = toggle

	def toggle_draw(self,toggle):
		print(self.toggle)
		if self.toggle == True:
			self.toggle = False
			return self.toggle
		elif self.toggle == False:
			self.toggle = True
			return self.toggle
		
	def get_toggle(self,toggle):
		print(self.toggle)
		return toggle
		
draw = drawable(False)


	
def drawrect(event):
	if draw.get_toggle(draw.toggle) == True:
		count = get_count()
		x,y = event.x,event.y
		x1,y1, = x+(lf*12),y+(lf*12)
		rm = room(x,y,x1,y1,f"Room {count}",(x1-x)//12,(y1-y)//12,8,"white", [],"")
		name = f"Room {count}"
		rm.rect = canvas.create_rectangle(x,y,x1,y1,outline="blue",fill=rm.color)
		rm.rectname = canvas.create_text(x+(6*lf),y+(6*lf),text=name)
		rooms.append(rm)
		for rom in rooms:
			print(rom.name)
	else:
		for rm in rooms:
			if event.x > rm.x1 and event.x < rm.x2 and event.y > rm.y1 and event.y < rm.y2:
				if rm not in selected:
					selected.append(rm)
					print(rm)
					canvas.itemconfigure(rm.rect, fill="light grey")
					
					
			else:
				selected.remove(rm)
				rm.color = "white"
				canvas.itemconfigure(rm.rect,fill="white")
				
	
def deleteRoom(event):
	canvas.delete()

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
contain = tk.Frame()
contain.grid(column=0,row=2)
drawbt = tk.Button(text="Draw room")
drawbt.grid(column=0, row=2)
delbt= tk.Button(text="delete",command="deleteRoom")
delbt.grid(column=1,row=2)
drawbt.bind("<Button-1>",draw.toggle_draw)
canvas.bind("<Button-1>",drawrect)
canvas.bind("<Return>", deleteRoom)
canvas.update()



app.mainloop()
