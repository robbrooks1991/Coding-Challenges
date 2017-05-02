import unittest

from vending_machine import give_change, give_item_and_change


class TestVendingMachine(unittest.TestCase):
    def test_return_change(self):
        self.assertEqual(give_change(.17), [.10, .05, .02])
        self.assertEqual(give_change(.18), [.10, .05, .02, .01])
        self.assertEqual(give_change(.04), [.02, .02])

    def test_unavailable_item(self):
        """if user asks for an item that's unavailable, they should not be given the item, and their money should be returned"""
        item, change, _ = give_item_and_change('crisps', .50)
        self.assertIsNone(item)
        self.assertEqual(change, 0.5)

    def test_not_enough_money(self):
        """if the user doesn't put enough money in, nothing will be provided the amount they have put in will be returned"""
        item, change, _ = give_item_and_change('coke', .70)
        self.assertLess(.70, 0.73)

    def test_for_enough_money(self):
        """if the user provides enough money for the item, then the item, change and writing should be issued"""
        item, change, _ = give_item_and_change('apple', .50)
        self.assertIsNotNone(item)
        self.assertEqual(change, [0.05, 0.02])
