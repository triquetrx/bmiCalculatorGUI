from tkinter import *
from tkinter import messagebox
def getHeight():
	height=float(ENTRY2.get())
	return height
def getWeight():
	weight=float(ENTRY1.get())
	return weight
def calculateBMI():
    try:
        h=getHeight()
        w=getWeight()
        h=h/100.0
        bmi=w//(h**2)
        strbmi=str(bmi)
    except ZeroDivisionError:
        messagebox.showerror("showerror","Enter a valid height")
    except ValueError:
        messagebox.showerror("showerror","Enter a valid data")
    else:
        if (bmi>=30.0):
            messagebox.showwarning("warning","You Fat Bitch your bmi is "+strbmi+"!!!")
        elif (25<=bmi<30):
            messagebox.showwarning("warning","You overweighted Fat ass, do eat a litte less your bmi is "+strbmi+"!!!")
        elif (18.5<=bmi<25):
            messagebox.showinfo("showinfo","You bmi is "+strbmi)
        else:
            messagebox.showwarning("warning","You waiting for a storm to take you away eat a little as your bmi is "+strbmi+" !!!")

if __name__=="__main__":
	TOP=Tk()
	TOP.bind("<Return>",calculateBMI)
	TOP.geometry("550x500")
	TOP.configure(background="#8c52ff")
	TOP.title("BMI Calculator")
	TOP.resizable(width=None, height=None)
	LABLE=Label(TOP,bg="#8c52ff",fg="#ffffff", text="BMI Calculator", font=("Helvetica",35,"bold"),padx=20)
	LABLE.place(x=100,y=0)
	LABLE1=Label(TOP,bg="#8c52ff",fg="#ffffff", text="Weight(Kgs)", font=("Helvetica",15,"bold"))
	LABLE1.place(x=55,y=100)
	ENTRY1=Entry(TOP,bg="#8c52ff",fg="#ffffff", font=("Helvetica",15,"bold"))
	ENTRY1.place(x=240,y=100)
	LABLE2=Label(TOP,bg="#8c52ff",fg="#ffffff", text="Height(cms)", font=("Helvetica",15,"bold"))
	LABLE2.place(x=55,y=161)
	ENTRY2=Entry(TOP,bg="#8c52ff",fg="#ffffff", font=("Helvetica",15,"bold"))
	ENTRY2.place(x=240,y=161)
	BUTTON=Button(bg="#000",fg="#ffffff",bd=12,text="Calculate",padx=43,pady=10,command=calculateBMI,font=("Helvetica",20,"bold"))
	BUTTON.grid(row=5,column=0,sticky=W)
	BUTTON.place(x=153,y=270)
	TOP.mainloop
