from datetime import date

def calculator_age(birthday):
    today = date.today()
    day_check = ((today.month,today.day)<(birthday.month,birthday.day))
    year_diff = today.year - birthday.year
    age_in_years = year_diff - day_check
    remaining_months = abs(today.month - birthday.month)
    remaining_days = abs(today.day - birthday.day)
    print("Age:",age_in_years,"Years",remaining_months,"months and",remaining_days,"days")
print("simple age calculator")
birthYear = int(input("Enter the birth year:"))
birthMonth = int(input("Enter the birth Month:"))
birthDay = int(input("Enter the birth Day:"))
dateOfBirth = date(birthYear,birthMonth,birthDay)
calculator_age(dateOfBirth)
    