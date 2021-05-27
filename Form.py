
import RangeTree as tree
import csv
from os import close, write
import tkinter as tk
from tkinter import ttk
from tkinter.constants import END
from tkcalendar import Calendar
from tkinter import messagebox
from tkinter import *
Countries: list = []
date1: str = ""
date2: str = ""
dimension: int = 1


def Search():
    '''check if ranges given are integer or not and are valid or not'''

    try:
        int(SB1_from_Entered.get())
        int(SB1_to_Entered.get())
        if int(SB1_from_Entered.get()) > int(SB1_to_Entered.get()):
            messagebox.showinfo(
                "Show error", "Invalid Range for " + SearchBy1.get())
        else:
            global All_countries
            if country.get() == "All":
                All_countries = Countries[1:]
            else:
                temp = []
                temp.append(country.get())
                All_countries = temp
            date1 = from_Entered.get()
            date2 = to_Entered.get()


            if FinalCount == 0:
                '''1-Dimension Searching'''
                # calliing 1-dimensional
                tree.main(All_countries, date1, date2)
            elif FinalCount == 1:
                '''1-Dimension Searching'''
                if SearchBy1.get() == "":
                    col_index1 = None
                    # calliing 1-dimensional
                    tree.main(All_countries, date1, date2)
                else:
                    col_index1 = column_dict[SearchBy1.get()]
                    # calliing 2-dimensional
                    tree.main(All_countries, date1, date2, param1=col_index1,
                              x1=SB1_from_Entered.get(), x2=SB1_to_Entered.get(), dimension=2)

    except ValueError:
        if FinalCount == 1:
            messagebox.showinfo("Show error", "Range should be an integer")


def Calendar_():
    # Create Object (tkinter variable)
    root = tk.Tk()
    root.title("Calendar")
    root.geometry("400x450+750+200")

    # Add Calender
    global cal
    cal = Calendar(root, selectmode='day',date_pattern='dd/MM/yyyy', year=2020, month=5, day=22)
    cal.pack(pady=20)

    # Gets date and put it in from and to text boxes'''
    def getDate():
        date.config(text="Selected Date is: " + cal.get_date())

    def from_date():
        from_Entered.configure(state="normal")
        from_Entered.delete(0, END)
        from_Entered .insert(0, cal.get_date())
        global fromDate
        fromDate = cal.get_date()
        from_Entered.configure(state="disable")

    def to_date():
        to_Entered.configure(state="normal")
        if (cal.get_date() < fromDate):
            messagebox.showinfo("Show error", "Invalid range for date")
        else:
            to_Entered.delete(0, END)
            to_Entered .insert(0, cal.get_date())
        to_Entered.configure(state="disable")
    # Add Buttons (same sequence will appear as per pady)
    tk.Button(root, text="Get Date", command=getDate).pack(pady=5)
    tk.Button(root, text="  From  ", command=from_date).pack(pady=5)
    tk.Button(root, text="   to   ", command=to_date).pack(pady=5)
    date = tk.Label(root, text="")
    date.pack(pady=5)
    lbl = tk.Label(
        root, text="you may view selected date by pressing 'Get Date' button")
    lbl.pack(pady=5)
    root.mainloop()


def searchBy():
    if count_ == 1:
        label_SearchBy.grid(column=10, row=40)
        label_SB1From.grid(column=10, row=60)
        label_SB1To.grid(column=21, row=60)

        SearchBy1.grid(column=20, row=40)
        SearchBy1.current()  # Calling Main()

        '''Integer Range text boxes '''
        SB1_from_Entered.grid(column=20, row=60)
        SB1_to_Entered.grid(column=80, row=60)
    elif count_ > 1:
        messagebox.showinfo("Show error", "No more fields can be added")


count_ = 0
FinalCount = 0


def AddButton():
    '''Monitors the addition of feilds to
     perform required dimensional searching 
     (for Add and Clear button)'''
    global count_
    count_ += 1
    global FinalCount
    FinalCount = count_
    searchBy()


def clearButton():
    ''' to clear form
        enabling all, then erasing
        and resuming back to initial states
        '''
    '''to deacrease dimension on clear'''
    FinalCount = count_ - 1
    country.configure(state="normal")
    to_Entered.configure(state="normal")
    from_Entered.configure(state="normal")
    SearchBy1.configure(state="normal")

    country.delete(0, END)
    country.insert(END, "All")
    to_Entered.delete(0, END)
    from_Entered.delete(0, END)
    from_Entered.insert(END, "3/01/2021")
    to_Entered.insert(END, "5/10/2021")
    SearchBy1.delete(0, END)
    SearchBy1.insert(END, "")
    SB1_from_Entered.delete(0, END)
    SB1_to_Entered.delete(0, END)
    SB1_from_Entered.insert(END, 0)
    SB1_to_Entered.insert(END, 0)

    country.configure(state="readonly")
    to_Entered.configure(state="disable")
    from_Entered.configure(state="disable")
    SearchBy1.configure(state="readonly")


def creatingForm():
    ''' Creating a tinkter variable and 
        defining dimensions for forms'''
    window = tk.Tk()
    window.title("Range Trees")
    window.minsize(670, 500)

    '''variable for background image'''
    bg = PhotoImage(file="Asset.png")
    picture_label = Label(window, image=bg)
    picture_label.place(x=0, y=210)

    mg = PhotoImage(file="Asset1.png")
    picture_label = Label(window, image=mg)
    picture_label.place(x=500, y=-40)

    

    ''' Putting all required Labels'''
    label_country = tk.Label(window, text="\nCountry    \n")
    label_country.grid(column=10, row=1)
    label_dateFrom = tk.Label(window, text="Date")
    label_dateFrom.grid(column=10, row=20)
    label_dateTo = tk.Label(window, text="to      ")
    label_dateTo.grid(column=21, row=20)

    global label_SearchBy, label_SB1From, label_SB1To
    label_SearchBy = tk.Label(window, text="\nSearch by  \n")
    label_SB1From = tk.Label(window, text="Range")
    label_SB1To = tk.Label(window, text="to      ")

    ''' Adding button for Calendar'''
    button_cal = tk.Button(window, text="   Calendar  ", command=Calendar_)
    button_cal.grid(column=180, row=20)
    # to create an add button
    button_add = tk.Button(window, text="Add", command=AddButton)
    button_add.grid(column=180, row=40)
    # opening CSV file using button
    button_search = tk.Button(window, text="Search", command=Search)
    button_search.grid(column=210, row=250)
    # to create a clear button
    button_clear = tk.Button(window, text="Clear", command=clearButton)
    button_clear.grid(column=180, row=160)

    ''' Creating Combo Boxes'''
    '''ComboBox 1: Country'''
    country_ = tk.StringVar()
    global country
    country = ttk.Combobox(window, state="readonly",
                           width=20, textvariable=country_)
    '''populating it'''
    with open("Countries.txt", newline="") as file:
        reader = csv.reader(file)
        for i in reader:
            Countries.append(str(i[0]))
    file.close()
    country['values'] = tuple(Countries)
    country.grid(column=20, row=1)
    country.current(0)

    ''' DateTime Picker 1: Date (from and to)'''
    global from_Entered
    from_ = tk.StringVar()

    from_Entered = ttk.Entry(window,
                             width=20, textvariable=from_)
    from_Entered.insert(END, "3/01/2021")
    from_Entered.configure(state="disable")

    global to_Entered
    to_ = tk.StringVar()
    to_Entered = ttk.Entry(window,  width=20, textvariable=to_)
    to_Entered.insert(END, "5/10/2021")  # default
    to_Entered.configure(state="disable")

    '''default string or selected date will apear'''
    from_Entered .grid(column=20, row=20)
    to_Entered .grid(column=80, row=20)

    global SearchBy1, SB1_from_Entered, SB1_to_Entered

    ''' Combo Box 2: Search By'''
    SearchBy1_ = tk.StringVar()
    SearchBy1 = ttk.Combobox(window, state="readonly",
                             width=30, textvariable=SearchBy1_)

    '''populating Search Boxes using csv file (Columns)'''
    global Columns
    global column_dict
    Columns = []
    column_dict = {}
    with open("CovidData.csv", newline="") as file:
        reader = csv.reader(file)
        for col in reader:
            for i in range(2, len(col)):
                Columns.append(col[i])
                column_dict[col[i]] = i
            break
    file.close()
    SearchBy1['values'] = tuple(Columns)
    SearchBy1.insert(0, "")
    '''Integer Range text boxes '''
    SearchBy1_from = tk.IntVar()
    SearchBy1_to = tk.IntVar()
    SB1_from_Entered = ttk.Entry(window, width=15, textvariable=SearchBy1_from)
    SB1_to_Entered = ttk.Entry(window, width=15, textvariable=SearchBy1_to)
    window.mainloop()


def main():
    creatingForm()
main()

