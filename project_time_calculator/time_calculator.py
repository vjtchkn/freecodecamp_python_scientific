def add_time(start, duration, day=""):
    # Extract starting time and duration from input
    start_t, start_per = start.split()
    start_h, start_m = start_t.split(":")
    start_h = int(start_h)
    start_m = int(start_m)
    dur_h, dur_m = duration.split(":")
    dur_h = int(dur_h)
    dur_m = int(dur_m)

    # Setup days of the week
    days = [
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
        "sunday",
    ]

    if len(day) > 0:
        start_day = days.index(day.lower())
        fin_day = start_day

    # Setup finish time info
    fin_h = start_h
    fin_m = start_m
    fin_per = start_per
    days_later = 0

    # Add minutes
    fin_m += dur_m
    if fin_m >= 60:
        fin_h += fin_m // 60
        fin_m = fin_m % 60
    fin_m = str(fin_m)
    if len(fin_m) == 1:
        fin_m = "0" + fin_m

    # Add hours
    fin_h += dur_h
    if start_h < 12 and fin_h == 12:
        if fin_per == "AM":
            fin_per = "PM"
        else:
            fin_per = "AM"
            days_later += 1
    elif fin_h > 12:
        if ((fin_h // 12) % 2) != 0:
            if fin_per == "AM":
                fin_per = "PM"
            else:
                fin_per = "AM"
                days_later += 1
        if dur_h > 23:
            days_later += dur_h // 24
        fin_h = fin_h % 12
        if fin_h == 0:
            fin_h = 12
    fin_h = str(fin_h)

    # Final day of the week
    if len(day) > 0:
        fin_day += days_later
        if fin_day > 6:
            fin_day = fin_day % 7

    # Construct new time
    new_time = fin_h + ":" + fin_m + " " + fin_per
    if len(day) > 0:
        new_time = new_time + f", {days[fin_day].capitalize()}"
    if days_later == 1:
        new_time = new_time + " (next day)"
    if days_later > 1:
        new_time = new_time + f" ({days_later} days later)"

    return new_time
