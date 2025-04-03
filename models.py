from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Cartridge(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)  # ФИО
    department = db.Column(db.String(100), nullable=False)  # Подразделение
    location = db.Column(db.String(100), nullable=False)  # Объект
    cartridge_model = db.Column(db.String(100), nullable=False)  # Модель картриджа
    start_date = db.Column(db.Date, nullable=False)  # Дата начала
    end_date = db.Column(db.Date)  # Дата окончания (может быть NULL)
    quantity = db.Column(db.Integer, nullable=False)  # Количество картриджей