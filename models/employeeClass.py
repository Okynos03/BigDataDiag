class empleadoModel:
    def __init__(self, emp_no, first_name, last_name, gender, hire_date):
        self.emp_no = emp_no
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.hire_date = hire_date

    def getGender(self):
        return self.gender

    def getHireDate(self):
        return self.hire_date

    def getEmpNo(self):
        return self.emp_no

    def getFirstName(self):
        return self.first_name

    def getLastName(self):
        return self.last_name

    def setFirstName(self, first_name):
        self.first_name = first_name

    def setLastName(self, last_name):
        self.last_name = last_name

    def setGender(self, gender):
        self.gender = gender

    def setHireDate(self, hire_date):
        self.hire_date = hire_date

    def setEmpNo(self, emp_no):
        self.emp_no = emp_no
