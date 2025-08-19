class departmentModel:
    def __init__(self):
        self.dept_no = None
        self.dept_name = None

    def getDeptNo(self):
        return self.dept_no
    def getDeptName(self):
        return self.dept_name

    def setDeptNo(self, dept_no):
        self.dept_no = dept_no
    def setDeptName(self, dept_name):
        self.dept_name = dept_name
