import datetime


def get_last_monday():
    today = datetime.date.today()
    return today - datetime.timedelta(days=today.weekday())
