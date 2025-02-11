from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///transactions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Transaction model
class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(80), nullable=False)
    category = db.Column(db.String(80), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(200))

    def __repr__(self):
        return f'<Transaction {self.id}>'

# Home route - display all transactions
@app.route('/')
def home():
    transactions = Transaction.query.all()  # Get all transactions
    return render_template('index.html', transactions=transactions)

# Add transaction route
@app.route('/add', methods=['GET', 'POST'])
def add_transaction():
    if request.method == 'POST':
        date = request.form['date']
        category = request.form['category']
        amount = float(request.form['amount'])
        description = request.form['description']
        
        new_transaction = Transaction(date=date, category=category, amount=amount, description=description)
        db.session.add(new_transaction)
        db.session.commit()

        return redirect('/')
    
    return render_template('add_transaction.html')

# Delete transaction route
@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete_transaction(id):
    transaction_to_delete = Transaction.query.get(id)  # Find transaction by ID
    if transaction_to_delete:
        db.session.delete(transaction_to_delete)  # Delete the transaction
        db.session.commit()  # Commit the changes to the database
    return redirect('/')  # Redirect to the home page after deletion

# Initialize the database
with app.app_context():
    db.create_all()  # Create the database tables

if __name__ == '__main__':
    app.run(debug=True)
