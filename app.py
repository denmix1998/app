from flask import Flask, render_template, request, redirect, url_for
from models import db, Cartridge
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cartridges.db'  # Для хостинга замените на вашу БД
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add', methods=['GET', 'POST'])
def add_cartridge():
    if request.method == 'POST':
        full_name = request.form['full_name']
        department = request.form['department']
        location = request.form['location']
        cartridge_model = request.form['cartridge_model']
        start_date = datetime.strptime(request.form['start_date'], '%Y-%m-%d').date()
        end_date_str = request.form.get('end_date')
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date() if end_date_str else None
        quantity = int(request.form['quantity'])

        new_cartridge = Cartridge(
            full_name=full_name,
            department=department,
            location=location,
            cartridge_model=cartridge_model,
            start_date=start_date,
            end_date=end_date,
            quantity=quantity
        )

        db.session.add(new_cartridge)
        db.session.commit()

        return redirect(url_for('view_cartridges'))

    return render_template('add.html')


@app.route('/view')
def view_cartridges():
    cartridges = Cartridge.query.all()
    return render_template('view.html', cartridges=cartridges)


if __name__ == 'main':
    app.run(debug=True)