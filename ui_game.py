import sys
import tkinter as tk
from dal_game import *
from tkinter import messagebox
from tkinter import Tk, DISABLED
import random 
#from PIL import Image, ImageTk

root=Tk()
root.title("master and minor")
root.geometry("440x440")
root.configure(bg="#31112c")
root.minsize(440, 440)
root.maxsize(440,440)
p1 = PhotoImage(file = r'C:\Users\negin\Downloads/98.png')
root.iconphoto(False, p1)

#region SHOWFRAME
def show_frame2():
    frame1.grid_forget()
    frame2.grid(row=0,column=0, columnspan=2,rowspan=2,ipadx=50,padx=(1,5),pady=(1,9),ipady=40)

def show_frame1(name,family,username,password):
    if name=="" or family=="" or username=="" or password=="":
        messagebox.showerror("ERROR","empty !!")
    else:
        if not savedata(name,family,username,password):
            messagebox.showerror("ERROR","account receantly added!!")
            return
        frame2.grid_forget()
        frame1.grid(row=0,column=0,columnspan=2,rowspan=2,ipadx=10,padx=(1,5),pady=(1,8),ipady=25)
def show_frame3():
    frame1.grid_forget()
    frame3.grid(row=0,column=0,columnspan=2,rowspan=2,ipadx=30,padx=(1,10),pady=(1,40),ipady=40)
def back2():
    frame9.grid_forget()
    frame8.grid_forget()
    frame7.grid_forget()
    frame6.grid_forget()
    frame5.grid_forget()
    frame4.grid_forget()
    frame3.grid(row=0,column=0,columnspan=2,rowspan=2,ipadx=30,padx=(1,10),pady=(1,40),ipady=40)
def back1():
    frame2.grid_forget()
    frame3.grid_forget()
    frame1.grid(row=0,column=0,columnspan=2,rowspan=2,ipadx=10,padx=(1,5),pady=(1,8),ipady=25)
   
def show_winroot():
    winroot = Toplevel() 
    winroot.geometry("300x320")
    winroot.title("Winning")
    winroot.configure(bg="#fe6878")
    canvas = Canvas(winroot,width=300,height=250)
    canvas.pack()
    img =PhotoImage(file=r"C:\Users\negin\Desktop\pro1.png")
    canvas.create_image(5,5,anchor=NW,image=img)
    button1 = Button( winroot, text = "OK",bg="#fe9ba5", command= winroot.destroy)
    button1.pack(side=BOTTOM, expand=True,fill=BOTH)
    # button1.place(x=120,y=270,width=60,height=30)
    # label1 = Label( winroot, text = "winner",bg="#fe6878")
    # label1.config(font=("Papyrus", 40))
    # label1.place(x=10,y=90,width=290)
    winroot.mainloop()
#endregion   

#region SHOW LEVEL   
def show_level4():
    frame3.grid_forget()
    frame4.grid(row=0,column=0,columnspan=2,rowspan=2,ipadx=10,padx=(1,5),pady=(1,10),ipady=160)
def show_level5():
    frame3.grid_forget()
    frame5.grid(row=0,column=0,columnspan=2,rowspan=2,ipadx=90,padx=(1,5),pady=(1,10),ipady=160)
def show_level6():
    frame3.grid_forget()
    frame6.grid(row=0,column=0,columnspan=2,rowspan=2,ipadx=90,padx=(1,5),pady=(1,10),ipady=160)
def show_level7():
    frame3.grid_forget()
    frame7.grid(row=0,column=0,columnspan=2,rowspan=2,ipadx=90,padx=(1,5),pady=(1,10),ipady=160)
def show_level8():
    frame3.grid_forget()
    frame8.grid(row=0,column=0,columnspan=2,rowspan=2,ipadx=90,padx=(1,5),pady=(1,10),ipady=160)
def show_level9():
    frame3.grid_forget()
    frame9.grid(row=0,column=0,columnspan=2,rowspan=2,ipadx=90,padx=(1,5),pady=(1,10),ipady=160)
#endregion    

def check(username,password):
    try:
             
        connection = sqlite3.connect("account.db")
        cursor = connection.cursor()

        query = """
        SELECT username,password
        FROM accountlist;
        """
       
        cursor.execute(query)
        result = cursor.fetchall()
        check_tuple = (username,password)
        cursor.close()
    except sqlite3.Error as err:
        print("err")
    else:
        if check_tuple in result:
            show_frame3()
        else:
           messagebox.showerror("ERROR!!","user Not found")  
    finally:
        if connection:
            connection.close()
            
#region LEVEL4           
pc_number = random.randint(1000,9999)  
print(pc_number)
def play(digit1,digit2,digit3,digit4,pc_num):
    member_number = digit1+digit2+digit3+digit4
    pc_digit_list = [str(d) for d in str(pc_num)]
    if digit1== pc_digit_list[0]:
        en_4_1.config(state=DISABLED)
        en_4_1.configure({"disabledbackground": "#D6FA8C"})
    if digit1!=pc_digit_list[0]:
        en_4_1.config(bg="#FF6962")
    if digit2== str(pc_digit_list[1]):
        en_4_2.config(state=DISABLED)
        en_4_2.configure({"disabledbackground": "#D6FA8C"})
    if digit2!=pc_digit_list[1]:
        en_4_2.config(bg="#FF6962")
    if digit3== str(pc_digit_list[2]):
        en_4_3.config(state=DISABLED)
        en_4_3.configure({"disabledbackground": "#D6FA8C"})
    if digit3!=pc_digit_list[2]:
        en_4_3.config(bg="#FF6962")
    if digit4== str(pc_digit_list[3]):
        en_4_4.config(state=DISABLED)
        en_4_4.configure({"disabledbackground": "#D6FA8C"})
    if digit4!=pc_digit_list[3]:
        en_4_4.config(bg="#FF6962")
        
    if "".join(pc_digit_list)==member_number:   
        show_winroot()
        
frame4 = Frame(root)
frame4.configure(bg="#FFFAB6")
lbl_guess = Label(frame4, text="guess number with 4 digit :" )
lbl_guess.config(font=("Papyrus", 14))
lbl_guess.configure(bg="#FFFAB6",fg="#F05F00")
lbl_guess.grid(row=1,column=1,columnspan=2,pady=(40,50),padx=40)
d41 = StringVar
d42 = StringVar
d43 = StringVar
d44 = StringVar
en_4_1 = Entry(frame4, textvariable= d41,width=5)
en_4_1.grid(row=5,column=0,ipady=20,pady=40,padx=(80,8),ipadx=5,columnspan=2)
en_4_2 = Entry(frame4,textvariable= d42,width=5)
en_4_2.grid(row=5,column=1,ipady=20,pady=40,padx=(5,3),ipadx=5,columnspan=3)
en_4_3 = Entry(frame4,textvariable= d43,width=5)
en_4_3.grid(row=5,column=2,ipady=20,pady=40,padx=(5,3),ipadx=5,columnspan=2)
en_4_4 = Entry(frame4,textvariable= d44,width=5)
en_4_4.grid(row=5,column=3,ipady=20,pady=40,padx=(5,80),ipadx=5,columnspan=2)
bt_play = Button(
                    frame4,
                    text="Play",
                    width=30,
                    command= lambda:play(
                                            digit1 = en_4_1.get(),
                                            digit2 = en_4_2.get(),
                                            digit3 = en_4_3.get(),
                                            digit4 = en_4_4.get(),
                                            pc_num = pc_number
                                        )
            )
bt_play.configure(bg="#FFB346")
bt_play.grid(row=7,column=1,columnspan=3,pady=10,ipady=10,padx=(80,10))
bt_back2 = Button(frame4, text="BACK", width=5,command= back2)
bt_back2.configure(bg="#ffcc5c")
bt_back2.place(x=380,y=5)
#endregion
  
#region LEVEL5
pc_number5 = random.randint(10000,99999)  
print(pc_number5)
def play5(digit1,digit2,digit3,digit4,digit5,pc_num):
    member_number = digit1+digit2+digit3+digit4+digit5
    pc_digit_list = [str(d) for d in str(pc_num)]
    if digit1== pc_digit_list[0]:
        en_5_1.config(state=DISABLED)
        en_5_1.configure({"disabledbackground": "#D6FA8C"})
    if digit1!=pc_digit_list[0]:
        en_5_1.config(bg="#FF6962")
    if digit2== str(pc_digit_list[1]):
        en_5_2.config(state=DISABLED)
        en_5_2.configure({"disabledbackground": "#D6FA8C"})
    if digit2!=pc_digit_list[1]:
        en_5_2.config(bg="#FF6962")
    if digit3== str(pc_digit_list[2]):
        en_5_3.config(state=DISABLED)
        en_5_3.configure({"disabledbackground": "#D6FA8C"})
    if digit3!=pc_digit_list[2]:
        en_5_3.config(bg="#FF6962")
    if digit4== str(pc_digit_list[3]):
        en_5_4.config(state=DISABLED)
        en_5_4.configure({"disabledbackground": "#D6FA8C"})
    if digit4!=pc_digit_list[3]:
        en_5_4.config(bg="#FF6962")
    if digit5== str(pc_digit_list[4]):
        en_5_5.config(state=DISABLED)
        en_5_5.configure({"disabledbackground": "#D6FA8C"})
    if digit5!=pc_digit_list[4]:
        en_5_5.config(bg="#FF6962")    
    if "".join(pc_digit_list)==member_number:
        show_winroot()
        
frame5 = Frame(root) 
frame5.configure(bg="#FFFAB6")
lbl_guess = Label(frame5, text="guess number with 5 digit :" )
lbl_guess.config(font=("Papyrus", 14))
lbl_guess.configure(bg="#FFFAB6",fg="#F05F00")
lbl_guess.grid(row=1,column=1,columnspan=2,pady=(40,50),padx=40)
d51 = StringVar
d52 = StringVar
d53 = StringVar
d54 = StringVar
d55 = StringVar
en_5_1 = Entry(frame5, textvariable= d51)
en_5_1.place(x=100,y=167,width=42,height=58)
en_5_2 = Entry(frame5,textvariable= d52,width=5)
en_5_2.place(x=150,y=167,width=42,height=58)
en_5_3 = Entry(frame5,textvariable= d53,width=5)
en_5_3.place(x=200,y=167,width=42,height=58)
en_5_4 = Entry(frame5,textvariable= d54,width=5)
en_5_4.place(x=250,y=167,width=42,height=58)
en_5_5 = Entry(frame5,textvariable= d55,width=5)
en_5_5.place(x=300,y=167,width=42,height=58)
bt_play5 = Button(
                    frame5,
                    text="Play",
                    width=30,
                    command= lambda:play5(
                                            digit1 = en_5_1.get(),
                                            digit2 = en_5_2.get(),
                                            digit3 = en_5_3.get(),
                                            digit4 = en_5_4.get(),
                                            digit5 = en_5_5.get(),
                                            pc_num = pc_number5
                                        )
            )
bt_play5.place(x=120,y=270,width=200,height=45)
bt_play5.configure(bg="#FFB346")
bt_back2 = Button(frame5, text="BACK", width=5,command= back2)
bt_back2.configure(bg="#ffcc5c")
bt_back2.place(x=380,y=5)
#endregion

#region LEVEL6
pc_number6 = random.randint(100000,999999)  
print(pc_number6)
def play6(digit1,digit2,digit3,digit4,digit5,digit6,pc_num):
    member_number = digit1+digit2+digit3+digit4+digit5+digit6
    pc_digit_list = [str(d) for d in str(pc_num)]
    if digit1== pc_digit_list[0]:
        en_6_1.config(state=DISABLED)
        en_6_1.configure({"disabledbackground": "#D6FA8C"})
    if digit1!=pc_digit_list[0]:
        en_6_1.config(bg="#FF6962")
    if digit2== str(pc_digit_list[1]):
        en_6_2.config(state=DISABLED)
        en_6_2.configure({"disabledbackground": "#D6FA8C"})
    if digit2!=pc_digit_list[1]:
        en_6_2.config(bg="#FF6962")
    if digit3== str(pc_digit_list[2]):
        en_6_3.config(state=DISABLED)
        en_6_3.configure({"disabledbackground": "#D6FA8C"})
    if digit3!=pc_digit_list[2]:
        en_6_3.config(bg="#FF6962")
    if digit4== str(pc_digit_list[3]):
        en_6_4.config(state=DISABLED)
        en_6_4.configure({"disabledbackground": "#D6FA8C"})
    if digit4!=pc_digit_list[3]:
        en_6_4.config(bg="#FF6962")
    if digit5== str(pc_digit_list[4]):
        en_6_5.config(state=DISABLED)
        en_6_5.configure({"disabledbackground": "#D6FA8C"})   
    if digit5!=pc_digit_list[4]:
        en_6_5.config(bg="#FF6962")
    if digit6== str(pc_digit_list[5]):
        en_6_6.config(state=DISABLED)
        en_6_6.configure({"disabledbackground": "#D6FA8C"})
    if digit6!=pc_digit_list[5]:
        en_6_6.config(bg="#FF6962") 
            
    if "".join(pc_digit_list)==member_number:
        show_winroot()
        
frame6 = Frame(root) 
frame6.configure(bg="#FFFAB6")
lbl_guess = Label(frame6, text="guess number with 6 digit :" )
lbl_guess.config(font=("Papyrus", 14))
lbl_guess.configure(bg="#FFFAB6",fg="#F05F00")
lbl_guess.grid(row=1,column=1,columnspan=2,pady=(40,50),padx=40)
d61 = StringVar
d62 = StringVar
d63 = StringVar
d64 = StringVar
d65 = StringVar
d66 = StringVar
en_6_1 = Entry(frame6, textvariable= d61)
en_6_1.place(x=60,y=167,width=42,height=58)
en_6_2 = Entry(frame6,textvariable= d62,width=5)
en_6_2.place(x=110,y=167,width=42,height=58)
en_6_3 = Entry(frame6,textvariable= d63,width=5)
en_6_3.place(x=160,y=167,width=42,height=58)
en_6_4 = Entry(frame6,textvariable= d64,width=5)
en_6_4.place(x=210,y=167,width=42,height=58)
en_6_5 = Entry(frame6,textvariable= d65,width=5)
en_6_5.place(x=260,y=167,width=42,height=58)
en_6_6 = Entry(frame6,textvariable= d66,width=5)
en_6_6.place(x=310,y=167,width=42,height=58)
bt_play6 = Button(
                    frame6,
                    text="Play",
                    width=30,
                    command= lambda:play6(
                                            digit1 = en_6_1.get(),
                                            digit2 = en_6_2.get(),
                                            digit3 = en_6_3.get(),
                                            digit4 = en_6_4.get(),
                                            digit5 = en_6_5.get(),
                                            digit6 = en_6_6.get(),
                                            pc_num = pc_number6
                                        )
            )
bt_play6.place(x=120,y=270,width=200,height=45)
bt_play6.configure(bg="#FFB346")
bt_back2 = Button(frame6, text="BACK", width=5,command= back2)
bt_back2.configure(bg="#ffcc5c")
bt_back2.place(x=380,y=5)
#endregion

#region LEVEL7
pc_number7 = random.randint(1000000,9999999)  
print(pc_number7)
def play7(digit1,digit2,digit3,digit4,digit5,digit6,digit7,pc_num):
    member_number = digit1+digit2+digit3+digit4+digit5+digit6+digit7
    pc_digit_list = [str(d) for d in str(pc_num)]
    if digit1== pc_digit_list[0]:
        en_7_1.config(state=DISABLED)
        en_7_1.configure({"disabledbackground": "#D6FA8C"})
    if digit1!=pc_digit_list[0]:
        en_7_1.config(bg="#FF6962")
    if digit2== str(pc_digit_list[1]):
        en_7_2.config(state=DISABLED)
        en_7_2.configure({"disabledbackground": "#D6FA8C"})
    if digit2!=pc_digit_list[1]:
        en_7_2.config(bg="#FF6962")
    if digit3== str(pc_digit_list[2]):
        en_7_3.config(state=DISABLED)
        en_7_3.configure({"disabledbackground": "#D6FA8C"})
    if digit3!=pc_digit_list[2]:
        en_7_3.config(bg="#FF6962")
    if digit4== str(pc_digit_list[3]):
        en_7_4.config(state=DISABLED)
        en_7_4.configure({"disabledbackground": "#D6FA8C"})
    if digit4!=pc_digit_list[3]:
        en_7_4.config(bg="#FF6962")
    if digit5== str(pc_digit_list[4]):
        en_7_5.config(state=DISABLED)
        en_7_5.configure({"disabledbackground": "#D6FA8C"})
    if digit5!=pc_digit_list[4]:
        en_7_5.config(bg="#FF6962")
    if digit6== str(pc_digit_list[5]):
        en_7_6.config(state=DISABLED)
        en_7_6.configure({"disabledbackground": "#D6FA8C"})
    if digit6!=pc_digit_list[5]:
        en_7_6.config(bg="#FF6962") 
    if digit7== str(pc_digit_list[6]):
        en_7_7.config(state=DISABLED)
        en_7_7.configure({"disabledbackground": "#D6FA8C"})
    if digit7!=pc_digit_list[6]:
        en_7_7.config(bg="#FF6962")        
    if "".join(pc_digit_list)==member_number:
        show_winroot()
        
frame7 = Frame(root) 
frame7.configure(bg="#FFFAB6")
lbl_guess = Label(frame7, text="guess number with 7 digit :" )
lbl_guess.config(font=("Papyrus", 14))
lbl_guess.configure(bg="#FFFAB6",fg="#F05F00")
lbl_guess.grid(row=1,column=1,columnspan=2,pady=(40,50),padx=40)
d71 = StringVar
d72 = StringVar
d73 = StringVar
d74 = StringVar
d75 = StringVar
d76 = StringVar
d77 = StringVar
en_7_1 = Entry(frame7, textvariable= d71)
en_7_1.place(x=50,y=167,width=42,height=58)
en_7_2 = Entry(frame7,textvariable= d72,width=5)
en_7_2.place(x=100,y=167,width=42,height=58)
en_7_3 = Entry(frame7,textvariable= d73,width=5)
en_7_3.place(x=150,y=167,width=42,height=58)
en_7_4 = Entry(frame7,textvariable= d74,width=5)
en_7_4.place(x=200,y=167,width=42,height=58)
en_7_5 = Entry(frame7,textvariable= d75,width=5)
en_7_5.place(x=250,y=167,width=42,height=58)
en_7_6 = Entry(frame7,textvariable= d76,width=5)
en_7_6.place(x=300,y=167,width=42,height=58)
en_7_7 = Entry(frame7,textvariable= d77,width=5)
en_7_7.place(x=350,y=167,width=42,height=58)
bt_play7 = Button(
                    frame7,
                    text="Play",
                    width=30,
                    command= lambda:play7(
                                            digit1 = en_7_1.get(),
                                            digit2 = en_7_2.get(),
                                            digit3 = en_7_3.get(),
                                            digit4 = en_7_4.get(),
                                            digit5 = en_7_5.get(),
                                            digit6 = en_7_6.get(),
                                            digit7 = en_7_7.get(),
                                            pc_num = pc_number7
                                        )
            )
bt_play7.place(x=120,y=270,width=200,height=45)
bt_play7.configure(bg="#FFB346")
bt_back2 = Button(frame7, text="BACK", width=5,command= back2)
bt_back2.configure(bg="#ffcc5c")
bt_back2.place(x=380,y=5)
#endregion

#region LEVEL8
pc_number8 = random.randint(10000000,99999999)  
print(pc_number8)
def play8(digit1,digit2,digit3,digit4,digit5,digit6,digit7,digit8,pc_num):
    member_number = digit1+digit2+digit3+digit4+digit5+digit6+digit7+digit8
    pc_digit_list = [str(d) for d in str(pc_num)]
    if digit1== pc_digit_list[0]:
        en_8_1.config(state=DISABLED)
        en_8_1.configure({"disabledbackground": "#D6FA8C"})
    if digit1!=pc_digit_list[0]:
        en_8_1.config(bg="#FF6962")
    if digit2== str(pc_digit_list[1]):
        en_8_2.config(state=DISABLED)
        en_8_2.configure({"disabledbackground": "#D6FA8C"})
    if digit2!=pc_digit_list[1]:
        en_8_2.config(bg="#FF6962")
    if digit3== str(pc_digit_list[2]):
        en_8_3.config(state=DISABLED)
        en_8_3.configure({"disabledbackground": "#D6FA8C"})
    if digit3!=pc_digit_list[2]:
        en_8_3.config(bg="#FF6962")
    if digit4== str(pc_digit_list[3]):
        en_8_4.config(state=DISABLED)
        en_8_4.configure({"disabledbackground": "#D6FA8C"})
    if digit4!=pc_digit_list[3]:
        en_8_4.config(bg="#FF6962")
    if digit5== str(pc_digit_list[4]):
        en_8_5.config(state=DISABLED)
        en_8_5.configure({"disabledbackground": "#D6FA8C"})
    if digit5!=pc_digit_list[4]:
        en_8_5.config(bg="#FF6962")
    if digit6== str(pc_digit_list[5]):
        en_8_6.config(state=DISABLED)
        en_8_6.configure({"disabledbackground": "#D6FA8C"})
    if digit6!=pc_digit_list[5]:
        en_8_6.config(bg="#FF6962") 
    if digit7== str(pc_digit_list[6]):
        en_8_7.config(state=DISABLED)
        en_8_7.configure({"disabledbackground": "#D6FA8C"})
    if digit7!=pc_digit_list[6]:
        en_8_7.config(bg="#FF6962")
    if digit8== str(pc_digit_list[7]):
        en_8_8.config(state=DISABLED)
        en_8_8.configure({"disabledbackground": "#D6FA8C"})
    if digit8!=pc_digit_list[7]:
        en_8_8.config(bg="#FF6962")              
    if "".join(pc_digit_list)==member_number:
        show_winroot()
        
frame8 = Frame(root) 
frame8.configure(bg="#FFFAB6")
lbl_guess = Label(frame8, text="guess number with 8 digit :" )
lbl_guess.config(font=("Papyrus", 14))
lbl_guess.configure(bg="#FFFAB6",fg="#F05F00")
lbl_guess.grid(row=1,column=1,columnspan=2,pady=(40,50),padx=40)
d81 = StringVar
d82 = StringVar
d83 = StringVar
d84 = StringVar
d85 = StringVar
d86 = StringVar
d87 = StringVar
d88 = StringVar
en_8_1 = Entry(frame8, textvariable= d81)
en_8_1.place(x=20,y=167,width=42,height=58)
en_8_2 = Entry(frame8,textvariable= d82,width=5)
en_8_2.place(x=70,y=167,width=42,height=58)
en_8_3 = Entry(frame8,textvariable= d83,width=5)
en_8_3.place(x=120,y=167,width=42,height=58)
en_8_4 = Entry(frame8,textvariable= d84,width=5)
en_8_4.place(x=170,y=167,width=42,height=58)
en_8_5 = Entry(frame8,textvariable= d85,width=5)
en_8_5.place(x=220,y=167,width=42,height=58)
en_8_6 = Entry(frame8,textvariable= d86,width=5)
en_8_6.place(x=270,y=167,width=42,height=58)
en_8_7 = Entry(frame8,textvariable= d87,width=5)
en_8_7.place(x=320,y=167,width=42,height=58)
en_8_8 = Entry(frame8,textvariable= d88,width=5)
en_8_8.place(x=370,y=167,width=42,height=58)
bt_play8 = Button(
                    frame8,
                    text="Play",
                    width=30,
                    command= lambda:play8(
                                            digit1 = en_8_1.get(),
                                            digit2 = en_8_2.get(),
                                            digit3 = en_8_3.get(),
                                            digit4 = en_8_4.get(),
                                            digit5 = en_8_5.get(),
                                            digit6 = en_8_6.get(),
                                            digit7 = en_8_7.get(),
                                            digit8 = en_8_8.get(),
                                            pc_num = pc_number8
                                        )
            )
bt_play8.place(x=115,y=270,width=200,height=45)
bt_play8.configure(bg="#FFB346")
bt_back2 = Button(frame8, text="BACK", width=5,command= back2)
bt_back2.configure(bg="#ffcc5c")
bt_back2.place(x=380,y=5)
#endregion
 
#region LEVEL9
pc_number9 = random.randint(100000000,999999999)  
print(pc_number9)
def play9(digit1,digit2,digit3,digit4,digit5,digit6,digit7,digit8,digit9,pc_num):
    member_number = digit1+digit2+digit3+digit4+digit5+digit6+digit7+digit8+digit9
    pc_digit_list = [str(d) for d in str(pc_num)]
    if digit1== pc_digit_list[0]:
        en_9_1.config(state=DISABLED)
        en_9_1.configure({"disabledbackground": "#D6FA8C"})
    if digit1!=pc_digit_list[0]:
        en_9_1.config(bg="#FF6962")
    if digit2== str(pc_digit_list[1]):
        en_9_2.config(state=DISABLED)
        en_9_2.configure({"disabledbackground": "#D6FA8C"})
    if digit2!=pc_digit_list[1]:
        en_9_2.config(bg="#FF6962")
    if digit3== str(pc_digit_list[2]):
        en_9_3.config(state=DISABLED)
        en_9_3.configure({"disabledbackground": "#D6FA8C"})
    if digit3!=pc_digit_list[2]:
        en_9_3.config(bg="#FF6962")
    if digit4== str(pc_digit_list[3]):
        en_9_4.config(state=DISABLED)
        en_9_4.configure({"disabledbackground": "#D6FA8C"})
    if digit4!=pc_digit_list[3]:
        en_9_4.config(bg="#FF6962")
    if digit5== str(pc_digit_list[4]):
        en_9_5.config(state=DISABLED)
        en_9_5.configure({"disabledbackground": "#D6FA8C"})
    if digit5!=pc_digit_list[4]:
        en_9_5.config(bg="#FF6962")
    if digit6== str(pc_digit_list[5]):
        en_9_6.config(state=DISABLED)
        en_9_6.configure({"disabledbackground": "#D6FA8C"})
    if digit6!=pc_digit_list[5]:
        en_9_6.config(bg="#FF6962") 
    if digit7== str(pc_digit_list[6]):
        en_9_7.config(state=DISABLED)
        en_9_7.configure({"disabledbackground": "#D6FA8C"})
    if digit7!=pc_digit_list[6]:
        en_9_7.config(bg="#FF6962")
    if digit8== str(pc_digit_list[7]):
        en_9_8.config(state=DISABLED)
        en_9_8.configure({"disabledbackground": "#D6FA8C"})
    if digit8!=pc_digit_list[7]:
        en_9_8.config(bg="#FF6962")     
    if digit9== str(pc_digit_list[8]):
        en_9_9.config(state=DISABLED)
        en_9_9.configure({"disabledbackground": "#D6FA8C"})
    if digit9!=pc_digit_list[8]:
        en_9_9.config(bg="#FF6962")              
    if "".join(pc_digit_list)==member_number:
        show_winroot()
        
frame9 = Frame(root) 
frame9.configure(bg="#FFFAB6")
lbl_guess = Label(frame9, text="guess number with 9 digit :" )
lbl_guess.config(font=("Papyrus", 14))
lbl_guess.configure(bg="#FFFAB6",fg="#F05F00")
lbl_guess.grid(row=1,column=1,columnspan=2,pady=(40,50),padx=40)
d91 = StringVar
d92 = StringVar
d93 = StringVar
d94 = StringVar
d95 = StringVar
d96 = StringVar
d97 = StringVar
d98 = StringVar
d99 = StringVar
en_9_1 = Entry(frame9, textvariable= d91)
en_9_1.place(x=30,y=167,width=37,height=58)
en_9_2 = Entry(frame9,textvariable= d92,width=5)
en_9_2.place(x=70,y=167,width=37,height=58)
en_9_3 = Entry(frame9,textvariable= d93,width=5)
en_9_3.place(x=110,y=167,width=37,height=58)
en_9_4 = Entry(frame9,textvariable= d94,width=5)
en_9_4.place(x=150,y=167,width=37,height=58)
en_9_5 = Entry(frame9,textvariable= d95,width=5)
en_9_5.place(x=190,y=167,width=37,height=58)
en_9_6 = Entry(frame9,textvariable= d96,width=5)
en_9_6.place(x=230,y=167,width=37,height=58)
en_9_7 = Entry(frame9,textvariable= d97,width=5)
en_9_7.place(x=270,y=167,width=37,height=58)
en_9_8 = Entry(frame9,textvariable= d98,width=5)
en_9_8.place(x=310,y=167,width=37,height=58)
en_9_9 = Entry(frame9,textvariable= d99,width=5)
en_9_9.place(x=350,y=167,width=37,height=58)
bt_play9 = Button(
                    frame9,
                    text="Play",
                    width=30,
                    command= lambda:play9(
                                            digit1 = en_9_1.get(),
                                            digit2 = en_9_2.get(),
                                            digit3 = en_9_3.get(),
                                            digit4 = en_9_4.get(),
                                            digit5 = en_9_5.get(),
                                            digit6 = en_9_6.get(),
                                            digit7 = en_9_7.get(),
                                            digit8 = en_9_8.get(),
                                            digit9 = en_9_9.get(),
                                            pc_num = pc_number9
                                        )
            )
bt_play9.place(x=110,y=270,width=200,height=45)
bt_play9.configure(bg="#FFB346")
bt_back2 = Button(frame9, text="BACK", width=5,command= back2)
bt_back2.configure(bg="#ffcc5c")
bt_back2.place(x=380,y=5)
#endregion

#region FRAME1      
frame1= Frame(root)
frame1.configure(bg="#fbefcc")
#ENTRY
username_var = StringVar()
password_var = StringVar()
ent_username = Entry(frame1,width=30,textvariable=username_var)

ent_username.grid(row=2,column=1,columnspan=2,pady=5,ipady=15,padx=(1,110))
ent_password = Entry(frame1,width=30,textvariabl=password_var)

ent_password.grid(row=3,column=1,columnspan=2,pady=5,ipady=15,padx=(1,110))

#LABL
lbl_masterandminor = Label(frame1, text="Master and Minor" )
lbl_masterandminor.config(font=("Papyrus", 29))
lbl_masterandminor.configure(bg="#fbefcc",fg="#d64161")
lbl_masterandminor.grid(row=0,column=0,columnspan=2,pady=(15,40),padx=(30,10),ipadx=35)
lbl_username = Label(frame1,text="User Name :")
lbl_username.configure(bg="#fbefcc",fg="#d64161")
lbl_username.grid(row=2,column=0,pady=5,ipady=15,padx=(30,5))
lbl_password = Label(frame1,text="Password :")
lbl_password.configure(bg="#fbefcc",fg="#d64161")
lbl_password.grid(row=3,column=0,pady=5,ipady=10,padx=(30,5))
lbl_signin=Label(frame1,text="if you dont have an account :")
lbl_signin.configure(bg="#fbefcc",fg="#034f84")
lbl_signin.grid(row=6,column=1,columnspan=2,pady=10,ipady=7,padx=(1,110))

#BUTTON
bt_login = Button(
                    frame1,
                    text="Login",
                    font="Garamond",
                    width=16,
                    bg="#e06377",
                    command= lambda:check(username = username_var.get(), password = password_var.get())
                )
bt_login.grid(row=5,column=1,columnspan=2,pady=5,ipady=7,padx=(1,110))
bt_signin = Button(frame1, text="Sign In",bg="#80ced6" ,command= show_frame2)
bt_signin.grid(row=7,column=1,columnspan=2,pady=2,ipady=7,padx=(1,120))
#endregion

#region FRAME2
frame2 = Frame(root)
frame2.configure(bg="#d5f4e6")

#entry
name_var = StringVar()
family_var = StringVar()
final_usernam_var = StringVar()
final_password_var = StringVar()

ent_name = Entry(frame2,width=30,textvariable=name_var)
ent_name.grid(row=1,column=1,columnspan=2,pady=5,ipady=15,padx=(25,60))
ent_family = Entry(frame2,width=30,textvariable=family_var)
ent_family.grid(row=2,column=1,columnspan=2,pady=5,ipady=15,padx=(25,60))
ent_username = Entry(frame2,width=30,textvariable=final_usernam_var)
ent_username.grid(row=3,column=1,columnspan=2,pady=5,ipady=15,padx=(25,60))
ent_password = Entry(frame2,width=30,textvariable=final_password_var)
ent_password.grid(row=4,column=1,columnspan=2,pady=5,ipady=15,padx=(25,60))
#button
bt_signin_f = Button(
                        frame2,
                        text="Sign In" ,
                        font="Garamond",
                        width=16,
                        command= lambda: show_frame1(
                                                        name = name_var.get(),
                                                        family = family_var.get(),
                                                        username = final_usernam_var.get(),
                                                        password = final_password_var.get()
                                                    )
                )
bt_signin_f.configure(bg="#8ab6d6")
bt_signin_f.grid(row=5,column=1,columnspan=2,pady=5,ipady=8,padx=(25,60))
bt2_back1 = Button(frame2, text="BACK", width=5,command= back1)
bt2_back1.configure(bg="#ffdcdc")
bt2_back1.place(x=380,y=5)

#lable
lbl_detail = Label(frame2, text="Enter your details " )
lbl_detail.configure(bg="#d5f4e6",fg="#034f84")
lbl_detail.config(font=("Garamond", 16))
lbl_detail.grid(row=0,column=1,columnspan=2,pady=(25,20),padx=(20,50))
lbl_name = Label(frame2,text="Name :")
lbl_name.configure(bg="#d5f4e6",fg="#034f84")
lbl_name.grid(row=1,column=0,pady=5,ipady=15,padx=(30,5))
lbl_family = Label(frame2,text="Family :")
lbl_family.configure(bg="#d5f4e6",fg="#034f84")
lbl_family.grid(row=2,column=0,pady=5,ipady=15,padx=(30,5))
lbl_username = Label(frame2,text="User Name :")
lbl_username.configure(bg="#d5f4e6",fg="#034f84")
lbl_username.grid(row=3,column=0,pady=5,ipady=15,padx=(30,5))
lbl_password = Label(frame2,text="Password :")
lbl_password.configure(bg="#d5f4e6",fg="#034f84")
lbl_password.grid(row=4,column=0,pady=5,ipady=15,padx=(30,5))
#endregion 

#region MENU
def show_rule_frame():
    show_rule = Tk()
    show_rule.geometry("440x440")
    show_rule.config(bg="#CBE8BE")
    show_rule.title("Rules")
    text = Label(show_rule,text=" Rules of the game")
    text.config(font =("Papyrus", 15),bg="#CBE8BE")
    text.place(x=140,y=6)
    text_rule = Text(show_rule, height = 5, width = 52,bg="#CBE8BE",bd=0)
    text_rule.config(font =("Papyrus", 14))
    text_rule.place(x=12,y=45,width=414,height=400)
    Fact ="""First of all,you have to choose the level you want 
    according to the difficulty and easy , each level
    has the same number of digits according to the
    degree of difficulty to guess the number correctly.
    In this way, after selecting the level,
    the empty degrees are guessed,and after pressing 
    the play button, the numbers that are guessed 
    correctly or incorrectly are displayed.
    
    """
    bt_ok_g = Button(show_rule, text = "OK", command = show_rule.destroy)
    bt_ok_g.config(bg="#3EB489")
    bt_ok_g.place(x=200,y=370,width=50,height=35)
    text_rule.insert(tk.END, Fact)
    show_rule.mainloop()
def producer():
    show_producer = Tk()
    show_producer.geometry("440x440")
    show_producer.title("producer")
    show_producer.configure(bg="#ffc87a")
    lbl_producer = Label(show_producer,text="thank you for your attention")
    lbl_producer.configure(font =("Papyrus", 15),bg="#ffc87a")
    lbl_producer.place(x=98,y=90)
    lbl2_producer = Label(show_producer,text="Negin Parsa")
    lbl2_producer.configure(font =("Papyrus", 15),bg="#ffc87a")
    lbl2_producer.place(x=160,y=140)
    bt_ok_p = Button(show_producer, text = "OK", command = show_producer.destroy)
    bt_ok_p.config(bg="#FFB346")
    bt_ok_p.place(x=200,y=370,width=50,height=35)
    show_producer.mainloop()

menubar = Menu(root, background='#FCEBD9', foreground='black')
filemenu = Menu(menubar, tearoff=0, background='#FCEBD9',foreground='black')
filemenu.add_command(label="Rule game", command=show_rule_frame)
filemenu.add_command(label="Produser", command=producer)
menubar.add_cascade(label="About", menu=filemenu)
menubar.add_command(label="Exit", command=root.destroy)  

root.config(bg='#FCEBD9', menu=menubar)
#endregion

#region FRAME3
frame3 = Frame(root)
frame3.configure(bg="#F3D8E8")
name_show = username_var.get()
lbl_level = Label(frame3,text="choose level..." )
lbl_level.config(font=("Garamond", 18))
lbl_level.configure(bg="#F3D8E8",fg="#673146")
lbl_level.grid(row=1,column=1,pady=(5,40))

lb_esay = Label(frame3,text="easy")
lb_esay.configure(bg="#F3D8E8")
lb_esay.grid(row=3,column=1,padx=10,pady=(5,10))
bt_4 = Button(frame3,text="Level 4",width=10,height=5, command= show_level4)
bt_4.configure(bg="#E6B2D0")
bt_4.grid(row=4,column=1,padx=(40,18),ipadx=10,pady=(3,10))
bt_5 = Button(frame3,text="Level 5",width=10,height=5, command= show_level5)
bt_5.configure(bg="#E6B2D0")
bt_5.grid(row=5,column=1,padx=(40,18),ipadx=10,pady=30)

lb_medium = Label(frame3,text="medium")
lb_medium.configure(bg="#F3D8E8")
lb_medium.grid(row=3,column=2,padx=10,pady=(5,10))
bt_6 = Button(frame3,text="Level 6",width=10,height=5,command= show_level6)
bt_6.configure(bg="#CA68A1")
bt_6.grid(row=4,column=2,padx=(10,8),ipadx=10,pady=(3,10))
bt_7 = Button(frame3,text="Level 7",width=10,height=5,command= show_level7)
bt_7.configure(bg="#CA68A1")
bt_7.grid(row=5,column=2,padx=(10,8),ipadx=10,pady=30)

lb_hard= Label(frame3,text="hard")
lb_hard.configure(bg="#F3D8E8")
lb_hard.grid(row=3,column=3,padx=10,pady=(5,10))
bt_8 = Button(frame3,text="Level 8",width=10,height=5,command= show_level8)
bt_8.configure(bg="#BC438A")
bt_8.grid(row=4,column=3,padx=(27,1),ipadx=10,pady=(3,10))
bt_9 = Button(frame3,text="Level 9",width=10,height=5,command= show_level9)
bt_9.configure(bg="#BC438A")
bt_9.grid(row=5,column=3,padx=(27,1),ipadx=10,pady=30)

bt3_back1 = Button(frame3, text="BACK", width=5,command= back1)
bt3_back1.configure(bg="#80ced6")
bt3_back1.place(x=380,y=5)
#endregion


frame1.grid(row=0,column=0,columnspan=2,rowspan=2,ipadx=10,padx=(1,5),pady=(1,8),ipady=25)
root.mainloop()

