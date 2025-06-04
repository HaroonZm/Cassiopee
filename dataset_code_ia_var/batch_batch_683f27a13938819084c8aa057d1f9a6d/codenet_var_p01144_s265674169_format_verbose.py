#!/usr/bin/env python

import os
import sys
import itertools
import math
from collections import Counter, defaultdict

class BillPenaltyCalculator(object):

    def __init__(self):
        pass

    def calculate_total_penalty(self):
        """
        Reads input for bills, their amounts, and associated penalty rates.
        Calculates the minimal total penalty based on the available money.
        Continues processing until two zeros are entered.
        """
        while True:
            total_number_of_bills, available_money = map(int, raw_input().split())

            if total_number_of_bills == 0 and available_money == 0:
                break

            list_of_bills_with_penalty = []

            for bill_index in range(total_number_of_bills):
                bill_amount, penalty_per_unit = map(int, raw_input().split())
                list_of_bills_with_penalty.append((penalty_per_unit, bill_amount))

            list_of_bills_with_penalty.sort(reverse=True)

            remaining_money = available_money
            total_penalty = 0

            for penalty_per_unit, bill_amount in list_of_bills_with_penalty:
                remaining_money -= bill_amount

                if remaining_money < 0:
                    unpaid_bill_amount = -remaining_money
                    total_penalty += unpaid_bill_amount * penalty_per_unit
                    remaining_money = 0

            print total_penalty

        return None

if __name__ == '__main__':
    bill_penalty_calculator = BillPenaltyCalculator()
    bill_penalty_calculator.calculate_total_penalty()