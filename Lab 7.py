class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_info(self):
        return f'Имя сотрудника:{self.name}, ID сотрудника: {self.id}'

class Manager(Employee):
    def __init__(self, name, id, department):
        Employee.__init__(self, name, id)
        self.department = department

    def manage_project(self):
        return f'Менеджер {self.name} управляет проектами в отделе {self.department}'

class Technician(Employee):
    def __init__(self, name, id, specialization):
        Employee.__init__(self, name, id)
        self.specialization = specialization

    def perform_maintenance(self):
        return f'Техник {self.name} выполняет техническое обслуживание в области {self.specialization}'

class TechManager(Manager, Technician):
    def __init__(self, name, id, department, specialization):
        Manager.__init__(self, name, id, department)
        Technician.__init__(self, name, id, specialization)
        self.new_employees = []

    def add_employee(self, employee):
        self.new_employees.append(employee)

    def get_team_info(self):
        team_info = f"Подчинённые тех. менеджера {self.name}:\n"
        for employee in self.new_employees:
            team_info += f"* {employee.get_info()}\n"
        return team_info

employee = Employee('Alexey', 999)
manager = Manager('Balera', 269, 'Derevnya')
technician = Technician('Bob', 169, 'Gubernatorstvo')
tech_manager = TechManager('Leha', 69, 'Hell', 'Dovolno')

print(employee.get_info())
print(manager.get_info())
print(manager.manage_project())
print(technician.get_info())
print(technician.perform_maintenance())
print(tech_manager.get_info())
print(tech_manager.manage_project())
print(tech_manager.perform_maintenance())

tech_manager.add_employee(employee)
tech_manager.add_employee(technician)
print(tech_manager.get_team_info())

