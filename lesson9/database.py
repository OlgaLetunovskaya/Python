from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

DATABASE_URL = "postgresql+psycopg2://x_clients_user:x7ngHjC1h08a85bELNifgKmqZa8KIR40@dpg-cn1542en7f5s73fdrigg-a.frankfurt-postgres.render.com/x_clients_xxet"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def get_db_session():
    session = Session()
    return session

def add_employee(session, employee_data):
    new_employee = Employee(id=employee_data['id'], first_name=employee_data['firstName'], last_name=employee_data['lastName'])
    session.add(new_employee)
    session.commit()

def delete_employee(session, employee_id):
    employee_to_delete = session.query(Employee).filter(Employee.id == employee_id).first()
    if employee_to_delete:
        session.delete(employee_to_delete)
        session.commit()
