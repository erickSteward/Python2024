# transactions_module.py
class Transaction:
    def __init__(self, transaction_id, date, type, category, amount, description):
        self.transaction_id = transaction_id
        self.date = date
        self.type = type
        self.category = category
        self.amount = amount
        self.description = description


class TransactionManager:
    def __init__(self, crud_operation):
        self.crud_operation = crud_operation

    def add_transaction(self, transaction):
        query = "INSERT INTO transactions (date, type, category, amount, description) VALUES (%s, %s, %s, %s, %s)"
        self.crud_operation.create(query, (transaction.date, transaction.type, transaction.category, transaction.amount, transaction.description))

    def view_transactions(self):
        query = "SELECT * FROM transactions"
        return self.crud_operation.read(query)

    def delete_transaction(self, transaction_id):
        query = "DELETE FROM transactions WHERE transaction_id = %s"
        self.crud_operation.delete(query, (transaction_id,))
