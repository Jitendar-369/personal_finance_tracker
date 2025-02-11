# Personal Finance Tracker

## Overview

The **Personal Finance Tracker** is a simple web application built using Flask and SQLAlchemy to help users manage and track their personal finances. The app allows users to add, edit, and delete transactions, view transaction history, and categorize their expenses for better financial planning.

## Features

- **Track Transactions**: Add, view, and delete transactions with details like date, category, amount, and description.
- **Search Transactions**: Filter transactions by date, category, or description.
- **Responsive UI**: Simple and easy-to-use interface for seamless user experience.
- **Database Integration**: SQLite database to store transaction data securely.

## Technologies Used

- **Flask**: A lightweight web framework for Python to handle routing and server-side logic.
- **SQLAlchemy**: ORM (Object Relational Mapping) for interacting with the SQLite database.
- **SQLite**: A lightweight relational database used for data storage.
- **Bootstrap**: Front-end framework to ensure the app is mobile-responsive and user-friendly.
- **Jinja2**: Templating engine used for rendering HTML dynamically in Flask.

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/personal-finance-tracker.git
Navigate to the project directory:

cd personal-finance-tracker
Create and activate a virtual environment:


python -m venv venv
# For Windows:
venv\Scripts\activate
# For macOS/Linux:
source venv/bin/activate
Install the required dependencies:


pip install -r requirements.txt
Set up the database: In the Python shell or a script, run:

from app import db
db.create_all()
Run the Flask application:

python app.py
Open the app in a browser: Go to http://127.0.0.1:5000 to access the Personal Finance Tracker.

Usage
Home Page: Displays a list of all transactions with an option to add new ones.
Add Transaction: Users can add a transaction by entering the date, category, amount, and a description.
Search Transactions: Use the search bar to filter transactions based on date, category, or description.
Delete Transaction: Click on the delete icon next to a transaction to remove it.

Contributing
If you'd like to contribute to this project, feel free to fork the repository, make changes, and create a pull request. Contributions are welcome to enhance the app's features or improve the code quality.

License
This project is open-source and available under the MIT License. See the LICENSE file for more details.

This version should be ready to copy-paste into your README.md file.
