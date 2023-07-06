import unittest
from client3 import getDataPoint
from client3 import getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    test_price1 = (121.2 + 120.48) / 2
    test_price2 = (121.68 + 117.87) / 2

    prices = {}
    for quote in quotes:
      stock, bid_price, ask_price, price = getDataPoint(quote)
      prices[stock] = price

    self.assertEqual(prices["ABC"], test_price1, '\n\n*** Incorrect stock price' + ' ***\n')
    self.assertEqual(prices["DEF"], test_price2, '\n\n*** Incorrect stock price' + ' ***\n')

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    differences = {}
    for quote in quotes:
      stock, bid_price, ask_price, price = getDataPoint(quote)
      differences[stock] = bid_price - ask_price

    self.assertGreater(differences["ABC"], 0, '\n\n*** Bid not greater than ask' + ' ***\n')
    self.assertGreater(differences["DEF"], 0, '\n\n*** Bid not greater than ask' + ' ***\n')

if __name__ == '__main__':
    unittest.main()
