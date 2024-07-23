"""
Author: Pavith Bambaravanage
URL: https://github.com/Pavith19
"""
tests = int(input())

for x in range(tests):
    meals_given = int(input())
    
    names = {}
    
    for y in range(meals_given):
        meal = input().split()
        
        by_whom = meal[0]
        count = int(meal[1])
        to_whom = meal[2:]
        
        if by_whom not in names:
            names[by_whom] = count
        else:
            names[by_whom] += count
            
        for i in to_whom:
            if i not in names:
                names[i] = -1
            else:
                names[i] -= 1
        
    meals_to_buy = sum([x for x in names.values() if x > 0])
    days = max(names.values())
    
    print(meals_to_buy, days)       
