import tkinter
from calculator import *

money = 0
year = 0

result = dict()

result['money'] = 0
result['year'] = 0
result['yearDeduction'] = 0
result['amountAfterDeduction'] = 0
result['calSalary'] = 0
result['calSalaryDeduction'] = 0
result['specialTaxationStandard'] = 0
result['taxAmount'] = 0
result['incomeTax'] = 0
result['residentTax'] = 0

#퇴직소득
def getRetirementIncome():
    try:
        money = int(moneyEntry.get())
    except:
        print("Invalid money Input,, Retry")
        moneyErrorMessage.pack()
        return -1
    
    if money > 0:
        print("get money input Success")
        moneyErrorMessage.pack_forget()
        return money
    else:
        print("Invalid money Input,, Retry")
        moneyErrorMessage.pack()
        return -1

#근속연수
def getYear():
    try:
        year = int(yearEntry.get())
    except:
        print("Invalid year` Input,, Retry")
        yearErrorMessage.pack()
        return -1
    if year > 0:
        print("get year input Success")
        yearErrorMessage.pack_forget()
        return year
    else:
        print("Invalid year Input,, Retry")
        yearErrorMessage.pack()
        return -1

def onCalButtonClicked(event=1):
    result['money'] = money = getRetirementIncome()
    result['year'] = year = getYear()
    result['yearDeduction'] = getYearDeduction(year)
    result['amountAfterDeduction'] = getAmountAfterDeduction(money, year)
    result['calSalary'] = getCalSalary(money, year)
    result['calSalaryDeduction'] = getCalSalaryDeduction(money, year)
    result['specialTaxationStandard'] = getSpecialTaxationStandard()
    result['taxAmount'] = getTaxAmount()
    result['incomeTax'] = getIncomeTax(year)
    result['residentTax'] = getResidentTax()

    if result['money'] > 0 and result['year'] > 0:
        moneyLabel.config(text=f"퇴직소득: {result['money']}원")
        yearLabel.config(text=f"근속연수: {result['year']}원")
        yearDeductionLabel.config(text=f"근속연수공제: {result['yearDeduction']}원")
        amountAfterDeductionLabel.config(text=f"공제후금액: {result['amountAfterDeduction']}원")
        calSalaryLabel.config(text=f"환산급여: {result['calSalary']}원")
        calSalaryDeductionLabel.config(text=f"환산급여특별공제: {result['calSalaryDeduction']}원")
        specialTaxationStandardLabel.config(text=f"특별소득과세표준: {result['specialTaxationStandard']}원")
        taxAmountLabel.config(text=f"환산산출세액: {result['taxAmount']}원")
        incomeTaxLabel.config(text=f"산출세액(소득세): {result['incomeTax']}원")
        residentTaxLabel.config(text=f"주민세: {result['residentTax']}원")

    print(result)

window = tkinter.Tk()

window.title("EOM HYE JIN")
window.geometry("800x600+200+200")

moneyErrorMessage = tkinter.Message(window, text="퇴직급여가 잘못되었습니다. 재시도하세요", width=100, relief='solid', fg="red")
yearErrorMessage = tkinter.Message(window, text="근속연수가 잘못되었습니다. 재시도하세요", width=100, relief='solid', fg="red")

mainLabel = tkinter.Label(window, text="환영합니다. 엄혜진의 회계 월드입니다.")
mainLabel.pack()

moneyEntry = tkinter.Entry(window, text="퇴직급여 입력", highlightthickness=1)
moneyEntry.bind("<Return>", onCalButtonClicked)
moneyEntry.pack()

yearEntry = tkinter.Entry(window, text="근속연수 입력", highlightthickness=1)
yearEntry.bind("<Return>", onCalButtonClicked)
yearEntry.pack()

moneyLabel = tkinter.Label(window, text="퇴직소득: ")
moneyLabel.pack()

yearLabel = tkinter.Label(window, text="근속연수: ")
yearLabel.pack()

yearDeductionLabel = tkinter.Label(window, text="근속연수공제: ")
yearDeductionLabel.pack()

amountAfterDeductionLabel = tkinter.Label(window, text="공제후금액: ")
amountAfterDeductionLabel.pack()

calSalaryLabel = tkinter.Label(window, text="환산급여: ")
calSalaryLabel.pack()

calSalaryDeductionLabel = tkinter.Label(window, text="환산급여특별공제: ")
calSalaryDeductionLabel.pack()

specialTaxationStandardLabel = tkinter.Label(window, text="특별소득과세표준: ")
specialTaxationStandardLabel.pack()

taxAmountLabel = tkinter.Label(window, text="환산산출세액: ")
taxAmountLabel.pack()

incomeTaxLabel = tkinter.Label(window, text="산출세액(소득세): ")
incomeTaxLabel.pack()

residentTaxLabel = tkinter.Label(window, text="주민세: ")
residentTaxLabel.pack()

calButton = tkinter.Button(window, text="계산하기", command=onCalButtonClicked, width=40, height=5, bg='green')
calButton.pack()

window.mainloop()