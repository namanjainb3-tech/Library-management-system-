# 📚 Library Management System

A console-based Library Management System built using Python and MySQL.

This project helps manage books, customer records, memberships, book issuing, and return operations through a menu-driven interface.

---

## 🚀 Features

### Book Management

* Add new books
* Remove books
* View all books
* Search books by:

  * Book Name
  * Author
  * Publication
  * Availability Status

### Customer Management

* Register new customers
* Store customer details
* Track issued books
* Membership management

### Book Issue & Return

* Issue books to customers
* Check availability before issuing
* Automatically update book status
* Return books and update records

### Membership System

* 1 Month Plan – ₹799
* 6 Months Plan – ₹3999
* 1 Year Plan – ₹6999

### Database Storage

All records are permanently stored in MySQL database.

---

## 🛠️ Technologies Used

* Python 3
* MySQL
* mysql-connector-python

---

## 📂 Database Structure

### customer_details

| Column      | Type    |
| ----------- | ------- |
| C_id        | Integer |
| C_Name      | Varchar |
| Ph_no       | Varchar |
| Book_issued | Integer |
| Issue_date  | Varchar |
| Return_Date | Varchar |
| Member      | Char    |
| Membership  | Integer |

### book_details

| Column      | Type    |
| ----------- | ------- |
| b_id        | Integer |
| b_name      | Varchar |
| publication | Varchar |
| author      | Varchar |
| status      | Varchar |
| reviews     | Decimal |

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/Library-Management-System.git

cd Library-Management-System
```

### 2. Install Dependencies

```bash
pip install mysql-connector-python
```

### 3. Configure MySQL

Update credentials inside the code:

```python
mydb = msq.connect(
    host="localhost",
    user="root",
    passwd="YOUR_PASSWORD"
)
```

### 4. Run

```bash
python library_management.py
```

---

## 📸 Workflow

1. Start Program
2. View Menu
3. Add/Remove Books
4. Issue Books
5. Manage Memberships
6. Return Books
7. Exit

---

## Future Improvements

* GUI using Tkinter
* Login Authentication
* Fine Calculation
* Book Categories
* ISBN Support
* Admin Dashboard
* Email Notifications
* Date Validation
* Search Optimization

---

## Author

Naman Jain

CSE Student, IIIT Sonepat

Passionate about Software Development, AI, and Building Real-World Projects.
