# Call Tkinter Library To Start
from tkinter import *


# Start Making One Window In Tkinter
win = Tk()
# Change Size Of Window
win.geometry("300x300")
# Put Title Name Of Window
win.title('Calculator')


# These Variable Are For Clean The Entry Screen When One Operate As + - * / Called And You Want To Put New Number
a , b , c = 0 , 1 , 0
# These Variable Are For Oprate Numbers In Calculate As Addition Or Subtraction
x , y , z =  0 , 0 , 0
# These Variable Are For Knowing That Which Operator Was Called That Button(btn18(Enter Button)) Start Operate On It When User Call This Button
m , n , o , p = 0 , 0 , 0 , 0
# This Varible Is For If Operate With One Operator Was Done Operator Dont Do Action Again
t = 0



# Make One Entry Box For Type Number
en = Entry(win , width = 50 )
# Put Entry Box In Your Position
en.place(x = 0 , y = 0)
# Make Other Entry Like Up
en1 = Entry(win , width = 50)
en1.place(x = 0 , y = 30)



# Make Functon For Button To Insert Number In Enrtry And Clean Entry Screen After Operation
def cbtn0():
    #Call c Variable As Global TO Read In Function
    global c , t
    # Put Condition To Know If Our Variable In Our Function That Is For Operators Had Change To Clean Screen If You Right New Number It Meaning Every Time After We Use Operator Button And After Use Number Button Screen Automaticaly Be Clean
    if c == b:
        # Entry Box Clean Command
        en.delete(0 , END)
        # Becuase c And b Variable Now Are Equal We Sum C With 1 If We Right More Number Dont Do This Condition Again And Cross It And Do Else
        c += 1
        # Insert Number Command For Put Text Or Number In Entry Box
        en.insert(END , 0)
        t = 0
    # This Is For Other True Condition If Last one Was'nt True
    else:
        en.insert(END , 0)

# This Is Button Making Command And Information Inside As Window Variable Name And Button Name That We Have Here As (text = '0') And Etc ... And Command That Is Here For Calling Button Function
btn0 = Button(win , text = '0' , width = '4' , height = '2' , bd = 4 , command = cbtn0)
# This Command Is For Put Button On Your Potion x An y Is Posion On Point x = Horizontal And y = Vertical
btn0.place(x = 45 , y = 253)


# These All Functions Until (btn9) And (ppoint) Are Same As Up
def cbtn1():
    global c , t
    if c == b:
        en.delete(0 , END)
        c += 1
        en.insert(END , 1)
        t = 0
    else:
        en.insert(END , 1)


btn1 = Button(win , text = '1' , width = '4' , height = '2' , bd = 4 , command = cbtn1)
btn1.place(x = 2 , y = 205)



def cbtn2():        
    global c , t
    if c == b:
        en.delete(0 , END)
        c += 1
        en.insert(END , 2)
        t = 0
    else:
        en.insert(END , 2)

btn2 = Button(win , text = '2' , width = '4' , height = '2' , bd = 4 , command = cbtn2)
btn2.place(x = 45 , y = 205)



def cbtn3():    
    global c , t
    if c == b:
        en.delete(0 , END)
        c += 1
        en.insert(END , 3)
        t = 0
    else:
        en.insert(END , 3)

btn3 = Button(win , text = '3' , width = '4' , height = '2' , bd = 4 , command = cbtn3)
btn3.place(x = 88 , y = 205)



def cbtn4():
    global c , t
    if c == b:
        en.delete(0 , END)
        c += 1
        en.insert(END , 4)
        t = 0
    else:
        en.insert(END , 4)

btn4 = Button(win , text = '4' , width = '4' , height = '2' , bd = 4 , command = cbtn4)
btn4.place(x = 2 , y = 157)



def cbtn5():
    global c , t
    if c == b:
        en.delete(0 , END)
        c += 1
        en.insert(END , 5)
        t = 0
    else:
        en.insert(END , 5)

btn5 = Button(win , text = '5' , width = '4' , height = '2' , bd = 4 , command = cbtn5)
btn5.place(x = 45 , y = 157)



def cbtn6():
    global c , t
    if c == b:
        en.delete(0 , END)
        c += 1
        en.insert(END , 6)
        t = 0
    else:
        en.insert(END , 6)

btn6 = Button(win , text = '6' , width = '4' , height = '2' , bd = 4 , command = cbtn6)
btn6.place(x = 88 , y = 157)



def cbtn7():
    global c , t
    if c == b:
        en.delete(0 , END)
        c += 1
        en.insert(END , 7)
        t = 0
    else:
        en.insert(END , 7)

btn7 = Button(win , text = '7' , width = '4' , height = '2' , bd = 4 , command = cbtn7)
btn7.place(x = 2 , y = 109)



def cbtn8():
    global c , t
    if c == b:
        en.delete(0 , END)
        c += 1
        en.insert(END , 8)
        t = 0
    else:
        en.insert(END , 8)

btn8 = Button(win , text = '8' , width = '4' , height = '2' , bd = 4 , command = cbtn8 )
btn8.place(x= 45 , y = 109)



def cbtn9():
    global c , t
    if c == b:
        en.delete(0 , END)
        c += 1
        en.insert(END , 9)
        t = 0
    else:
        en.insert(END , 9)

btn9 = Button(win , text = '9' , width = '4' , height = '2' , bd = 4 , command = cbtn9)
btn9.place(x = 88 , y = 109)



def ppoint():
    global c , t
    if c == b:
        en.delete(0 , END)
        c += 1
        en.insert(END , '.')
        t = 0
    else:
        en.insert(END , '.')

btn15 = Button(win , text = '.' , width = '4' , height = '2' , bd = 4 , command = ppoint)
btn15.place(x = 88 , y = 253)




# Becuase y Variable Need To Every Time We Right New Number In Entery Be Same Ase Entry Number Here Make One Fuction And Take Entry Number With get() Command In y Variable Until Use in Our Functions That Is For Operate Numbers 
def ygeter():
    global y
    # This Command Put The Amount Of Entry Inside y Variable
    y = float(en.get())


# Here We Make Addition Function And One Tip : In Function And State Condition And For Loop And Other Commands Like This We Should Put Our Comand Inside These Commands In Their Indent That Inden Meaning Is For Step Forward In Python
def addcalculate():
    # First We Call Our Variable In Our Fuction As Local Variable Becuase When We Make Variable Out Of Our Function Those Variable Don't Work In Function Becuase In Function We Need Local Variable So We Use global Command And Our Variables Name To Use In Function 
    global a , b , c , x , y , z , m , n , o , p , t
    # Here We Put One Condition For Put Amount In Variable x If Is 0
    if x == 0:
        # This Is Command For Put Entry Amount In x
        x = float(en.get())
    # Here We Put One Condition For Put Amount In Variable y If Is Not 0 And Here Is Important To Know In Operation y Is That Number That Come EvryTime To Operate With x So ygeter() Function Is For This That EvryTime New Number Come To y For Operate  
    if y != 0:
        ygeter()
    if t == 0:
        # Operat For + Button
        z = x + y
        # Here We Say To Button Every Time Attach Numbers That We Right In Second Entry And One + To Other Entry To Know Ho Many Items We Want To Operate 
        en1.insert(END , en.get() + '+')
        # Here Again We Clean The Entry To Be Clean *Tip : If We Dont Clean Entry Like This New Number Attach To Olde Numbers And ENtry Go Full    
        en.delete(0 , END)
        # Here We Put New Amount Of Operate Inside First Entry    
        en.insert(END , z)
    t += 1
    # Variable For Operate Go Ready For Next Time Its Meanin We Put Total Amount Inside  Every Time For New Operate
    x = z
    # Here We Put This Condition For Condition Of Line 211 And 212 If Amount Of This Variable  After One Operate Was'nt To Take Amount From Entry Becuase Of Any Operate That is Possible To y Amount Be 0 
    if y == 0:
        # We Addition y Amount To 1
        y += 1
    # Here We Put These Variable For Knowing About One Operate Run To Clean Enrty Screen With Number Button Putting Here We Sayed Every Time b Have Addition To 1
    b += 1
    # Put b In a 
    a = b  
    # Put a In c I Have One Variable Here As a And I Just Use This Variable For Better Knowing To Understand How I Use These Variable To Do This Operate For Clean Screen
    c = a
    # These Condiotions Are For Enter And Equal Button To Work Good I Put These Algoritm With Variable To Our Program Work Smart And Good Here For This Operation We Have Four Variable The In For Function For Operation One Variable Is Biger Than Other To Our Function For Enter And Equal Know With Operator In Wich Function Used To Operate As Thar Operator But With Enter Button   
    if n > o and n >p:
        m = n
    elif o > n and o >p:
        m = o
    elif p > n and p>o:
        m = p
    m +=1
    

btn10 = Button(win , text = '+' , width = '4' , height = '2' , bd = 4 , command = addcalculate)
btn10.place(x = 130 , y = 205)


# For All Of These Function Also Is Like Up
def subcalculate():
    global a , b , c , x , y , z , m , n , o , p , t
    if x == 0:
        x = float(en.get())
    if y != 0:
        ygeter()
    if t == 0:
        z = x - y
        en1.insert(END , en.get() + '-')        
        en.delete(0 , END)
        en.insert(END , z)
    t += 1
    x = z
    if y == 0:
        y += 1  
    b += 1
    a = b
    c = a
    if m > o and m > p:
        n = m
    elif o > m and o > p:
        n = o
    elif p > m and p > o:
        n = p
    n += 1
    

btn11 = Button(win , text = '-' , width = '4' , height = '2' , bd =4 , command = subcalculate)
btn11.place(x = 130 , y = 157) 



def multiplecalculate():
    global a , b , c , x , y , z , m , n , o , p , t
    if x == 0:
        x = float(en.get())
    if y != 0:
        ygeter()
    if y == 0:
        y += 1
    if t == 0:
        z = x * y
        en1.insert(END , en.get() + '*')        
        en.delete(0 , END)
        en.insert(END , z)
    t += 1
    x = z
    if y == 0:
        y += 1  
    b += 1
    a = b
    c = a
    if o > m and o > n:
        p = o
    elif m > o and m > n:
        p = m
    elif n > o and n > m:
        p = n
    p += 1

btn12 = Button(win , text = '*' , width = '4' , height = '2' , bd = 4 , command = multiplecalculate)
btn12.place(x = 130 , y = 109)



def divisioncalculate():
    global a , b , c , x , y , z , m , n , o , p , t
    if x == 0:
        x = float(en.get())
    if y != 0:
        ygeter()    
    if y == 0:
        y += 1
    if t == 0:
        z = x / y
        en1.insert(END , en.get() + '/')        
        en.delete(0 , END)
        en.insert(END , z)
    t += 1
    x = z
    if y == 0:
        y += 1  
    b += 1
    a = b
    c = a
    if m > n and m > p:
        o = m
    elif n > m and n > p:
        o = n
    elif p > m and p > n:
        o = p
    o += 1

btn17 = Button(win , text = '/' , width = '10' , height = '2' , bd = 4 , command = divisioncalculate)
btn17.place(x = 88 , y = 59)


# *Tip: Here In Equal Button I Put All Our Conditions To Know When Equal Used First Take Wich Operator Was Used From Than Oparting I Right Up And Take TaThat Operation As Equal Button And Empty All Variable To Just We Cal Do One Time Operate With Equal Button
def eequal():
    global m , n , o , p
    if m > n and m > n and m > p:
        addcalculate()
        m , n , o , p = 0 , 0 , 0 , 0
    elif n > m and n > o and n > p:
        subcalculate()
        m , n , o , p = 0 , 0 , 0 , 0
    elif p > m and p > n and p > o:
        multiplecalculate()
        m , n , o , p = 0 , 0 , 0 , 0
    elif o > m and o > n and o > p:
        divisioncalculate()
        m , n , o , p = 0 , 0 , 0 , 0
    

btn16 = Button(win , text = '=' , width = '4' , height = '2' , bd = 4 , command = eequal)
btn16.place(x = 130 , y = 253)



# Here Is Like Up As Equal But We Can Use Enter Also As Operator Its Meanin We Can Use Enter For Ever Operating
def eenter():
    global m , n , o , p
    if m > n and m > n and m > p:
        addcalculate()
    elif n > m and n > o and n > p:
        subcalculate()
    elif p > m and p > n and p > o:
        multiplecalculate()
    elif o > m and o > n and o > p:
        divisioncalculate()

btn18 = Button(win , text = 'Enter' , width = '15' , height = '15' , bd = 4 , command = eenter)
btn18.place(x = 175 , y = 58)


# This Function Is For Clean All Caculate And Entries
def bclear():
    global x , y , z , m , n , o , p
    en1.delete(0 , END)
    en.delete(0 , END)
    x = 0
    y = 0
    z = 0
    m , n , o , p = 0 , 0 , 0 , 0

btn14 = Button(win , text = 'C' , width = '4' , height = '2' , bd = 4 , command = bclear)
btn14.place(x = 2 , y = 253)


# This Fuction Is For Just Clean Entry One That We Right Our Numbers
def sclear():
    en.delete(0 , END)


btn13 = Button(win , text = 'c' , width = '10' , height = '2' , bd = 4 , command = sclear)
btn13.place(x = 2 , y = 59)



mainloop()