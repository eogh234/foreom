#근속연수공제
def getYearDeduction(year):    
    if 0 < year and year <= 5:
        return year * 100 * 10000
    elif year <= 10:
        return (500 * 10000) + ((year - 5) * 200 * 10000)
    elif year <= 20:
        return (1500 * 10000) + ((year - 10) * 250 * 10000)
    else:
        return (4000 * 10000) + ((year - 20) * 300 * 10000)
#공제 후 금액
def getAmountAfterDeduction(money, year):
    return money - getYearDeduction(year)

#환산급여
def getCalSalary(money, year):
    amount = getAmountAfterDeduction(money, year)
    
    if amount > 0:
        return amount * 12 // year
    else:
        print(f"amount is invalid,, amount: {amount}")
        return 0

#환산급여특별공제
def getCalSalaryDeduction(money, year):
    salary = getCalSalary(money, year)
    if salary > 0 and salary <= (800 * 10000):
        return salary
    elif salary <= (7000 * 10000):
        return (800 * 10000) + ((salary - (800 * 10000))*0.6)
    elif salary <= (10000 * 10000):
        return (4520 * 10000) + ((salary - (7000 * 10000)) * 0.55)
    elif salary <= (3 * 10000 * 10000):
        return (6170 * 10000) + ((salary - (10000 * 10000)) * 0.45)
    else:
        return (15170 * 10000) + ((salary - (30000 * 10000)) * 0.35)

#특별소득과세표준
def getSpecialTaxationStandard():
    return 0

#환산산출세액
def getTaxAmount():
    return 10000

#산출세액(소득세)
def getIncomeTax(year):
    return getTaxAmount() * year // 12
#주민세
def getResidentTax():
    return 50599