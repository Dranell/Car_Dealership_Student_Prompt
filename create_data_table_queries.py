directory_table = """
create table directory(
tax_id int primary key unique,
employee_name varchar(100) not null,
employee_position varchar(100) not null,
employee_salary int not null,
employee_hiring_date date,
employee_years_experience int not null
);
"""
sports_cars = """
create table sports_cars(
vin_number int primary key unique,
year int not null,
make varchar(100) not null,
model varchar(100) not null,
price int not null,
mileage int not null,
arrival_date date,
sold boolean
);
"""

sedan_cars = """
create table sedan_cars(
vin_number int primary key unique,
year int not null,
make varchar(100) not null,
model varchar(100) not null,
price int not null,
mileage int not null,
arrival_date date,
sold boolean
);
"""