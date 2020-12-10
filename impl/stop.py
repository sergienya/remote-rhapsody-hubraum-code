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
from skill_sdk.l10n import _
import shelve
import datetime
import time
from .srg_utils import get_user_id, is_same_date


@skill.intent_handler('TEAM_23_STOP_INTENT')
def handler() -> Response:
    """ A very basic handler of TEAM_23_STOP_INTENT intent,
        TEAM_23_STOP_INTENT intent is activated when user says "Beende die Arbeit" or "Beende die Pause" or "Beende"
        returns the confirmation and stop time tracking

    :return:        Response
    """

    print(context)
    user_id = get_user_id(context)
    print(user_id)

    with shelve.open('db.txt', writeback=True) as db:
        if user_id not in db:
            msg = _('NO_STOP_TRACKING')
            response = tell(msg)
            return response

        else:
            user_data = db[user_id]

            # if the date is not today, remove everything
            today = datetime.date.today()
            today = {'month': today.month, 'day': today.day}
            print(today)
            now = time.time()
            print(now)

            if 'date' not in user_data or not is_same_date(today, user_data['date']):
                print("different dates or no date - clear stats and add today's date")
                user_data = {'data': []}
                db[user_id] = user_data
                msg = _('NO_STOP_TRACKING')
                response = tell(msg)
                return response

            #user_data['date'] = {'month': today.month, 'day': today.day}

            if 'start_cat' in user_data:
                curr_cat = user_data['start_cat']
                curr_start_time = user_data['start_time']
                time_delta = now - curr_start_time
                print("time_delta" + str(time_delta))

                # Close current category tracker
                record = next((item for item in user_data['data'] if item['cat'] == curr_cat), None)
                if record is None:
                    user_data['data'].append({'cat': curr_cat, 'sum_time': time_delta})
                else:
                    record['sum_time'] = record['sum_time'] + time_delta

                # Remove old tracker
                del user_data['start_cat']
                del user_data['start_time']
            else:
                msg = _('NO_STOP_TRACKING')
                response = tell(msg)
                return response

            db[user_id] = user_data

    # We get a translated message
    msg = _('STOP_TRACKING')
    # We create a simple response
    response = tell(msg)
    # We return the response
    return response
