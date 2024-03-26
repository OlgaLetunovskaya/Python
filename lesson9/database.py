import psycopg2

DATABASE_URL = "postgres://x_clients_user:x7ngHjC1h08a85bELNifgKmqZa8KIR40@dpg-cn1542en7f5s73fdrigg-a.frankfurt-postgres.render.com/x_clients_xxet"

def get_db_connection(database_url=DATABASE_URL):
    return psycopg2.connect(database_url)

def add_employee(connection, employee_data):
    with connection.cursor() as cursor:
        cursor.execute(
            "INSERT INTO employees (id, first_name, last_name) VALUES (%s, %s, %s)",
            (employee_data['id'], employee_data['firstName'], employee_data['lastName'])
        )
        connection.commit()

def delete_employee(connection, employee_id):
    with connection.cursor() as cursor:
        cursor.execute(
            "DELETE FROM employees WHERE id = %s",
            (employee_id,)
        )
        connection.commit()
