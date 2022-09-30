def read_data():
    n = int(input())
    d = [int(input()) for i in range(n)]
    return d

def get_mean(d):
    return sum(d)/len(d)

def get_median(d):
    sorted_d = sorted(d)
    n = len(d)
    return (sorted_d[(n-1)//2] + sorted_d[(n//2)/2])