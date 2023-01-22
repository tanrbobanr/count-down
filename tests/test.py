"""Code used to test the module.

"""
import sys
sys.path.append(".")
from src import countdown
import datetime
import unittest

cd = countdown.Countdown(
    "T{z}{y.Ea}{y}[_]{Eb}{M}{Ec}{p}{w}{Ed}{P}{d}{Ee}{ep}{h}{Ef}{eP}{m}{Eg}{Ep}{S}{Eh}{EP}{s}{Ei}"
    "{u}{Ej}",
    Ea="[YL]",
    Eb="[YR]",
    Ec="[mo]",
    Ed="[w]",
    Ee="[d]",
    Ef="[h]",
    Eg="[m]",
    Eh="[s]",
    Ei="[ms]",
    Ej="[microseconds] "
)

class TestCountdown(unittest.TestCase):
    def test_default_instance(self) -> None:
        cd2 = countdown.Countdown.default
        value = cd2.format(4864563743338)
        self.assertEqual(value, "1mo 3w 5d 7h 16m 3s")

    def test_parse(self) -> None:
        value = cd.parse("T+[YL]3969[_][YR]1[mo]4[w]S1[h]22[m]Es3[s]ES456[ms]789[microseconds]")
        self.assertEqual(value.total_microseconds(), 123456792123456789)

    def test_format_microseconds(self) -> None:
        value = cd.format(123456792123456789)
        self.assertEqual(value,
                         "T+[YL]3969[_][YR]1[mo]4[w]S1[h]22[m]Es3[s]ES456[ms]789[microseconds]")
    
    def test_format_datetime(self) -> None:
        value = cd.format_datetime(datetime.datetime(2022, 12, 1), datetime.datetime(2023, 1, 15))
        self.assertEqual(value, "T+[_]1[mo]2[w]S1[d]")
    
    def test_format_neg_datetime(self) -> None:
        value = cd.format_datetime(datetime.datetime(2023, 1, 15), datetime.datetime(2022, 12, 1))
        self.assertEqual(value, "T-[_]1[mo]2[w]S1[d]")

    def test_format_weeks(self) -> None:
        value = cd.format_weeks(1.56671)
        self.assertEqual(value, "T+[_]1[w]3[d]es23[h]eS12[m]Es26[s]ES208[ms]")

    def test_format_days(self) -> None:
        value = cd.format_days(-1)
        self.assertEqual(value, "T-[_]1[d]")

    def test_format_hours(self) -> None:
        value = cd.format_hours(241.77)
        self.assertEqual(value, "T+[_]1[w]3[d]es1[h]46[m]Es12[s]ES")

    def test_format_minutes(self) -> None:
        value = cd.format_minutes(71.49999001)
        self.assertEqual(value, "T+[_]1[h]11[m]Es29[s]ES999[ms]400[microseconds]")

    def test_format_seconds(self) -> None:
        value = cd.format_seconds(86400.0001)
        self.assertEqual(value, "T+[_]1[d]100[microseconds]")

    def test_format_milliseconds(self) -> None:
        value = cd.format_milliseconds(-86400.001)
        self.assertEqual(value, "T-[_]1[m]26[s]ES400[ms]1[microseconds]")

    def test_format_microseconds(self) -> None:
        value = cd.format_microseconds(9876543210)
        self.assertEqual(value, "T+[_]2[h]eS44[m]Es36[s]ES543[ms]210[microseconds]")

    def test_format_time(self) -> None:
        value = cd.format_time(weeks=1, days=2, hours=-1, minutes=1, seconds=1, milliseconds=1,
                               microseconds=1)
        self.assertEqual(value, "T+[_]1[w]1[d]23[h]eS1[m]1[s]1[ms]1[microseconds]")

    def test_format_timedelta(self) -> None:
        value = cd.format_timedelta(datetime.timedelta(weeks=1, days=2, hours=-1, minutes=1,
                                                       seconds=1, milliseconds=1, microseconds=1))
        self.assertEqual(value, "T+[_]1[w]1[d]23[h]eS1[m]1[s]1[ms]1[microseconds]")

if __name__ == "__main__":
    unittest.main()
