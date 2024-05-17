from datetime import datetime

from flask import Flask, render_template, request, redirect, url_for, make_response, session
from tools import DatabaseWorker

app = Flask(__name__)
app.secret_key = "23yerfgjuehib2qrf"


@app.route('/food/<int:food_id>', methods = ['GET', 'POST'])
def get_food(food_id):
    db = DatabaseWorker('database.db')
    food = db.search(f"SELECT * FROM foods where id = {food_id}", multiple=False)
    reviews = db.search(f"SELECT * FROM reviews where food_id = {food_id}", multiple=True)
    if request.method == "POST":
        #The form was submitted with the new review
        date = datetime.now().strftime("%Y/%b/%d")
        comment = request.form.get('comment')
        stars = request.form.get('stars')
        print(stars)
        query = f"""INSERT INTO reviews (food_id, comment, stars, date) VALUES 
        ({food_id}, '{comment}', {stars},'{date}')"""
        print(query)
        db.run_query(query)
        db.close()
        return redirect(url_for('get_food', food_id=food_id))
    db.close()
    return render_template('food.html', food=food, reviews=reviews)

@app.route('/food/<int:food_id>/review/<int:review_id>/delete')
def delete_review(review_id, food_id):
    db = DatabaseWorker('database.db')
    db.run_query(f"DELETE FROM reviews where id = {review_id}")
    db.close()
    return redirect(url_for('get_food', food_id= food_id))

@app.route('/food/<int:food_id>/review/<int:review_id>/edit', methods = ['GET', 'POST'])
def edit_review(review_id, food_id):
    db = DatabaseWorker('database.db')
    food = db.search(f"SELECT * FROM foods where id = {food_id}", multiple=False)
    reviews = db.search(f"SELECT * FROM reviews where food_id = {food_id}", multiple=True)
    review_to_edit = db.search(f"SELECT * FROM reviews where id = {review_id}", multiple=False)
    comments = review_to_edit[1]
    stars = review_to_edit[3]
    if request.method == 'POST': # update the review and redirect to the food page
        comment = request.form.get('comment')
        stars = request.form.get('stars')
        db.run_query(f"UPDATE reviews SET comment = '{comment}', stars = {stars} WHERE id = {review_id}")
        db.close()
        return redirect(url_for('get_food', food_id=food_id))


    db.close()
    return render_template("food.html", food=food, reviews= reviews, comments=comments, stars=stars)

@app.route('/food/all')
def get_all_food():
    user = 'guest'
    if request.cookies.get('user_id'):
        user_id = session['user_id']
        users = {1:'bob', 2:'alice'}
        #query the database to get the user info
        user = users[int(user_id)]

    #1-query the database, get all foods
    #2-return a template(html) with the variable results
    db = DatabaseWorker('database.db')
    results = db.search("SELECT * FROM foods", multiple=True)
    db.close()
    return render_template('foods.html', foods=results)

@app.route('/profile')
def profile():
    # if request.cookies.get('user_id'):
    if session['user_id']:
        user_id = session['user_id']

        # user_id = request.cookies.get('user_id')
        users = {1:'bob', 2:'alice'}
        #query the database to get the user info
        user = users[int(user_id)]

        return f'<h1>Hello {user}</h1>'

    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    response = make_response(redirect(url_for('login')))
    response.set_cookie('user_id', '', expires=0)
    return response


@app.route('/', methods = ['GET', 'POST'])
def login():  # put application's code here
    if request.method == 'POST':
        uname = request.form.get('uname')
        password = request.form.get('psw')

        #check database for user and compare hash of password

        if uname == "bob":
            #valid login, create a cookie
            user_id = 1
            # response = make_response(redirect(url_for('get_all_food')))
            # response.set_cookie('userID', f"{user_id}")

            session['user_id'] = user_id

            return (redirect(url_for('get_all_food')))

    return render_template('login.html')



if __name__ == '__main__':
    app.run(Debug = True)
