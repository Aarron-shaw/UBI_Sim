import time
import random
import matplotlib.pyplot as plt


fig, ax = plt.subplots()


class cit(object):
    def __init__(self,income,bills,tax,ubi):
        self.funds = 0
        self.income = income
        self.bills = bills
        self.tax = tax
        self.disposable = 0
        self.ubi = ubi
        self.funds_list = []
    
    def monthly(self):
        self.disposable = 0
        self.disposable += deviate_income(self.income)
        self.disposable -= deviate_bills(self.bills)
        self.disposable -= self.income * self.tax
        self.disposable += self.ubi
        self.funds += self.disposable
        self.funds_list.append(self.funds)
        
        
def deviate_income(income):        
    perce_change = random.randint(-20,20) / 100
    
    return (income * perce_change) + income
        
def deviate_bills(bills):
    perce_change = random.randint(-5,30) / 100
    
    return (bills * perce_change) + bills

def gen_rand_income():
    return random.randint(1000,4000)

income = gen_rand_income()
bill_perc =  random.randint(50,65) / 100
bills = income * bill_perc
tax_income_normal = 0.25
tax_income_ubi = 0.30
ubi = 0

print(income,bills,tax_income_normal,ubi)

person = cit(income,bills,tax_income_normal,ubi)
person_ubi = cit(income,bills,tax_income_ubi,500)

months = []
count = 0
for year in range(0,1):

    for month in range(1,13):
        person.monthly()
        person_ubi.monthly()
        months.append(count)
        count += 1
    
ax.plot(months,person.funds_list, label="No UBI")
ax.plot(months,person_ubi.funds_list, label="With UBI")
plt.ticklabel_format(style = 'plain')
ax.legend()
plt.show()
    

        
        
        
    