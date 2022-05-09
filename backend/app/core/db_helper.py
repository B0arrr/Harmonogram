import datetime


class Helper:
    def datetime_sqlalchemy(self, value):
        return datetime.datetime.strptime(str(value), '%Y-%m-%d').date()


helper = Helper()
