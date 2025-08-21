import mysql.connector



class employeeDAO:
    def __init__(self):
        pass

    def get_all_employees(self, conn):
        employees_list = []
        try:
            cursor = conn.cursor(dictionary=True)
            query = "SELECT emp_no, first_name, last_name, gender, hire_date FROM employees limit 100"
            cursor.execute(query)

            employees_list = cursor.fetchall()
            cursor.close()

        except mysql.connector.Error as err:
            print(f"Error: {err}")

        return employees_list

    def get_current_n_salary(self, conn):
        employees_list = []
        try:
            cursor = conn.cursor(dictionary=True)
            query = ("SELECT e.emp_no, CONCAT(e.first_name, ' ', e.last_name) as full_name, s.salary "
                     "FROM employees e "
                     "inner join salaries s on e.emp_no = s.emp_no "
                     "where s.to_date = '9999-01-01';")
            cursor.execute(query)

            employees_list = cursor.fetchall()
            cursor.close()

        except mysql.connector.Error as err:
            print(f"Error: {err}")

        return employees_list

    #PARA LA DE GRAFICA DE PASTEL
    def get_counts(self, conn):
        total = 0
        m_total = 0
        f_total = 0
        try:
            cursor = conn.cursor(dictionary=True)
            query = "SELECT COUNT(*) FROM employees inner join dept_emp on employees.emp_no = dept_emp.emp_no where dept_emp.to_date = '9999-01-01'; "
            cursor.execute(query)
            total = cursor.fetchall()

            query = "SELECT COUNT(*) FROM employees inner join dept_emp on employees.emp_no = dept_emp.emp_no where dept_emp.to_date = '9999-01-01' and gender = 'F';"
            cursor.execute(query)
            f_total = cursor.fetchall()

            query = "SELECT COUNT(*) FROM employees inner join dept_emp on employees.emp_no = dept_emp.emp_no where dept_emp.to_date = '9999-01-01' and gender = 'M';"
            cursor.execute(query)
            m_total = cursor.fetchall()
            cursor.close()

        except mysql.connector.Error as err:
            print(f"Error: {err}")

        return total, f_total, m_total

    #GRAFICAS BARRAS HORIZONTALES
    def get_top_ten(self, conn):
        top_ten = []
        try:
            cursor = conn.cursor(dictionary=True)
            query = "select e.emp_no, CONCAT(e.first_name, ' ', e.last_name) as full_name, s.salary from employees e inner join salaries s on e.emp_no = s.emp_no WHERE s.to_date = '9999-01-01'  order by s.salary desc limit 10;"
            cursor.execute(query)

            top_ten = cursor.fetchall()

            cursor.close()

        except mysql.connector.Error as err:
            print(f"Error: {err}")

        return top_ten

    def get_num_female_employee(self, conn):
        count = 0
        try:
            cursor = conn.cursor(dictionary=True)
            query = "select count(emp_no) from employees where gender = 'F';"
            cursor.execute(query)
            num_female_employee = cursor.fetchone()
            count = num_female_employee['count(emp_no)']
            cursor.close()

        except mysql.connector.Error as err:
            print(f"Error: {err}")

        return count

    def get_num_male_employee(self, conn):
        count = 0
        try:
            cursor = conn.cursor(dictionary=True)
            query = "select count(emp_no) from employees where gender = 'M';"
            cursor.execute(query)
            num_male_employee = cursor.fetchone()
            count = num_male_employee['count(emp_no)']
            cursor.close()

        except mysql.connector.Error as err:
            print(f"Error: {err}")

        return count