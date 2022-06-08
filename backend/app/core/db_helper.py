import datetime


class Helper:
    def datetime_sqlalchemy(self, value):
        return datetime.datetime.strptime(str(value), '%Y-%m-%d').date()

    def get_list_of_days(self, start: datetime.date, end: datetime.date):
        days = []
        delta = end - start
        for i in range(delta.days + 1):
            days.append(start + datetime.timedelta(days=i))
        return days


helper = Helper()
