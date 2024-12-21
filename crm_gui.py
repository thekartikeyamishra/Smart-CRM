import tkinter as tk
from tkinter import ttk, messagebox, dialog
from utils.data_handler import load_data, save_data, add_customer, delete_customer, DATA_PATH


class CRMApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Smart CRM for MSMEs")

        self.data = load_data()

        self.tree = ttk.Treeview(self.root, columns=("ID", "Name", "Contact", "Purchase History", "Notes"), show="headings")
        self.tree.heading("ID", text="Customer ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Contact", text="Contact")
        self.tree.heading("Purchase History", text="Purchase History")
        self.tree.heading("Notes", text="Notes")
        self.tree.pack(pady=10, fill=tk.BOTH, expand= True)

        self.refresh_tree()

        tk.Button(self.root, text="Add Customer", command=self.add_customer_dialog).pack(side= tk.LEFT, padx=5, pady=5)
        tk.Button(self.root, text="Delete Customer", command=self.delete_customer).pack(side= tk.LEFT, padx=5, pady=5)
        tk.Button(self.root, text="Export Data", command=self.export_data).pack(side= tk.LEFT, padx=5, pady=5)

    def refresh_tree(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for _, row in self.data.iterrows():
            self.tree.insert(" ", tk.END, values=row.tolist())

    def add_customer_dialog(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Add Customer")

        tk.Label(dialog, text="Customer ID:").pack(pady=5)
        customer_id = tk.Entry(dialog)
        customer_id.pack(pady =5)

        tk.Label(dialog, text="Name:").pack(pady=5)
        name = tk.Entry(dialog)
        name.pack(pady=5)

        tk.Label(dialog, text="Contact :").pack(pady=5)
        contact = tk.Entry(dialog)
        contact.pack(pady=5)

        tk.Label(dialog, text="Purchase History:").pack(pady=5)
        purchase_history = tk.Entry(dialog)
        purchase_history.pack(pady=5)

        tk.Label(dialog, text="Notes:").pack(pady=5)
        notes = tk.Entry(dialog)
        notes.pack(pady=5)

    def save_customer(customer_id=None, name=None, contact=None, purchase_history=None, notes=None, self=None):
        customer = {
            "Customer ID": customer_id.get(),
            "Name" : name.get(),
            "Contact": contact.get(),
            "Purchase History": purchase_history.get(),
            "Notes": notes.get()

        }
        self.data = add_customer(self.data, customer)
        save_data(self.data)
        self.refresh_tree()
        dialog.destroy()

    tk.Button(dialog, text="Save", command=save_customer).pack(pady=5)


    def delete_customer(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "No customer selected!")
            return
        customer_id = self.tree.item(selected_item[0])["values"][0]
        self.data = delete_customer(self.data, customer_id)
        save_data(self.data)
        self.refresh_tree()

    def export_data(self):
        save_data(self.data)
        messagebox.showinfo("Success", f"Data exported to {DATA_PATH}!")

    def run(self):
        self.root.mainloop()