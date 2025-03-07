class employee():
    empcount=0
    def __init__(self,eid,name,salary,did):
        self.eid=eid
        self.name=name
        self.salary=salary
        self.did=did
        employee.empcount+=1
    def displayemployee(self):
        print("Employee id:",self.eid,",Employee Name:",self.name,",Employee salary:",self.salary,",did:",self.did)
emp1=employee(1,"Zara",2000,10)
emp2=employee(2,"meera",4000,20)
emp1.displayemployee()
emp2.displayemployee()
print("total employee %d" %employee.empcount)
