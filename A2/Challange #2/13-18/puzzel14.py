from datetime import datetime, timedelta

start_date_str = '01/01/2001'
start_date_obj = datetime.strptime(start_date_str, "%m/%d/%Y")

end_date_str = '12/31/2100'
end_date_obj = datetime.strptime(end_date_str, "%m/%d/%Y")

friday_the_13ths = 0
while start_date_obj != end_date_obj:
    weekday = start_date_obj.weekday()
    day = start_date_obj.day

    if weekday == 4 and day == 13:
        friday_the_13ths += 1

    start_date_obj += timedelta(days=1)

print(f"fridays that happen to fall on the 13th this century: {friday_the_13ths}")