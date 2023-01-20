from typing import Union
from . import constants
from . import types
import plogging
import operator
import logging
import typing


class TimeValue:
    """Stores a time value partitioned into weeks, days, hours, minutes, seconds, milliseconds,
    and/or microseconds.
    
    """
    _log = plogging.setup_new("TimeValue", level=logging.DEBUG, package=__name__)
    def __init__(self, z: typing.Literal[1, -1], w: Union[int, float] = None,
                 d: Union[int, float] = None, h: Union[int, float] = None,
                 M: Union[int, float] = None, s: Union[int, float] = None,
                 m: Union[int, float] = None, u: Union[int, float] = None) -> None:
        self.z = z
        self.w = w
        self.d = d
        self.h = h
        self.M = M
        self.s = s
        self.m = m
        self.u = u

    @typing.overload
    def get(self, name: str, /) -> Union[int, float, None]: ...
    @typing.overload
    def get(self, name: str, default: types.T, /) -> Union[int, float, None, types.T]: ...
    def get(self, name: str, default = types.MISSING, /):
        """Get the stored time value given a valid flag name and optional default.
        
        """
        if default is types.MISSING:
            TimeValue._log.debug(f"Acquiring value from flag name: '{name}'")
            if name not in constants.BASE_FLAGS:
                raise ValueError(f"Invalid flag name: '{name}'")
            return getattr(self, name)
        
        TimeValue._log.debug(f"Acquiring value from flag name: '{name}'; default={default}")
        if name not in constants.BASE_FLAGS:
            return default
        return getattr(self, name)

    def set(self, name: str, value: Union[int, float, None], /) -> None:
        """Set the given flag specified by `name` to `value`.
        
        """
        if name not in constants.BASE_FLAGS:
            raise ValueError(f"Invalid flag name: '{name}'")
        setattr(self, name, value)
    
    @property
    def sign(self) -> typing.Literal[1, -1]:
        return self.z

    @property
    def weeks(self) -> Union[int, float] | None:
        return self.w
    
    @property
    def days(self) -> Union[int, float] | None:
        return self.d
    
    @property
    def hours(self) -> Union[int, float] | None:
        return self.h
    
    @property
    def minutes(self) -> Union[int, float] | None:
        return self.M
    
    @property
    def seconds(self) -> Union[int, float] | None:
        return self.s
    
    @property
    def milliseconds(self) -> Union[int, float] | None:
        return self.m
    
    @property
    def microseconds(self) -> Union[int, float] | None:
        return self.u

    def total_microseconds(self) -> int:
        values = (self.w or 0, self.d or 0, self.h or 0, self.M or 0, self.s or 0, self.m or 0,
                  self.u or 0)
        muls = (constants.MICROSECONDS_IN_WEEK, constants.MICROSECONDS_IN_DAY,
                constants.MICROSECONDS_IN_HOUR, constants.MICROSECONDS_IN_MINUTE,
                constants.MICROSECONDS_IN_SECOND, constants.MICROSECONDS_IN_MILLISECOND, 1)
        return sum(map(operator.mul, values, muls)) * self.z

    def total_milliseconds(self) -> float:
        return self.total_microseconds / constants.MICROSECONDS_IN_MILLISECOND

    def total_seconds(self) -> float:
        return self.total_microseconds / constants.MICROSECONDS_IN_SECOND

    def total_minutes(self) -> float:
        return self.total_microseconds / constants.MICROSECONDS_IN_MINUTE

    def total_hours(self) -> float:
        return self.total_microseconds / constants.MICROSECONDS_IN_HOUR

    def total_days(self) -> float:
        return self.total_microseconds / constants.MICROSECONDS_IN_DAY

    def total_weeks(self) -> float:
        return self.total_microseconds / constants.MICROSECONDS_IN_WEEK
