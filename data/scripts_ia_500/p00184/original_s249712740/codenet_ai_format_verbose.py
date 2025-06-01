import sys
from sys import stdin
from collections import defaultdict

input = stdin.readline

def main(arguments):
    
    while True:
        
        number_of_visitors = int(input())
        
        if number_of_visitors == 0:
            break
        
        age_group_counters = defaultdict(int)
        
        for _ in range(number_of_visitors):
            
            visitor_age = int(input())
            
            if visitor_age < 10:
                age_group_counters['under_10'] += 1
            elif visitor_age < 20:
                age_group_counters['from_10_to_19'] += 1
            elif visitor_age < 30:
                age_group_counters['from_20_to_29'] += 1
            elif visitor_age < 40:
                age_group_counters['from_30_to_39'] += 1
            elif visitor_age < 50:
                age_group_counters['from_40_to_49'] += 1
            elif visitor_age < 60:
                age_group_counters['from_50_to_59'] += 1
            else:
                age_group_counters['60_and_above'] += 1
        
        print(age_group_counters['under_10'])
        print(age_group_counters['from_10_to_19'])
        print(age_group_counters['from_20_to_29'])
        print(age_group_counters['from_30_to_39'])
        print(age_group_counters['from_40_to_49'])
        print(age_group_counters['from_50_to_59'])
        print(age_group_counters['60_and_above'])

if __name__ == '__main__':
    main(sys.argv[1:])