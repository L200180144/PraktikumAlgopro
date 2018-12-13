from tkinter import*

my_app = Tk(className= 'Kalkulator sederhana')
L1 = Label(my_app, text= 'Bangun Geometri', font= ('Arial', 24))
L1.grid(row=0, column=0, columnspan=3, sticky= 'w')
L2 = Label(my_app, text= 'Deskripsi tentang bangun persegi, antaralain nama, dimensi, contoh benda, dll.')
L2.grid(row=1, column=0, columnspan=3, sticky= 'w')
L3 = Label(my_app, text= 'Sisi :')
L3.grid(row=3, column=0, columnspan=3, sticky= 'w')
E3 = Entry(my_app)
E3.grid(row=3, column=1, sticky='w')
L4 = Label(my_app, text='Luas:')
L4.grid(row=4, column=1, sticky='w')
luas = StringVar()
L5 = Label(my_app, textvariable= luas)
L5.grid(row=4, column=2, sticky= 'w')

def hitung():
           luas.set(int(E3.get())**2)

B1= Button(my_app, text= 'hitung luas', command= hitung)
B1.grid(row=4, column=0, sticky= 'w')

my_app.mainloop()
