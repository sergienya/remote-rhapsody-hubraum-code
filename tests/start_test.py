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

    def test_category_work(self):
        """ Mock random number to return 5 and ensure we won the game
        """
        response = skill.test_intent('TEAM_23_START_INTENT', category=[' die Arbeit'])
        self.assertEqual(response.text.key, 'START_TRACKING_WORK')

    def test_category_break(self):
        """ Mock random number to return 1 and ensure we lost the game
        """
        response = skill.test_intent('TEAM_23_START_INTENT', category=[' die Pause'])
        self.assertEqual(response.text.key, 'START_TRACKING_BREAK')

    def test_unknown_category(self):
        """ Supply a non-numerical value and ensure the implementation returns the error
        """
        response = skill.test_intent('TEAM_23_START_INTENT', category=[' hallo'])
        self.assertEqual(response.text.key, 'START_TRACKING_ELSE')
