import time
def load_data(filename):
    with open(filename, 'r') as f:
        data = f.readlines()
    data = [d.strip().split(',') for d in data]
    data = [(int(d[0]), int(d[1])) for d in data]
    return data

def knapSack(W, wt, val, n):
    if n == 0 or W == 0 :
        return 0

    if (wt[n-1] > W):
        return knapSack(W, wt, val, n-1)
    else:
        return max(val[n-1] + knapSack(W-wt[n-1], wt, val, n-1),
                   knapSack(W, wt, val, n-1))

filename = 'output30.txt'
data = load_data(filename)
val = [d[1] for d in data]
wt = [d[0] for d in data]
W = 50
n = len(val)

start_time = time.time()
result = knapSack(W, wt, val, n)
end_time = time.time()

print("Resultado: ", result)
print("Tempo gasto: ", end_time - start_time, " segundos")