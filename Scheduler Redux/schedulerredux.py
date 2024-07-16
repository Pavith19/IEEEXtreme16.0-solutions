from collections import defaultdict

mod = 1000000007

num_jobs, num_workers = map(int, input().split())

jobs = list(map(int, input().split()))

if num_workers == 1:
    sum = 0
    
    for i in range(num_jobs):
        sum += pow(2, jobs[i], mod)
        
    print(sum % mod)
    
else:
    jobs.sort(reverse = True)
    
    number_of_each_job = defaultdict(int)
    
    max_time = jobs[0]
    times = []
    times.append(max_time)
    
    for i in range(num_jobs):
        number_of_each_job[jobs[i]] += 1
        
        x = jobs[i]
        
        while number_of_each_job[x] == 2 and x != max_time:
            number_of_each_job[x] = 0
            x += 1
            number_of_each_job[x] += 1
            
        if number_of_each_job[max_time] == num_workers:
            if i < num_jobs - 1:
                times.append(jobs[i + 1])
                number_of_each_job[max_time] = 0
                max_time = jobs[i + 1]
                
    sum = 0
    
    for time in times:
        sum += pow(2, time, mod)
        
    print(sum % mod)
