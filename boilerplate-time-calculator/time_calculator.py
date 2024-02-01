def add_time(start, duration, start_day=None):
    # Parse start time
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))
    
    # Parse duration time
    duration_hour, duration_minute = map(int, duration.split(':'))

    # Calculate total minutes
    total_minutes = start_hour * 60 + start_minute + duration_hour * 60 + duration_minute

    # Calculate days and remaining minutes
    days_later = total_minutes // (24 * 60)
    remaining_minutes = total_minutes % (24 * 60)

    # Calculate new hour and minute
    new_hour, new_minute = divmod(remaining_minutes, 60)

    # Determine period (AM/PM) and handle period change at 12:00
    new_period = period
    change = False
    if (start_hour + new_hour) >= 12:
        new_period = 'AM' if period == 'PM' else 'PM'
    if period == 'PM' and new_period == 'AM':
        change = True
        days_later += 1
    if new_hour >= 12:
        new_hour -= 12
    # Correct midnight representation  
    if new_hour == 0:  
        new_hour = 12

    # Format new time
    new_time = f"{new_hour}:{new_minute:02d} {new_period}"

    # Add days later to output if applicable
    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"

    # Add start day if provided
    if start_day:
        start_day = start_day.capitalize()
        if days_later > 0:
            # Calculate new day index and adjust
            days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
            start_day_index = days_of_week.index(start_day)
            new_day_index = (start_day_index + days_later) % 7
            new_day = days_of_week[new_day_index]

            # Adjust output to include the day of the week
            if days_later == 1:
                new_time += f", {new_day} (next day)"
            else:
                new_time += f", {new_day}"

    return new_time
