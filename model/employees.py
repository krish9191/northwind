from extension import db
from manager import to_str_date, byte_array_to_json
from datetime import date


class Employee(db.Model):
    __tablename__ = 'employees'
    employee_id = db.Column(db.SmallInteger, primary_key=True, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    title_of_courtesy = db.Column(db.String, nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    hire_date = db.Column(db.Date, nullable=False)
    address = db.Column(db.String, nullable=False)
    city = db.Column(db.String, nullable=False)
    region = db.Column(db.String, nullable=False)
    postal_code = db.Column(db.String, nullable=False)
    country = db.Column(db.String, nullable=False)
    home_phone = db.Column(db.String, nullable=False)
    extension = db.Column(db.String, nullable=False)
    photo = db.Column(db.LargeBinary, nullable=False)
    notes = db.Column(db.Text, nullable=False)
    reports_to = db.Column(db.SmallInteger, nullable=False)
    photo_path = db.Column(db.String, nullable=False)

    @classmethod
    def find_by_id(cls, employee_id):
        return Employee.query.filter(Employee.employee_id == employee_id).first()

    def to_json(self, emp_id):
        emp = Employee.find_by_id(emp_id)
        data = {}
        for key, value in emp.__dict__.items():
            if type(value) == date:
                data[key] = to_str_date(value)
            elif type(value) == bytes:
                data[key] = byte_array_to_json(value)
            else:
                data[key] = value
        data.pop('_sa_instance_state')
        return data


class EmployeeTerritories(db.Model):
    __tablename__ = 'employee_territories'
    employee_id = db.Column(db.SmallInteger, db.ForeignKey('employee_id'), nullable=False)
    territory_id = db.Column(db.String, db.ForeignKey('territory_id'), nullable=False)
