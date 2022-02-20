# in:  2021-06-21 23:52:25+0800
#      2021-06-21 23:52:25.442
#      2021-06-21 23:52:25 +0800 CST:
# out: datetime.datetime(2021, 6, 21, 23, 52, 25)
import datetime
def string2datetime(st):
    if " +0800 CST:"in st: return datetime.datetime.strptime(st, "%Y-%m-%d %H:%M:%S +0800 CST:")
    if "+800" in st: return datetime.datetime.strptime(st, "%Y-%m-%dT%H:%M:%S.%f+0800")
    return datetime.datetime.strptime(st, "%Y-%m-%dT%H:%M:%S.%f")
