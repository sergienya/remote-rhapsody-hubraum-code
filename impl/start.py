#
# voice-skill-sdk
#
# (C) 2020, YOUR_NAME (YOUR COMPANY), Deutsche Telekom AG
#
# This file is distributed under the terms of the MIT license.
# For details see the file LICENSE in the top directory.
#
#
from skill_sdk import skill, Response, tell, context
#from skill_sdk import skill, Response, tell
#from skill_sdk.intents import context
from skill_sdk.l10n import _
from skill_sdk.services.persistence import PersistenceService
import datetime
import time
from .srg_utils import get_user_id, is_same_date, is_arbeit, is_pause, start_with_article


@skill.intent_handler('TEAM_23_START_INTENT')
def handler(category: str) -> Response:
    """ A very basic handler of TEAM_23_START_INTENT intent,
        TEAM_23_START_INTENT intent is activated when user says "Starte die Arbeit" or "Starte die Pause"
        returns the confirmation and start time tracking

    :return:        Response
    """
    #print(context.attributesV2.get("user_id")['value'])
    print(context)
    #print(context.attributesV2.get("user_id")[0]['value'])
    user_id = get_user_id(context)
    print(user_id)

    print(category)
    # We get a translated message
    if not category:
        msg = _('START_TRACKING_ELSE', category='')
        resolved_category = ''
    elif is_arbeit(category.lower()):
        msg = _('START_TRACKING_WORK')
        resolved_category = _('CATEGORY_WORK')
    elif is_pause(category.lower()):
        msg = _('START_TRACKING_BREAK')
        resolved_category = _('CATEGORY_BREAK')
    else:
        category = category.strip().lower()
        if start_with_article(category):
            category = category[4:]
        resolved_category = category.strip()
        msg = _('START_TRACKING_ELSE', category=resolved_category.title())

    print('>' + resolved_category + '<')

    db = PersistenceService().get()
    if user_id in db:
        user_data = db[user_id]
    else:
        user_data = {'data': []}
    # if the date is not today, remove everything
    today = datetime.date.today()
    today = {'month': today.month, 'day': today.day}
    print(today)
    now = time.time()
    print(now)

    if 'date' not in user_data or not is_same_date(today, user_data['date']):
        print("different dates or no date - clear stats and add today's date")
        user_data = {'data': []}
        user_data['date'] = {'month': today['month'], 'day': today['day']}

    if 'start_cat' in user_data:
        curr_cat = user_data['start_cat']
        curr_start_time = user_data['start_time']
        time_delta = now - curr_start_time
        print("time_delta " + str(time_delta))

        # Close current category tracker
        record = next((item for item in user_data['data'] if item['cat'] == curr_cat), None)
        if record is None:
            user_data['data'].append({'cat': curr_cat, 'sum_time': time_delta})
        else:
            record['sum_time'] = record['sum_time'] + time_delta

    # Start new tracker
    user_data['start_cat'] = resolved_category.lower()
    user_data['start_time'] = now

    #db[user_id] = user_data
    PersistenceService().set({user_id: user_data})

    # We create a simple response
    response = tell(msg)

    # We return the response
    return response
