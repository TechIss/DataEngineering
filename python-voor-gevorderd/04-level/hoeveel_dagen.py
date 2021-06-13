import datetime

jaar = int(input("Wat is het jaar? "))
maandnummer = int(input("Wat is het maandnummer? "))
dag = int(input("Wat is de dag? "))

myDate = datetime.date(jaar, maandnummer, dag)

datetime_object = datetime.date.today()

def howLongToGo():
    print(datetime_object - myDate)

howLongToGo()
