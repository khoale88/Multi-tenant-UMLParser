from flask import Flask, request, url_for, Response, make_response,json,abort
from flask_sqlalchemy import SQLAlchemy
from model import db, Expenses,CreateDB,DropDB    #,DropDB,CreateDB

app = Flask(__name__)

@app.route('/v1/expenses',methods=['POST'])
def create_expense():
    if request.method == 'POST':
        json_request = json.loads(request.data)
        name = json_request['name']
        email = json_request['email']
        category = json_request['category']
        description = json_request['description']
        link = json_request['link']
        estimated_costs = json_request['estimated_costs']
        submit_date = json_request['submit_date']
        status = status_generator()
        decision_date = decision_date_update()
        expense = Expenses(name,email,category,description,link,estimated_costs,submit_date,status,decision_date)
        db.session.add(expense)
        db.session.commit()  
        response = make_response(str(expense))
        response.status_code = 201
    return response

def status_generator():
    return 'pending'

def decision_date_update():
    return ''

@app.route('/v1/expenses/<int:expense_id>',methods=['GET','PUT','DELETE'])
def show_expense(expense_id):
    if request.method == 'GET':
        expense = Expenses.query.get_or_404(expense_id)
        response = make_response(str(expense))
        #response.status_code = 200 #accepted

    if request.method == 'PUT':
        expense = Expenses.query.get_or_404(expense_id)
        response = make_response()
        response.status_code = 202
        json_request = json.loads(request.data)
        expense.estimated_costs = json_request['estimated_costs']
        db.session.commit()

    if request.method == 'DELETE':
        expense = Expenses.query.get_or_404(expense_id)
        response = make_response()
        db.session.delete(expense)
        db.session.commit()
        response.status_code = 204

    return response

if __name__ == '__main__':
    CreateDB()       
    db.create_all()
    app.run(debug=True,host='0.0.0.0')