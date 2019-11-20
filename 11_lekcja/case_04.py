from datetime import datetime


class Watch:
    # def __init__(self):
    #     print("I tell time")

    def time(self):
        return datetime.now().time()


class Calendar:
    # def __init__(self):
    #     print("I tell date")

    def date(self):
        return datetime.now().date()


class WatchCalendar(Watch, Calendar):
    def __init__(self):
        print("I can tell date and time!")


def check_datetime():
    print("Today is", wc.date(), "and right now is", wc.time(), "hour.")


w = Watch()
c = Calendar()
wc = WatchCalendar()
print(w.time())
print(c.date())
check_datetime()
