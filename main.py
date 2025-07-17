import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

# Database Connection
def connect_to_db():
    return mysql.connector.connect(
        host='localhost',
        user='Use your user name',
        password='Use your user password',
        database='contact_management'
    )

def add_contact():
    f_name = entry_f_name.get()
    l_name = entry_l_name.get()
    address = entry_address.get()
    contact = entry_contact.get()
    email = entry_email.get()
    if f_name and l_name and address and contact and email:
        try:
            conn = connect_to_db()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO contact_register (f_name, l_name, address, contact, email)
                VALUES (%s, %s, %s, %s, %s)
            """, (f_name, l_name, address, contact, email))
            conn.commit()
            messagebox.showinfo("Success", "Contact added successfully!")
            entry_f_name.delete(0, tk.END)
            entry_l_name.delete(0, tk.END)
            entry_address.delete(0, tk.END)
            entry_contact.delete(0, tk.END)
            entry_email.delete(0, tk.END)
            cursor.close()
            conn.close()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")
    else:
        messagebox.showerror("Input Error", "All fields must be filled.")

def display_contacts():
    try:
        conn = connect_to_db()
        cursor = conn.cursor()

        cursor.execute("SELECT f_name, l_name, address, contact, email FROM contact_register")
        rows = cursor.fetchall()
        for row in treeview.get_children():
            treeview.delete(row)
        for row in rows:
            treeview.insert("", tk.END, values=row)

        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

def delete_contact():
    selected_item = treeview.selection()
    if not selected_item:
        messagebox.showwarning("Selection Error", "Please select a contact to delete.")
        return
    selected_contact = treeview.item(selected_item, "values")
    if not selected_contact:
        messagebox.showerror("Error", "No contact data found for the selected item.")
        return

    f_name, l_name, address, contact, email = selected_contact
    confirm = messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete {f_name} {l_name}?")
    if not confirm:
        return

    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute("""
            DELETE FROM contact_register 
            WHERE f_name = %s AND l_name = %s AND address = %s AND contact = %s AND email = %s
        """, (f_name, l_name, address, contact, email))
        conn.commit()

        treeview.delete(selected_item)

        messagebox.showinfo("Success", f"Contact {f_name} {l_name} deleted successfully.")

        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

def dynamic_search(event=None):
    search_term = entry_search.get()
    try:
        conn = connect_to_db()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT f_name, l_name, address, contact, email 
            FROM contact_register 
            WHERE f_name LIKE %s OR l_name LIKE %s
        """, ('%' + search_term + '%', '%' + search_term + '%'))

        rows = cursor.fetchall()

        for row in treeview.get_children():
            treeview.delete(row)

        for row in rows:
            treeview.insert("", tk.END, values=row)

        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

def show_add_section():
    frame_add.place(x=1015, y=0)
    frame_add.lift()

def hide_add_section():
    frame_add.place_forget()

root = tk.Tk()
root.title("Contact Management System")
root.geometry("1000x600")
root.configure(bg="#f5f5f5")

frame_add = tk.Frame(root, bg="white", bd=2, relief=tk.SUNKEN, width=350, height=300)
frame_add.place_forget()

label_f_name = tk.Label(frame_add, text="First Name:", bg="white", font=("Arial", 12))
label_f_name.grid(row=0, column=0, padx=5, pady=5)
entry_f_name = tk.Entry(frame_add, font=("Arial", 12))
entry_f_name.grid(row=0, column=1, padx=5, pady=5)

label_l_name = tk.Label(frame_add, text="Last Name:", bg="white", font=("Arial", 12))
label_l_name.grid(row=1, column=0, padx=5, pady=5)
entry_l_name = tk.Entry(frame_add, font=("Arial", 12))
entry_l_name.grid(row=1, column=1, padx=5, pady=5)

label_address = tk.Label(frame_add, text="Address:", bg="white", font=("Arial", 12))
label_address.grid(row=2, column=0, padx=5, pady=5)
entry_address = tk.Entry(frame_add, font=("Arial", 12))
entry_address.grid(row=2, column=1, padx=5, pady=5)

label_contact = tk.Label(frame_add, text="Contact:", bg="white", font=("Arial", 12))
label_contact.grid(row=3, column=0, padx=5, pady=5)
entry_contact = tk.Entry(frame_add, font=("Arial", 12))
entry_contact.grid(row=3, column=1, padx=5, pady=5)

label_email = tk.Label(frame_add, text="Email:", bg="white", font=("Arial", 12))
label_email.grid(row=4, column=0, padx=5, pady=5)
entry_email = tk.Entry(frame_add, font=("Arial", 12))
entry_email.grid(row=4, column=1, padx=5, pady=5)

button_add_contact = tk.Button(frame_add, text="Add Contact", command=add_contact, width=20, bg="#66b3b3", font=("Arial", 12), activebackground="#339966")
button_add_contact.grid(row=5, columnspan=2, pady=10)

button_hide_add = tk.Button(frame_add, text="Close", command=hide_add_section, width=20, bg="#ff9999", font=("Arial", 12), activebackground="#ff6666")
button_hide_add.grid(row=6, columnspan=2, pady=10)

frame_buttons_with_border = tk.Frame(root, bg="white", bd=2, relief=tk.SUNKEN)
frame_buttons_with_border.pack(side=tk.RIGHT, fill=tk.Y, padx=15)

frame_buttons = tk.Frame(frame_buttons_with_border, bg="white")
frame_buttons.pack()

label_search = tk.Label(frame_buttons, text="Search:", bg="white", font=("Arial", 12))
label_search.pack(pady=5)
entry_search = tk.Entry(frame_buttons, width=20, font=("Arial", 12))
entry_search.pack(pady=5)
entry_search.bind("<KeyRelease>", dynamic_search)

button_add = tk.Button(frame_buttons, text="Add New", command=show_add_section, width=20, bg="skyblue", font=("Arial", 12), activebackground="#339966")
button_add.pack(pady=5)

button_display = tk.Button(frame_buttons, text="Display", command=display_contacts, width=20, bg="skyblue", font=("Arial", 12), activebackground="#339966")
button_display.pack(pady=5)

button_delete = tk.Button(frame_buttons, text="Delete", command=delete_contact, width=20, bg="#ff9999", font=("Arial", 12), activebackground="#ff6666")
button_delete.pack(pady=5)

button_exit = tk.Button(frame_buttons, text="Exit", command=root.destroy, width=20, bg="#ff9999", font=("Arial", 12), activebackground="#ff6666")
button_exit.pack(pady=5)

treeview_frame = tk.Frame(root, bg="white", bd=2, relief=tk.SUNKEN)
treeview_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)

treeview = ttk.Treeview(treeview_frame, columns=("f_name", "l_name", "address", "contact", "email"), show="headings", height=10)
treeview.pack(fill=tk.BOTH, expand=True)
treeview.heading("f_name", text="First Name")
treeview.heading("l_name", text="Last Name")
treeview.heading("address", text="Address")
treeview.heading("contact", text="Contact")
treeview.heading("email", text="Email")

root.mainloop()
