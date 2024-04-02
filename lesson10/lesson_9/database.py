import allure
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class Employee(Base):
    """
    Класс представляет таблицу Employee в базе данных.

    Атрибуты:
    - id: ID сотрудника.
    - first_name: Имя сотрудника.
    - last_name: Фамилия сотрудника.
    """

    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)


DATABASE_URL = "postgresql+psycopg2://x_clients_user:x7ngHjC1h08a85bELNifgKmqZa8KIR40@dpg-cn1542en7f5s73fdrigg-a.frankfurt-postgres.render.com/x_clients_xxet"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)


def get_db_session():
    """
    Получение сессии базы данных.

    Возвращается:
    - Session: Сессия базы данных.
    """
    session = Session()
    return session


def add_employee(session, employee_data):
    """
    Добавление нового сотрудника в базу данных.

    Параметры:
    - session (Session): Сессия базы данных.
    - employee_data (dict): Данные о сотруднике.
    """
    new_employee = Employee(id=employee_data['id'], first_name=employee_data['firstName'], last_name=employee_data['lastName'])
    session.add(new_employee)
    session.commit()


def delete_employee(session, employee_id):
    """
    Удаление сотрудника из базы данных по ID.

    Параметры:
    - session (Session): Сессия базы данных.
    - employee_id (int): ID сотрудника.
    """
    employee_to_delete = session.query(Employee).filter(Employee.id == employee_id).first()
    if employee_to_delete:
        session.delete(employee_to_delete)
        session.commit()


@allure.step("Test Adding and Deleting Employee")
def test_add_and_delete_employee(db_session, fake_employee_data):
    """
    Тест для добавления и удаления сотрудника из базы данных.

    Параметры:
    - db_session: Сеанс работы с базой данных.
    - fake_employee_data: Поддельные данные для сотрудника.
    """
    with allure.step("Добавление сотрудника в базу данных"):
        add_employee(db_session, fake_employee_data)

    with allure.step("Проверка данных о сотрудниках"):
        employee_data = db_session.query(Employee).filter(Employee.id == fake_employee_data['id']).first()
        assert employee_data.first_name == fake_employee_data['firstName']
        assert employee_data.last_name == fake_employee_data['lastName']

    with allure.step("Удаление сотрудника из базы данных"):
        delete_employee(db_session, fake_employee_data['id'])

    with allure.step("Проверка удаления сотрудника из базы данных"):
        employee_data = db_session.query(Employee).filter(Employee.id == fake_employee_data['id']).first()
        assert employee_data is None
