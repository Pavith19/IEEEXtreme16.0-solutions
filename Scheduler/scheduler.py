# To get 100% points, you have to use Pypy3 instead of Python3
jobs, workers = map(int, input().split())

times = list(map(int, input().split()))

if workers > 1:
    print(2 ** max(times)%1000000007)
else:
    total = 0
    for i in times:
        total += 2 ** i
    print(total%1000000007)
