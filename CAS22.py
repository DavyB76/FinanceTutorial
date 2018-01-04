import unittest

from RateEquivalenceProccessing import ProcessEquivalenMoneyMarketRate


class TestCAS22_ContinuousRates(unittest.TestCase):

    def test_should_return_equivalent_money_market_rate_with_period_equals_2_when_annual_rate_is_6_percent(self):
        actual = ProcessEquivalenMoneyMarketRate(0.06, 2)
        self.assertEqual(actual, 0.05912602819739998)

    def test_should_return_equivalent_money_market_rate_with_period_equals_4_when_annual_rate_is_6_percent(self):
        actual = ProcessEquivalenMoneyMarketRate(0.06, 4)
        self.assertEqual(actual, 0.0586953846746372)

    def test_should_return_equivalent_money_market_rate_with_period_equals_12_when_annual_rate_is_6_percent(self):
        actual = ProcessEquivalenMoneyMarketRate(0.06, 12)
        self.assertEqual(actual, 0.05841060678411658)

    def test_should_return_equivalent_money_market_rate_with_period_equals_365_when_annual_rate_is_6_percent(self):
        actual = ProcessEquivalenMoneyMarketRate(0.06, 365)
        self.assertEqual(actual, 0.05827355942028878)

    def test_should_return_equivalent_money_market_rate_with_period_equals_1000000_when_annual_rate_is_6_percent(self):
        actual = ProcessEquivalenMoneyMarketRate(0.06, 1000000)
        self.assertEqual(actual, 0.05826890991933453)


    