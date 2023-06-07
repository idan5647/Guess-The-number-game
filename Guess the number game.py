from tkinter import *
from random import *

num2=randint(1,100)
counter=10
def check():
  global counter
  num=int(txt.get())
  if num2==num:
    lbl2.configure(text='correct', fg='green')
  elif num>num2:
    lbl2.configure(text='too big', fg='red')
  elif num2>num:
    lbl2.configure(text='too small', fg='red')
  counter -= 1
  if counter > 0:
    lbl_counter.configure(text=f"You have {counter} turns left")
  else:
    print("game over you lost")
    root.destroy()

def restart():
  global counter
  global num2
  counter=10
  lbl_counter.configure(text="You have 10 turns left")
  num2=randint(1,100)
  lbl2.configure(text="start")

def back():
  global big_flag
  global flag
  root.destroy()
  big_flag=0
  flag=0



counter2=2
counter3=0
def check2():
  global counter2
  global counter3
  num=int(txt.get())
  if num2==num:
    if counter2 == 2:
      lbl2.configure(text=f'player one: {name1} won!!!!', fg='green')
      counter3 += 1
    else:
      lbl2.configure(text=f'player two: {name2} won!!!!', fg='green')
      counter3 += 1
  if counter3==0:
    if num>num2:
      lbl2.configure(text='too big', fg='red')
    elif num2>num:
      lbl2.configure(text='too small', fg='red')
    else:
      print("game over you lost")
      root2.destroy()
    if counter2 == 2:
      lbl_players.configure(text=f"player {counter2}: {name2}")
      counter2 -= 1
    else:
      lbl_players.configure(text=f"player {counter2}: {name1}")
      counter2 += 1

def restart2():
  global counter2
  global num2
  counter2=2
  lbl_players.configure(text="player 1")
  num2=randint(1,100)
  lbl2.configure(text="start")
  counter3=0

def back2():
  global big_flag
  global flag
  root2.destroy()
  big_flag=0
  flag=0

name1=""
name2=""

def sumbit():
  global name1
  global name2
  name1=txt1.get()
  name2=txt2.get()
  root_name.destroy()
  




big_flag=0
flag=0
def one():
  global flag
  flag += 1
  start.destroy()
  
def two():
  start.destroy()

while big_flag==0:
  start=Tk()
  start.title("start")
  start.configure(bg="grey")
  start.geometry("400x300")
  lbl=Label(start, text='The number of players in the game is:')
  lbl.pack(pady=5)
  btn_1pl=Button(start, text='1 player', bg="cyan", command=one)
  btn_1pl.pack(pady=50)
  btn_2pl=Button(start, text='2 players', bg="pink", command=two)
  btn_2pl.pack(pady=50)
  big_flag += 1
  start.mainloop()
  
  if flag==1:
    root=Tk()
    root.geometry("400x300")
    root.configure(bg="cyan")
    root.title('Guess the number one player')
    
    lbl=Label(root, text='guess number: ', bg="pink")
    lbl.grid(row=0, column=0)
    txt=Entry(root)
    txt.grid(row=0, column=1)
    
    btn=Button(root, text='Check', bg="brown", command=check)
    btn.grid(row=1, column=1)
    btn=Button(root, text='restart', bg="brown", command=restart)
    btn.grid(row=3, column=1)
    
    lbl2=Label(root, text='start', bg="pink", fg='black')
    lbl2.grid(row=4, column=1)
    lbl_counter=Label(root, text="You have 10 turns left", bg="pink")
    lbl_counter.grid(row=2, column=0)
    btn_back=Button(root, text="back", bg="red", command=back)
    btn_back.grid(row=9, column=0)
    
    root.mainloop()
  else:
    root_name=Tk()
    root_name.title("name")
    
    lbl_name1=Label(root_name, text='enter name of player one: ', bg="pink")
    lbl_name1.grid(row=0, column=0)
    txt1=Entry(root_name)
    txt1.grid(row=0, column=1)

    lbl_name2=Label(root_name, text='enter name of player two: ', bg="pink")
    lbl_name2.grid(row=1, column=0)
    txt2=Entry(root_name)
    txt2.grid(row=1, column=1)

    btn=Button(root_name, text='Sumbit', bg="brown", command=sumbit)
    btn.grid(row=2, column=1)
    

    root_name.mainloop()
    
    root2=Tk()
    root2.geometry("400x300")
    root2.configure(bg="cyan")
    root2.title('Guess the number two players')
    
    lbl=Label(root2, text='guess number: ', bg="pink")
    lbl.grid(row=0, column=0)
    txt=Entry(root2)
    txt.grid(row=0, column=1)
    
    btn=Button(root2, text='Check', bg="brown", command=check2)
    btn.grid(row=1, column=1)
    btn=Button(root2, text='restart', bg="brown", command=restart2)
    btn.grid(row=3, column=1)
    
    lbl2=Label(root2, text='start', bg="pink", fg='black')
    lbl2.grid(row=4, column=1)
    lbl_players=Label(root2, text=f"player 1: {name1}", bg="pink")
    lbl_players.grid(row=2, column=0)
    btn_back=Button(root2, text="back", bg="red", command=back2)
    btn_back.grid(row=9, column=0)
    
    root2.mainloop()s