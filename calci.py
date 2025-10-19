import tkinter as tk
root=tk.Tk()
root.title("simple calculator")
root.geometry("400x500")
root.resizable(False,False)
entry=tk.Entry(root,width=25,borderwidth=5,font=('Arial',18),bg="pink",fg="blue")
entry.grid(row=0,column=0,columnspan=4,padx=10,pady=20)
def button_click(number):
    current=entry.get()
    entry.delete(0,tk.END)
    entry.insert(0,current+str(number))
def button_equal():
    try:
        result=str(eval(entry.get())) 
        entry.delete(0,tk.END)
        entry.insert(0,result) 
    except:
        entry.delete(0,tk.END)
        entry.insert(0,"Error")
buttons=[
    ('7',1,0),('8',1,1),('9',1,2),('+',1,3),
    ('4',2,0),('5',2,1),('6',2,2),('-',2,3),
    ('1',3,0),('2',3,1),('3',3,2),('*',3,3),
    ('0',4,0),('.',4,1),('c',4,2),('/',4,3),
]
for(text,row,col)in buttons:
    if text=='C':
        tk.Button(root,text=text,width=5,height=2,font=("Arial",16),command=button_clear).grid(row=row,column=col,padx=5,pady=5)
    else:
        tk.Button(root,text=text,width=5,height=2,font=('Arial',16),command=lambda t=text:button_click(t)).grid(row=row,column=col,padx=5,pady=5)
equal_button=tk.Button(root,text='=',width=23,height=2,font=('Arial',16),command=button_equal)
equal_button.grid(row=5,column=0,columnspan=4,padx=5,pady=10)
root.mainloop()        

