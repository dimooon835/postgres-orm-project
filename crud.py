from database import SessionLocal
from models import Department, Employee, Project
from decimal import Decimal

def create_department(name: str):
    with SessionLocal() as session:
        department = Department(name=name)

        session.add(department)
        session.commit()
        session.refresh(department)
        
        return department
    
def create_employee(
        name: str,
        salary: Decimal,
        department_id: int | None = None
):
    with SessionLocal() as session:
        employee = Employee(
            name=name,
            salary=salary,
            department_id=department_id
        )

        session.add(employee)
        session.commit()
        session.refresh(employee)

        return employee
        
def create_project(
    name: str,
    budget: Decimal,
    employee_id: int | None = None
):
    with SessionLocal() as session:
        project = Project(
            name=name,
            budget=budget,
            employee_id=employee_id
        )

        session.add(project)
        session.commit()
        session.refresh(project)

        return project
    
with SessionLocal() as session:
    department = Department(name="Dev")
    employee = Employee(
        name="Ivan",
        salary=Decimal("100000.00")
    )
    project = Project(
        name="Mobile",
        budget=Decimal("200000.00")
    )

    department.employees.append(employee)
    employee.projects.append(project)
    session.add(department)
    session.commit()