import datetime


class Helper:
    def datetime_sqlalchemy(self, value):
        return datetime.datetime.strptime(str(value), '%Y-%m-%d').date()

    def get_list_of_days(self, start: datetime.date, end: datetime.date):
        days = []
        temp = start
        while start <= end:
            days.append(temp)
            temp += datetime.timedelta(days=1)
        return days


helper = Helper()
