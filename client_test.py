import unittest
from client3 import getDataPoint, calculatePriceBidGreaterThanAsk, getRatio


class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
                'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:

            testdata = (quote['stock'], quote['top_bid']['price'], quote['top_ask']
                        ['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2)

            self.assertEqual(getDataPoint(
                quote), testdata, "Error, data point calculation has incorrect attributes")

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
                'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 127.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """

        for quote in quotes:
            self.assertEquals(calculatePriceBidGreaterThanAsk(
                quote), quote['top_bid']['price'] > quote['top_ask']['price'], "Error result compares if bid is greater than ask")

    """ ------------ Add more unit tests ------------ """

    def test_getRatio(self):
        ratios = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
                'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        prices = [
            {"price1": 0, "price2": 2},
            {"price1": 10, "price2": 12},
            {"price1": 12, "price2": 10}
        ]

        for price in prices:
            self.assertEqual(
                getRatio(price["price1"], price["price2"]), price["price1"] / price["price2"])

        self.assertEqual(
            getRatio(50, 0), "Illegal operation: Zero division error")


if __name__ == '__main__':
    unittest.main()
