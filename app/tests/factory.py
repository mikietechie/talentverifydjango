import datetime

from app.models import User, Department, Company, Employee, Employment


class DataFactory():
    def create_data(self):
        self.today = datetime.date.today()
        self.year_ago = self.today - datetime.timedelta(days=365)
        self.year2_ago = self.today - datetime.timedelta(days=365*2)
        self.year10_ago = self.today - datetime.timedelta(days=365*10)

        self.su = User.objects.create(
            username = "su",
            password = "password",
            email = "su@mail.com",
            role = "Admin",
            first_name = "Super",
            last_name = "User",
            is_superuser=True,
        )

        self.u2 = User.objects.create(
            username = "u2",
            password = "password",
            email = "u2@mail.com",
            role = "Admin",
            first_name = "Super",
            last_name = "User"
        )

        self.ad_dep = Department.objects.create(name="Admin")
        self.hr_dep = Department.objects.create(name="HR")
        self.eng_dep = Department.objects.create(name="Eng")
        self.acc_dep = Department.objects.create(name="Accounting")
        self.sec_dep = Department.objects.create(name="Security")
        self.un_dep = Department.objects.create(name="unwanted")

        self.goprime_company = Company.objects.create(
            name = "Goprime",
            date_of_registration = self.year2_ago,
            registration_number = "gp1",
            contact_person = "Gerry",
            contact_phone = "0713122648",
            email_address = "g@gp.com",
        )
        self.goprime_company.departments.set([self.eng_dep, self.ad_dep])

        self.koin_company = Company.objects.create(
            name = "Koin Tech",
            date_of_registration = self.year_ago,
            registration_number = "kt1",
            contact_person = "Munashe",
            contact_phone = "07131224647",
            email_address = "m@kt.com",
        )
        self.koin_company.departments.set([self.eng_dep, self.ad_dep, self.acc_dep])

        self.mike_emp = Employee.objects.create(
            name = "Mike Z",
            id_number = "630000",
            contact_phone = "2349802",
            email_address = "m@m.com",
            trade = "Engineer",
        )

        self.caleb_emp = Employee.objects.create(
            name = "Caleb",
            id_number = "67838",
            contact_phone = "09378299",
            email_address = "c@gp.com",
            trade = "Engineer",
        )

        self.munashe_emp = Employee.objects.create(
            name = "Munashe",
            id_number = "hhh",
            contact_phone = "09378299",
            email_address = "c@mm.com",
            trade = "Accountant",
        )

        self.mike_goprime = Employment.objects.create(
            department = self.eng_dep,
            employee = self.mike_emp,
            company = self.goprime_company,
            role = "SE",
            date_started = datetime.date(2022, 8, 1),
            date_left = datetime.date(2023, 5, 1),
            duties = "Assistant Fullstack Developer",
        )

        self.mike_koin = Employment.objects.create(
            department = self.eng_dep,
            employee = self.mike_emp,
            company = self.koin_company,
            role = "PM",
            date_started = datetime.date(2022, 8, 1),
            date_left = datetime.date(2023, 5, 1),
            duties = "Projects MAnager and Tech Lead",
        )

        self.caleb_goprime = Employment.objects.create(
            department = self.eng_dep,
            employee = self.caleb_emp,
            company = self.goprime_company,
            role = "Manager",
            date_started = datetime.date(2018, 8, 1),
            date_left = None,
            duties = "Senior Software Engineer",
        )

        self.munashe_koin = Employment.objects.create(
            department = self.ad_dep,
            employee = self.munashe_emp,
            company = self.koin_company,
            role = "SE",
            date_started = datetime.date(2020, 1, 1),
            date_left = None,
            duties = "Operations Manager",
        )
