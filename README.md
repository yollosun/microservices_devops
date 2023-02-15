Task:
Create a new table: cleaning_order, with the following columns:
- id (int, primary key)
- objectName (varchar)
- description (varchar)
- deadline (date) default now
- status (int) default "created"

Services: 
1. Create a new transaction every minute.
1. Read all transactions from the database and check the deadline, if deadline is over change status to "overdue"

Instructions:

Inserting goes like this:
```python
cursor = conn.cursor()
    cursor.execute("INSERT INTO expenses (type, description, amount) VALUES (%s, %s, %s)", (expense.type, 
expense.description, expense.amount))
conn.commit()
```
    
Selecting goes like this:
```python
cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()
    return [{
        "id": expense[0],
        "type": expense[1],
        "description": expense[2],
        "amount": expense[3],
        "created": expense[4]
    } for expense in expenses
    ]
```