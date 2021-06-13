import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','jobsProject.settings')

import django
django.setup()


from jobsApp.models import *
from faker import Faker
from random import *



fake = Faker()

def phoneNumberGenerator():
    d1 = randint(7,9)
    num = '' + str(d1)
    for i in range(9):
        num = num + str(randint(0,9))
    return int(num)

def populate(n):
    for i in range(n):
        fdate = fake.date()
        fcompany = fake.company()
        ftitle = fake.random_element(elements = (
          'Project Manager','Team Lead','Software Engineer'
        ))
        feligibility = fake.random_element(elements = (
        'B.Tech','M.Tech','MCA','Phd'
        ))
        faddress = fake.address()
        femail = fake.email()
        fphone_number = phoneNumberGenerator()
        hydjobs_record = hydjobs.objects.get_or_create(
        date = fdate,company = fcompany, job_title = ftitle,
        eligibility = feligibility,address = faddress,
        email = femail, phone_number = fphone_number )

        punejobs_record = punejobs.objects.get_or_create(
        date = fdate,company = fcompany, job_title = ftitle,
        eligibility = feligibility,address = faddress,
        email = femail, phone_number = fphone_number )

        delhijobs_record = delhijobs.objects.get_or_create(
        date = fdate,company = fcompany, job_title = ftitle,
        eligibility = feligibility,address = faddress,
        email = femail, phone_number = fphone_number )

populate(10)
