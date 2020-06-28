from tkinter import Tk,Label,Entry,Button,RAISED     #imported the important modules

root = Tk()                                          
root.geometry("505x235")                             #creating a canvas to put all the things measures are in pixel
Entry(root,bg = "gray", width = 34).place(x = 287, y = 20)       #creating a calculator display column
labels = [['MC','M+','M-','MR'],
          ['C','√','x2','+' ],
          ['7', '8', '9','-'],     
          ['4', '5', '6','*'],     
          ['1', '2', '3','/'],
          ['0', '.', '+-','=']]                    #inserting the labels as a array
x=255
y=20
k=10
for r in range(6):                                #for loop which prints all the labels in the above arrey
    y+=30
    for c in range(4):
        x+=30
        Button(root,relief=RAISED,padx=k,text=labels[r][c]).place(x=x, y=y)    #all the labels are creating as buttons
        x+=25
    k=15
    x=255   
    
Label(root, text = "Loan Amount:").place(x = 20,y = 50)             #creating additional entry boxes and its labels
Entry(root).place(x = 150, y = 50) 
Label(root, text = "Interest Rate:").place(x = 20, y = 90)
Entry(root).place(x = 150, y = 90) 
Label(root, text = "Loan Terms:").place(x = 20, y = 130)
Entry(root).place(x = 150, y = 130)
Button(root, text = "Compute Mortgage").place(x = 20, y = 170)
Entry(root).place(x = 150, y = 170)
root.mainloop()                                                   #making a loop to see continuously