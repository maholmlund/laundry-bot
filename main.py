import requests
import sys
import os
import datetime
from dateutil.relativedelta import relativedelta


def book_slot(creds, date, time, machine):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"}
    r = requests.get(
        "https://booking-hoas.tampuuri.fi/auth/login", headers=headers)
    csrf_token = r.cookies["csrf_cookie_name"]
    ci_session = r.cookies["ci_session"]
    payload = {
        "csrf_token_name": csrf_token,
        "login": creds[0],
        "password": creds[1],
        "submit": "Kirjaudu"
    }
    cookie_set = {
        "csrf_cookie_name": csrf_token,
        "ci_session": ci_session
    }
    r = requests.post("https://booking-hoas.tampuuri.fi/auth/login",
                      data=payload,
                      cookies=cookie_set,
                      headers=headers)
    if "pesulavuorojen varaaminen" not in r.content.decode().lower():
        sys.exit(f"login failed")
        exit(1)
    requests.get(
        f"https://booking-hoas.tampuuri.fi/varaus/service/reserve/{machine}/{time}/{date}",
        cookies=cookie_set,
        headers=headers)
    # Seems that the api does not give any feedback on whether the booking was successful or not.
    # So we ignore the return value here.


creds = (os.environ["HOAS_USER"], os.environ["HOAS_PASSWORD"])
time = os.environ["HOAS_TIME"]
weekday = int(os.environ["HOAS_WEEKDAY"])
machine_number = os.environ["HOAS_MACHINE"]

start = datetime.datetime.today() + relativedelta(months=1)
start = start.replace(day=1)
days = []
current = start
while current.month == start.month:
    if current.weekday() == weekday:
        days.append(f"{current.year}-{current.month}-{current.day}")
    current += relativedelta(days=1)

for day in days:
    print(f"booking slot {day}, {time}...")
    book_slot(creds, day, time, machine_number)
