import mysql.connector

class deptoDAO:
    def __init__(self):
        pass

    def get_all_depts(self, conn):
        depts_list = []
        try:
            cursor = conn.cursor(dictionary=True)
            query = "SELECT dept_no, dept_name FROM departments"
            cursor.execute(query)
            depts_list = cursor.fetchall()
            cursor.close()

        except mysql.connector.Error as err:
            print(f"Error: {err}")

        return depts_list

    def get_employees_by_dept(self, conn, num):
        employees_list = []
        try:
            cursor = conn.cursor(dictionary=True)
            if num == "0":
                query = (
                    "SELECT e.emp_no, CONCAT(e.first_name, ' ', e.last_name) as full_name, d.dept_name FROM departments d  "
                    "inner join dept_emp de on d.dept_no = de.dept_no "
                    "inner join employees e on e.emp_no = de.emp_no "
                    "where de.to_date != '9999-01-01';")
                cursor.execute(query)
            else:
                query = (
                    "SELECT e.emp_no, CONCAT(e.first_name, ' ', e.last_name) as full_name, d.dept_name FROM departments d  "
                    "inner join dept_emp de on d.dept_no = de.dept_no "
                    "inner join employees e on e.emp_no = de.emp_no "
                    "where d.dept_no = %s and de.to_date != '9999-01-01';")
                cursor.execute(query, (num,))

            employees_list = cursor.fetchall()
            cursor.close()

        except mysql.connector.Error as err:
            print(f"Error: {err}")

        return employees_list

    def get_managers(self, conn):
        managers = []
        try:
            cursor = conn.cursor(dictionary=True)
            query = ("select d.dept_name, CONCAT(e.first_name, ' ', e.last_name) as full_name, dm.from_date "
                     "from departments d "
                     "inner join dept_manager dm on d.dept_no = dm.dept_no "
                     "inner join employees e on dm.emp_no = e.emp_no "
                     "where dm.to_date = '9999-01-01';")
            cursor.execute(query)
            managers = cursor.fetchall()
            cursor.close()

        except mysql.connector.Error as err:
            print(f"Error: {err}")

        return managers

    def highest_payed(self, conn):
        highest = []
        try:
            cursor = conn.cursor(dictionary=True)
            query = (
                "SELECT "
                "    d.dept_name, "
                "    e.emp_no, "
                "    CONCAT(e.first_name, ' ', e.last_name) AS full_name, "
                "    s.salary "
                "FROM departments d "
                "INNER JOIN dept_emp de ON d.dept_no = de.dept_no "
                "INNER JOIN employees e ON de.emp_no = e.emp_no "
                "INNER JOIN salaries s ON e.emp_no = s.emp_no "
                "INNER JOIN ( "
                "    SELECT "
                "        de.dept_no, "
                "        MAX(s.salary) AS max_salary "
                "    FROM dept_emp de "
                "    INNER JOIN salaries s ON de.emp_no = s.emp_no "
                "    WHERE "
                "        de.to_date = '9999-01-01' AND s.to_date = '9999-01-01' "
                "    GROUP BY "
                "        de.dept_no "
                ") AS max_salaries_per_dept ON d.dept_no = max_salaries_per_dept.dept_no AND s.salary = max_salaries_per_dept.max_salary "
                "WHERE "
                "    de.to_date = '9999-01-01' AND s.to_date = '9999-01-01';"
            )
            cursor.execute(query)
            highest = cursor.fetchall()
            cursor.close()

        except mysql.connector.Error as err:
            print(f"Error: {err}")

        return highest

    #BARRAS VERTICALES
    def get_avg(self, conn):
        avgs = []
        try:
            cursor = conn.cursor(dictionary=True)
            query = (
                "SELECT d.dept_name, AVG(s.salary) as avg "
                "FROM departments d "
                "INNER JOIN dept_emp de ON d.dept_no = de.dept_no "
                "INNER JOIN salaries s ON de.emp_no = s.emp_no "
                "WHERE s.to_date = '9999-01-01' "
                "GROUP BY d.dept_name;"
            )
            cursor.execute(query)
            avgs = cursor.fetchall()
            cursor.close()

        except mysql.connector.Error as err:
            print(f"Error: {err}")

        return avgs