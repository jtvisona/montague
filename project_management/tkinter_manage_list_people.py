import tkinter as tk
from tkinter import messagebox

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Person Manager")

        self.people = []

        self.name_label = tk.Label(root, text="Name:")
        self.name_label.grid(row=0, column=0)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1)

        self.age_label = tk.Label(root, text="Age:")
        self.age_label.grid(row=1, column=0)
        self.age_entry = tk.Entry(root)
        self.age_entry.grid(row=1, column=1)

        self.add_button = tk.Button(root, text="Add Person", command=self.add_person)
        self.add_button.grid(row=2, column=0, columnspan=2)

        self.view_button = tk.Button(root, text="View People", command=self.view_people)
        self.view_button.grid(row=3, column=0, columnspan=2)

        self.delete_button = tk.Button(root, text="Delete Person", command=self.delete_person)
        self.delete_button.grid(row=4, column=0, columnspan=2)

    def add_person(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        if name and age:
            self.people.append(Person(name, age))
            messagebox.showinfo("Success", "Person added successfully!")
            self.name_entry.delete(0, tk.END)
            self.age_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter both name and age.")

    def view_people(self):
        if self.people:
            people_str = "\n".join([f"Name: {p.name}, Age: {p.age}" for p in self.people])
            messagebox.showinfo("People", people_str)
        else:
            messagebox.showinfo("No People", "No people to display.")

    def delete_person(self):
        name = self.name_entry.get()
        if name:
            self.people = [p for p in self.people if p.name != name]
            messagebox.showinfo("Success", "Person deleted successfully!")
            self.name_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter the name of the person to delete.")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
