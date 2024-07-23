"""
Author: Pavith Bambaravanage
URL: https://github.com/Pavith19
"""
tests = int(input())

for test in range(tests):
    angles = list(map(int, input().split()))
    del angles[0]
    cuts = set()
    
    for i in range(len(angles)):
        cuts.add(angles[i]%180)
        
    if len(cuts) == 0:
        print(1)
    else:print(len(cuts)*2)
