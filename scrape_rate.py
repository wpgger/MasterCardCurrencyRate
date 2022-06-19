import pandas as pd
import requests
import datetime


class RateScraper:
    def __init__(self):
        self.date = datetime.datetime.today().strftime("%Y-%m-%d")
        self.transCurrency = "USD"
        self.billCurrency = "CAD"
        self.bankFee = 0
        self.amount = 100
        self.df = ""

    def getRate(self):
        url = "https://www.mastercard.ca/settlement/currencyrate/conversion-rate?fxDate=" + self.date + "&transCurr=" + self.transCurrency +"&crdhldBillCurr=" + self.billCurrency +"&bankFee=" + str(self.bankFee) +"&transAmt=" + str(self.amount) 
        header = {
            "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
        }
        response = requests.get(url, headers=header)
        self.df = pd.read_json(response.text)
        



test = RateScraper()

answer = input("Get Today's USD/CAD Rate? Yes/No: ")
if answer =="Y" or answer == "y" or answer == "":
    pass
elif answer =="N" or answer == "n":
    test.date = input("Please enter the date of the transction (YYYY-MM-DD): ")
    test.transCurrency = input("Please enter the transction Currency: ")
    test.billCurrency = input("Please enter the card Currency: ")
    test.bankFee = input("Please enter bank fee(%): ")
    test.amount = input("Please enter the transation amount: ")
else:
    exit()
test.getRate()

print(f"\n{test.df.data.transAmt} {test.df.data.transCurr} = {test.df.data.crdhldBillAmt} {test.df.data.crdhldBillCurr} on {test.df.data.fxDate}")
print(f"Conversion Rate: {test.df.data.conversionRate}")

