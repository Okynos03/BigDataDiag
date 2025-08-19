class salaryModel:
    def __init__(self):
        self.emp_no = None
        self.salary = None
        self.from_date = None
        self.to_date = None

    def setEmpNo(self, emp_no):
        self.emp_no = emp_no
    def setSalary(self, salary):
        self.salary = salary
    def setFromDate(self, from_date):
        self.from_date = from_date
    def setToDate(self, to_date):
        self.to_date = to_date

    def getEmpNo(self):
        return self.emp_no
    def getSalary(self):
        return self.salary
    def getFromDate(self):
        return self.from_date
    def getToDate(self):
        return self.to_date