#!/usr/bin/python3

import sys
"""Dicts in order to map state/capital equivalence"""
def process_input(input_str: str):
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
    
    def normalize_string(s):
        return " ".join(s.split()).strip().lower()
    
    expressions = input_str.split(',')
    
    results = []
    
    for expr in expressions:
        expr_normalized = normalize_string(expr)
        if expr_normalized == '':
            continue
        
        found = False
        
        for state, code in states.items():
            if normalize_string(state) == expr_normalized:
                for abbr, city in capital_cities.items():
                    if abbr == code:
                        results.append(f"{city} is the capital of {state}")
                        found = True
                        break
                if found:
                    break
        
        if not found:
            for abbr, city in capital_cities.items():
                if normalize_string(city) == expr_normalized:
                    state = [state for state, code in states.items() if code == abbr][0]
                    results.append(f"{city} is the capital of {state}")
                    found = True
                    break
        
        if not found:
            results.append(f"{expr.strip()} is neither a capital city nor a state")
    
    for result in results:
        print(result)

def main():
    if len(sys.argv) == 2:
        input_str = sys.argv[1]
        if ',,' in input_str:
            return
        process_input(input_str)

if __name__ == '__main__':
    main()

