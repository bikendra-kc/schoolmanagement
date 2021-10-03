from tkinter import *
import sqlite3


def root():
    root = Tk()
    root.title('student management')

    # ================== Create a databases ==================
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    # Create table
    '''
    c.execute(""" CREATE TABLE addresses(
          first_name text,
          last_name text,
          roll_no integer,
          address text,
          section text,
          contact integer

    ) """)
    '''

    # ============= Create submit button =====================
    def add():

        conn = sqlite3.connect('address_book.db')

        c = conn.cursor()

        # ============== Insert into table ====================
        c.execute("INSERT INTO addresses VALUES (:e1, :e2, :e3, :e4, :e5, :e6)", {
            'e1': e1.get(),
            'e2': e2.get(),
            'e3': e3.get(),
            'e4': e4.get(),
            'e5': e5.get(),
            'e6': e6.get()
        })

        conn.commit()

        conn.close()

        # ============= clearing the enteries ====================
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e5.delete(0, END)
        e6.delete(0, END)

    def show():
        conn = sqlite3.connect('address_book.db')

        c = conn.cursor()

        c.execute("SELECT *, oid FROM addresses")

        records = c.fetchall()
        print(records)

        print_record = ''
        for record in records:
            print_record += str(record[0]) + ' ' + str(record[1]) + ' ' + str(record[2]) + ' ' + str(
                record[3]) + ' ' + str(record[4]) + ' ' + str(record[5]) + ' ' + str(record[6]) + "\n"
        query_label = Label(frame1, text=print_record, bg="grey", fg="red", font=("times", "18", "bold"))
        query_label.grid(row=1, column=1, columnspan=2)

        conn.commit()
        conn.close()

    def delete():
        conn = sqlite3.connect('address_book.db')

        c = conn.cursor()

        c.execute("DELETE from addresses WHERE oid = " + del_entry.get())
        print("deleted sucessfully")

        c.execute("SELECT *, oid FROM addresses")

        records = c.fetchall()
        print(records)

        print_record = ''
        for record in records:
            print_record += str(record[0]) + ' ' + str(record[1]) + ' ' + str(record[2]) + ' ' + str(
                record[3]) + ' ' + str(record[4]) + ' ' + str(record[5]) + ' ' + str(record[6]) + "\n"
        query_label = Label(frame1, text=print_record, bg="grey", fg="red", font=("times", "18", "bold"))
        query_label.grid(row=1, column=1, columnspan=2)

        conn.commit()
        conn.close()

    def edit():

        global editor

        editor = Tk()
        editor.title('Update Data')
        editor.geometry('300x480')

        conn = sqlite3.connect('address_book.db')

        c = conn.cursor()

        record_id = del_entry.get()

        c.execute("SELECT * FROM addresses WHERE oid=" + record_id)

        records = c.fetchall()

        # ========================== Creating global variable for all text boxes =====================
        global first_name_editor
        global last_name_editor
        global roll_no_editor
        global address_editor
        global section_editor
        global contact_editor

        first_name_editor = Entry(editor, width=30)
        first_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))

        last_name_editor = Entry(editor, width=30)
        last_name_editor.grid(row=1, column=1)

        roll_no_editor = Entry(editor, width=30)
        roll_no_editor.grid(row=2, column=1)

        address_editor = Entry(editor, width=30)
        address_editor.grid(row=3, column=1)

        section_editor = Entry(editor, width=30)
        section_editor.grid(row=4, column=1)

        contact_editor = Entry(editor, width=30)
        contact_editor.grid(row=5, column=1)

        # ================ creating the labels ====================
        f_name_label = Label(editor, text="First Name")
        f_name_label.grid(row=0, column=0, pady=(10, 0))

        l_name_label = Label(editor, text="Last Name")
        l_name_label.grid(row=1, column=0)

        roll_label = Label(editor, text="Roll No")
        roll_label.grid(row=2, column=0)

        address_label = Label(editor, text="Adress")
        address_label.grid(row=3, column=0)

        section_label = Label(editor, text="Section")
        section_label.grid(row=4, column=0)

        contact_label = Label(editor, text="Contact")
        contact_label.grid(row=5, column=0)

        for record in records:
            first_name_editor.insert(0, record[0])
            last_name_editor.insert(0, record[1])
            roll_no_editor.insert(0, record[2])
            address_editor.insert(0, record[3])
            section_editor.insert(0, record[4])
            contact_editor.insert(0, record[5])

        # Create a update button
        edit_btn = Button(editor, text=" SAVE ", command=update)
        edit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=125)

    def update():
        conn = sqlite3.connect('address_book.db')
        c = conn.cursor()
        record_id = del_entry.get()
        c.execute(""" UPDATE addresses SET
             first_name = :first,
             last_name = :last,
             roll_no = :roll_no,
             address = :address,
             section = :section,
             contact = :contact
             WHERE oid = :oid""",
                  {'first': first_name_editor.get(),
                   'last': last_name_editor.get(),
                   'roll_no': roll_no_editor.get(),
                   'address': address_editor.get(),
                   'section': section_editor.get(),
                   'contact': contact_editor.get(),
                   'oid': record_id
                   }
                  )
        conn.commit()
        conn.close()

    frame1 = Frame(root, relief=RIDGE, bg="grey")
    frame1.place(x=770, y=0, height=500, width=500)

    label_1 = Label(frame1, text="Students Details :-", font=("times", "25", "bold"), bg="grey")
    label_1.grid(row=0, column=1)
    # ======================== Create text boxes ==============================
    e1 = Entry(root, font=("times", "25", "bold"), width=30)
    e1.grid(row=0, column=1, padx=20)

    e2 = Entry(root, font=("times", "25", "bold"), width=30)
    e2.grid(row=1, column=1)

    e3 = Entry(root, font=("times", "25", "bold"), width=30)
    e3.grid(row=2, column=1)

    e4 = Entry(root, font=("times", "25", "bold"), width=30)
    e4.grid(row=3, column=1)

    e5 = Entry(root, font=("times", "25", "bold"), width=30)
    e5.grid(row=4, column=1)

    e6 = Entry(root, font=("times", "25", "bold"), width=30)
    e6.grid(row=5, column=1)

    del_entry = Entry(root, font=("times", "25", "bold"), width=30)
    del_entry.grid(row=8, column=1)

    # ====================== Create textbox labels =====================
    f_name = Label(root, font=("times", "25", "bold"), text="First Name")
    f_name.grid(row=0, column=0)

    l_name = Label(root, font=("times", "25", "bold"), text="Last Name")
    l_name.grid(row=1, column=0)

    roll_no_label = Label(root, font=("times", "25", "bold"), text="Roll no")
    roll_no_label.grid(row=2, column=0)

    address = Label(root, font=("times", "25", "bold"), text="Address")
    address.grid(row=3, column=0)

    section_label = Label(root, font=("times", "25", "bold"), text="Section")
    section_label.grid(row=4, column=0)

    contact_label = Label(root, font=("times", "25", "bold"), text="Contact")
    contact_label.grid(row=5, column=0)

    del_label = Label(root, font=("times", "25", "bold"), text="Delete ID")
    del_label.grid(row=8, column=0)

    # ================================ Create submit button =================================

    submit_btn = Button(root, text="Add Records", command=add)
    submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

    query_btn = Button(root, text="Show Records", command=show)
    query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

    del_btn = Button(root, text="Delete", command=delete)
    del_btn.grid(row=9, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

    update_btn = Button(root, text="Update", command=edit)
    update_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

    conn.commit()

    conn.close()

    mainloop()
