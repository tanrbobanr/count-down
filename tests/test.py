"""Code used to test the module.

"""
import sys
sys.path.append(".")
from src import countdown
import datetime
# import logging
# loggers = [logging.getLogger(name) for name in logging.root.manager.loggerDict]
# for l in loggers:
#     if "_countdown" in l.name:
#         l.setLevel(10)


c = countdown.Countdown(
    "T{z}{wL.w}{p.w}{wR.w}{w}{wL}{p}{wR}{d}{dL}{P}{dR}{h}{hL}{ep}{hR}{M}{ML}{eP}{MR}{s}{sL}{Ep}{sR}{m}{mL}{EP}{mR}{u}",
    wL="w[",
    wR="] ",
    dL="d[",
    dR="] ",
    hL="h[",
    hR="] ",
    ML="m[",
    MR="] ",
    sL="s[",
    sR="] ",
    mL="ms[",
    mR="] "
)


assert c.format(123456792123456789) == "T+w[s] 204128w[s] 2d[S] 1h[] 22m[eS] 3s[Es] 456ms[ES] 789"
assert c.format_datetime(datetime.datetime(2022, 12, 1),
                         datetime.datetime(2023, 1, 15)) == "T+w[s] 6w[s] 3d[S]"
assert c.format_datetime(datetime.datetime(2023, 1, 15),
                         datetime.datetime(2022, 12, 1)) == "T-w[s] 6w[s] 3d[S]"
assert c.format_weeks(1.56671) == "T+w[] 1w[] 3d[S] 23h[es] 12m[eS] 26s[Es] 208ms[ES]"
assert c.format_days(-1) == "T-1d[]"
assert c.format_hours(241.77) == "T+w[] 1w[] 3d[S] 1h[] 46m[eS] 12s[Es]"
assert c.format_minutes(71.49999001) == "T+1h[] 11m[eS] 29s[Es] 999ms[ES] 400"
assert c.format_seconds(86400.0001) == "T+1d[] 100"
assert c.format_milliseconds(-86400.0001) == "T-1m[] 26s[Es] 400ms[ES]"
assert c.format_microseconds(9876543210) == "T+2h[es] 44m[eS] 36s[Es] 543ms[ES] 210"
assert c.format_time(weeks=1, days=2, hours=-1, minutes=1, seconds=1, milliseconds=1,
                     microseconds=1) == "T+w[] 1w[] 1d[] 23h[es] 1m[] 1s[] 1ms[] 1"
assert c.format_timedelta(datetime.timedelta(weeks=1, days=2, hours=-1, minutes=1, seconds=1,
                          milliseconds=1,
                          microseconds=1)) == "T+w[] 1w[] 1d[] 23h[es] 1m[] 1s[] 1ms[] 1"
