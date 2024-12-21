# Smart-CRM
For the next 15 days, I'll be creating and sharing 15 projects – one per day! Free versions will be open to all on my GitHub, and a low-cost paid version will be available too. Can't wait to hear your thoughts!
Smart CRM for MSMEs, a simple and effective tool for small and medium-sized enterprises (MSMEs) to manage customer interactions and streamline customer relationship management.

**Smart CRM for MSMEs: Basic Version**

**Smart CRM for MSMEs**, a simple and effective tool for small and medium-sized enterprises (MSMEs) to manage customer interactions and streamline customer relationship management. This **basic version** focuses on usability and essential CRM functionalities to help businesses grow.

---

### **Features of the Basic Version**

1. **Customer Management**:
   - Add, update, and delete customer records.
   - Store customer details like name, contact information, and purchase history.

2. **Interaction Tracking**:
   - Record notes or follow-ups for customer interactions.

3. **Data Export**:
   - Export customer records to a CSV file for offline use.

4. **Simple GUI**:
   - A clean and user-friendly interface built with **Tkinter**, accessible for non-technical users.

---

### **File and Folder Structure**

```bash
SmartCRM/
├── data/
│   ├── customers.csv             # CSV file to store customer data
├── utils/
│   ├── __init__.py               # Initializes the utils module
│   ├── data_handler.py           # Handles customer data operations
├── gui/
│   ├── __init__.py               # Initializes the GUI module
│   ├── crm_gui.py                # GUI implementation using Tkinter
├── main.py                       # Entry point for the application
├── requirements.txt              # Dependencies required for the project
├── README.md                     # Documentation for the project
```

---

### **How It Works**

1. **Add Customers**:
   - Enter customer details like ID, name, contact information, purchase history, and notes.

2. **View and Manage Records**:
   - Use the GUI to view, update, or delete customer records in a table format.

3. **Export Data**:
   - Save all customer records to a `.csv` file for backup or offline use.

4. **Simple Interface**:
   - The GUI makes it easy for anyone to manage customer data without technical knowledge.

---

### **Code Implementation**

#### **1. `data_handler.py`**

Handles CRUD operations for customer data stored in a CSV file.

#### **2. `crm_gui.py`**

Implements a Tkinter-based GUI for customer management and interaction tracking.

#### **3. `main.py`**

The entry point for the application, initializing the GUI and starting the CRM tool.

---

### **Installation Instructions**

1. **Clone the Repository**:
   ```bash
   git clone [https://github.com/thekartikeyamishra/Smart-CRM](https://github.com/thekartikeyamishra/Smart-CRM.git
   cd SmartCRM
   ```

2. **Set Up Virtual Environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   ```bash
   python main.py
   ```

---

### **Future Enhancements**

1. **Advanced Analytics**:
   - Gain insights into customer behavior and interactions.

2. **Reminders and Notifications**:
   - Set reminders for follow-ups and automate customer notifications.

3. **Integration with Messaging Systems**:
   - Connect with WhatsApp, email, or SMS for seamless communication.

4. **Mobile-Friendly Version**:
   - Make the CRM accessible on mobile devices.

---

### **Contributions**

Contributions are welcome! Fork the repository, submit pull requests, or open issues for any bugs or feature requests.

---

### **Support**

If you encounter any issues or have suggestions, feel free to:
- Open an issue on GitHub.
- Contact me directly for feedback or queries.

---

### **Call to Action**

If you find this project useful:
- ⭐ **Star this repository** on GitHub: [Smart CRM for MSMEs](https://github.com/thekartikeyamishra/Smart-CRM)  
- Share this project with your network to help small businesses manage customers better.

---

### **Let’s Build Together**

This basic version is just the beginning! Together, let’s create tools that empower MSMEs to thrive in today’s competitive world. Your feedback and ideas are always welcome. 🚀

Happy coding! 💻
