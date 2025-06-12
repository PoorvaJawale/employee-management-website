from flask import Flask, render_template, request, redirect,flash, url_for
from models import db, Data 
from models import User
from flask import session
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.secret_key='SECRET_KEY'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'connect_args': {'check_same_thread': False}}

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name'].strip()
        email = request.form['email'].strip()
        password = request.form['password'].strip()

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email already registered', 'danger')
            return redirect(url_for('register'))

        new_user = User(name, email, password)
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful. Please login.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

    
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email'].strip()
        password = request.form['password'].strip()

        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):
            session['user_id'] = user.id
            session['user_name'] = user.name
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid credentials', 'danger')
            return redirect(url_for('login'))

    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    employees = Data.query.all()
    return render_template('index.html', employees=employees)

@app.route('/logout')
def logout():
    session.clear()
    flash("You have been logged out.")
    return redirect(url_for('login'))

@app.route("/add", methods=["GET", "POST"])
def add_data():
    if 'user_id' not in session:
        flash("Login required", "danger")
        return redirect(url_for('login'))

    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        new_entry = Data(name=name, email=email, phone=phone)
        db.session.add(new_entry)
        db.session.commit()

        flash("Employee Inserted Successfully", "success")
        return redirect(url_for('dashboard'))
    
    return render_template("index.html")  


@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    if 'user_id' not in session:
        flash("Login required", "danger")
        return redirect(url_for('login'))

    my_data = Data.query.get_or_404(id)

    if request.method == 'POST':
        my_data.name = request.form['name']
        my_data.email = request.form['email']
        my_data.phone = request.form['phone']
        db.session.commit()
        flash("Employee Updated Successfully", "success")
        return redirect(url_for('dashboard'))
    

@app.route("/delete/<int:id>")
def delete(id):
    if 'user_id' not in session:
        flash("Login required", "danger")
        return redirect(url_for('login'))

    my_data=Data.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Employee Deleted Successfully")
    return redirect(url_for('dashboard'))

if __name__=='__main__':
    app.run(debug=True)