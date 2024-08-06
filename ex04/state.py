#!/usr/bin/python3

import sys

def print_state(city: str):
    states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO"
    }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }
    
    # Find the state code by the capital city
    state_code = None
    for code, capital in capital_cities.items():
        if capital == city:
            state_code = code
            break
    
    if not state_code:
        print("Unknown capital city")
        return
    
    # Find the state name by the state code
    for state, code in states.items():
        if code == state_code:
            print(state)
            return

def main():
    if len(sys.argv) == 2:
        print_state(sys.argv[1])

if __name__ == '__main__':
    main()