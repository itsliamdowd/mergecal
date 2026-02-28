# mergecalweb/core/constants.py


class CalendarLimits:
    FREE = 20  # Same as BUSINESS - no free restrictions
    PERSONAL = 20
    BUSINESS = 20
    SUPPORTER = float("inf")


class SourceLimits:
    FREE = 5  # Same as BUSINESS - no free restrictions
    PERSONAL = 3
    BUSINESS = 5
    SUPPORTER = float("inf")
