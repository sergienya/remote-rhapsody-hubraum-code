#
# voice-skill-sdk
#
# (C) 2020, YOUR_NAME (YOUR COMPANY), Deutsche Telekom AG
#
# This file is distributed under the terms of the MIT license.
# For details see the file LICENSE in the top directory.
#
#
from skill_sdk import skill, Response, tell, Card, context
#from skill_sdk.intents import context
from skill_sdk.l10n import _
import shelve
import datetime
import time
from .srg_utils import get_user_id, is_same_date, convert_to_duration

def check_none(str):
    return _('NO_TIME') if len(str) == 0 else str

@skill.intent_handler('TEAM_23_STATS_INTENT')
def handler() -> Response:
    """ A very basic handler of TEAM_23_STATS_INTENT intent,
        TEAM_23_STATS_INTENT intent is activated when user says "Zeige Statistiken"
        returns the card with statistics

    :return:        Response
    """
    #print(context.attributesV2.get("user_id"))
    print(context)

    user_id = get_user_id(context)
    print(user_id)


    with shelve.open('db.txt') as db:
        if user_id not in db:
            msg = _('NO_STATS')
            response = tell(msg)
            return response


        user_data = db[user_id]
        print(user_data)

        # if the date is not today, remove everything
        today = datetime.date.today()
        today = {'month': today.month, 'day': today.day}
        print(today)

        if 'date' not in user_data or not is_same_date(today, user_data['date']) or 'data' not in user_data or len(user_data['data']) == 0:
            print("no stats for today")
            msg = _('NO_STATS')
            response = tell(msg)
            return response

        # Get stats
        data = user_data['data']
        card_text = "\n".join([item['cat'].strip().title() + ": " + check_none(convert_to_duration(item['sum_time'])) for item in data])

    # Get stats for today
    #card_text = 'Proj 1: 5h 35m\nProj 2: 1h 3m'
    print(card_text)
    # Get data
    card_date = str(today['day']) + '.' + str(today['month']) + '.2020'

    # We get a translated message
    msg = _('STATS_TEXT')

    # We create a simple response
    response = tell(msg)

    response.card = Card(
        title_text=_("CARD_SKILL_TITLE"),
        text=_("CARD_SKILL_SUBTITLE", date=card_date),
        sub_text=card_text
    )

    # We return the response
    return response
