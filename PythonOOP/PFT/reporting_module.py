

# report_module.py
class ReportGenerator:
    def __init__(self, crud_operation):
        self.crud_operation = crud_operation

    def generate_income_report(self):
        query = "SELECT * FROM transactions WHERE type = 'Income'"
        return self.crud_operation.read(query)

    def generate_expense_report(self):
        query = "SELECT * FROM transactions WHERE type = 'Expense'"
        return self.crud_operation.read(query)

    def generate_summary_report(self):
        query = "SELECT type, SUM(amount) as total_amount FROM transactions GROUP BY type"
        return self.crud_operation.read(query)
