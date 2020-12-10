import datetime

def get_user_id(context):
    user_id = "13456"
    try:
        user_id = context.attributesV2.get("user_id")[0]['value']
    finally:
        return user_id


def is_same_date(date1, date2):
    return date1['month'] == date2['month'] and date1['day'] == date2['day']

def convert_to_duration(sum_time):
    td = datetime.timedelta(seconds=sum_time)
    hours, minutes, seconds = td.seconds // 3600, td.seconds // 60 % 60, td.seconds % 60

    #return (str(hours) + "h " if hours != 0 else "") + str(minutes) + "m"
    return (str(hours) + "h " if hours != 0 else "") + \
           (str(minutes) + "m " if minutes != 0 else "") + \
           (str(seconds) + "s" if seconds != 0 else "")
