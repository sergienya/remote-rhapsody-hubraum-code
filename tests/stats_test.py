#
# voice-skill-sdk
#
# (C) 2020, YOUR_NAME (YOUR COMPANY), Deutsche Telekom AG
#
# This file is distributed under the terms of the MIT license.
# For details see the file LICENSE in the top directory.
#
#
from unittest import mock
import unittest

from impl.number import skill


class TestMain(unittest.TestCase):

    def test_show_statistics(self):
        """ Mock random number to return 5 and ensure we won the game
        """
        response = skill.test_intent('TEAM_23_STATS_INTENT')
        self.assertEqual(response.text.key, 'START_TRACKING_WORK')
        # self.assertEqual(response.text.key, 'START_TRACKING_WORK')
        # self.assertEqual(response.text.key, 'START_TRACKING_WORK')
        # self.assertEqual(response.text.key, 'START_TRACKING_WORK')
        # self.assertEqual(response.text.key, 'START_TRACKING_WORK')
