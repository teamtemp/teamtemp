__author__ = 'traviswarren'

from django.test import TestCase

from teamtemp.tests.factories import TeamTemperatureFactory, TeamResponseFactory


class TeamTemperatureStatsTestCases(TestCase):
    def test_stats_count(self):

        team_temp = TeamTemperatureFactory()

        self.assertEqual(team_temp.stats()['count'], 0)

        TeamResponseFactory(request=team_temp)
        self.assertEqual(team_temp.stats()['count'], 1)

        TeamResponseFactory(request=team_temp)
        TeamResponseFactory(request=team_temp)

        self.assertEqual(team_temp.stats()['count'], 3)

    def test_stats_average(self):

        team_temp = TeamTemperatureFactory()

        self.assertIsNone(team_temp.stats()['average']['score__avg'])

        TeamResponseFactory(request=team_temp, score=5)

        self.assertEqual(team_temp.stats()['average']['score__avg'], 5.0)

        TeamResponseFactory(request=team_temp, score=7)
        TeamResponseFactory(request=team_temp, score=6)

        self.assertEqual(team_temp.stats()['average']['score__avg'], 6.0)

    def test_stats_word(self):

        team_temp = TeamTemperatureFactory()

        self.assertEqual(len(team_temp.stats()['words']), 0)

        TeamResponseFactory(request=team_temp, word='first')

        self.assertEqual(len(team_temp.stats()['words']), 1)

        TeamResponseFactory(request=team_temp, word='second')
        TeamResponseFactory(request=team_temp, word='third')

        self.assertEqual(len(team_temp.stats()['words']), 3)
