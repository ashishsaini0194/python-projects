from tkinter import *
root = Tk()
root.geometry("600x600")
root.title("Calculator by Ashish saini")
scvalue = StringVar()
scvalue.set("")
entry = Entry(root,textvar=scvalue,font=("lucida 20 bold"),fg = "blue",borderwidth = "5")
entry.pack(fill = X)


#functions
        
def press(self):
    global scvalue
    text=self.widget.cget("text")#self.widget will give the button that pressed and .cget will take value from that button
    value = 0
    print(scvalue.get())
    
    if text == "=":
        try:
            value=str(eval(scvalue.get()))
        except:
            pass
        finally:
            value.replace("=","")
            value=int(value)
            scvalue.set(value)
        
    if text == "C":
        scvalue.set("")
        #screen.update()
        
    else:
        scvalue.set(scvalue.get()+ str(text))
        #screen.update()

b= Button(text = 9,font=("lucida 20 bold"),fg ="black",borderwidth = "8",relief= RIDGE,padx = "10")
b.place(x="150",y="40")
b.bind("<Button-1>",press)#to bind this key
b= Button(text = 8,font=("lucida 20 bold"),fg ="black",borderwidth = "8",relief= RIDGE,padx = "10")
b.place(x="250",y="40")
b.bind("<Button-1>",press)#to bind this key
b= Button(text = 7,font=("lucida 20 bold"),fg ="black",borderwidth = "8",relief= RIDGE,padx = "10")
b.place(x="350",y="40")
b.bind("<Button-1>",press)#to bind this key

b= Button(text = 6,font=("lucida 20 bold"),fg ="black",borderwidth = "8",relief= RIDGE,padx = "10")
b.place(x="150",y="140")
b.bind("<Button-1>",press)#to bind this key
b= Button(text = 5,font=("lucida 20 bold"),fg ="black",borderwidth = "8",relief= RIDGE,padx = "10")
b.place(x="250",y="140")
b.bind("<Button-1>",press)#to bind this key
b= Button(text = 4,font=("lucida 20 bold"),fg ="black",borderwidth = "8",relief= RIDGE,padx = "10")
b.place(x="350",y="140")
b.bind("<Button-1>",press)#to bind this key

b= Button(text = 3,font=("lucida 20 bold"),fg ="black",borderwidth = "8",relief= RIDGE,padx = "10")
b.place(x="150",y="240")
b.bind("<Button-1>",press)#to bind this key
b= Button(text = 2,font=("lucida 20 bold"),fg ="black",borderwidth = "8",relief= RIDGE,padx = "10")
b.place(x="250",y="240")
b.bind("<Button-1>",press)#to bind this key
b= Button(text = 1,font=("lucida 20 bold"),fg ="black",borderwidth = "8",relief= RIDGE,padx = "10")
b.place(x="350",y="240")
b.bind("<Button-1>",press)#to bind this key

b= Button(text = "+",font=("lucida 20 bold"),fg ="black",borderwidth = "8",relief= RIDGE,padx = "10")
b.place(x="150",y="340")
b.bind("<Button-1>",press)#to bind this key
b= Button(text = "-",font=("lucida 20 bold"),fg ="black",borderwidth = "8",relief= RIDGE,padx = "10")
b.place(x="250",y="340")
b.bind("<Button-1>",press)#to bind this key
b= Button(text = "=",font=("lucida 20 bold"),fg ="black",borderwidth = "8",relief= RIDGE,padx = "10")
b.place(x="350",y="340")
b.bind("<Button-1>",press)#to bind this key

b= Button(text = "/",font=("lucida 20 bold"),fg ="black",borderwidth = "8",relief= RIDGE,padx = "10")
b.place(x="150",y="440")
b.bind("<Button-1>",press)#to bind this key
b= Button(text = "*",font=("lucida 20 bold"),fg ="black",borderwidth = "8",relief= RIDGE,padx = "10")
b.place(x="250",y="440")
b.bind("<Button-1>",press)#to bind this key
b= Button(text = "%",font=("lucida 20 bold"),fg ="black",borderwidth = "8",relief= RIDGE,padx = "10")
b.place(x="350",y="440")
b.bind("<Button-1>",press)#to bind this key

b= Button(text = "(",font=("lucida 20 bold"),fg ="black",borderwidth = "8",relief= RIDGE,padx = "10")
b.place(x="150",y="540")
b.bind("<Button-1>",press)#to bind this key
b= Button(text = ")",font=("lucida 20 bold"),fg ="black",borderwidth = "8",relief= RIDGE,padx = "10")
b.place(x="250",y="540")
b.bind("<Button-1>",press)#to bind this key
b= Button(text = "C",font=("lucida 20 bold"),fg ="black",borderwidth = "8",relief= RIDGE,padx = "10")
b.place(x="350",y="540")
b.bind("<Button-1>",press)#to bind this key

root.mainloop()
