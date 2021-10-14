from .models import *
from faker import Faker
fake = Faker()
import random
choice=['math','science','english','hindi','histrory']
def seed_subdb(n):
    for i in range(0 , n):
        Subject.objects.create(
            subName = choice[i],
        )
lastname=['kumar','singh','paswaan']
def seed_prodb(n):
    for x in range(0,n):
         Professor.objects.create(
             p_fname=fake.name(),
             p_lname=lastname[random.lastname(0,3)],
             subjects=choice[random.randint(0,4)]
         )