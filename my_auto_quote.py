from tkinter import * 
from requests import *
from time import * 

root = Tk()
root.title("Quote app by harsh sir")
root.geometry("700x300+50+50")
f = ("times new roman", 30, "bold")


def gq():
	try:
		wa = "https://zenquotes.io/api/random"
		res = get(wa)
		data = res.json()
		quote = data[0]['q']
		lab_msg.configure(text=quote)
		root.after(5000, gq)
	except Exception as e:
		print("issue ", e)

lab_msg = Label(root, font=f, wraplength=400)
lab_msg.pack(pady=10)

gq()

root.mainloop()