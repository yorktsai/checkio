from datetime import date
from datetime import timedelta

def checkio(from_date, to_date):
    """
        Count the days of rest
    """
    count = 0
    delta = timedelta(days=1)
    while from_date <= to_date:
        if from_date.weekday() >= 5:
            count += 1
        from_date = from_date + delta
    
    return count

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(date(2013, 9, 18), date(2013, 9, 23)) == 2, "1st example"
    assert checkio(date(2013, 1, 1), date(2013, 2, 1)) == 8, "2nd example"
    assert checkio(date(2013, 2, 2), date(2013, 2, 3)) == 2, "3rd example"


