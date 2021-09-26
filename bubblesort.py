def bubblesort(data):
    n = len(data)
    for i in range(n-2):
        for j in range(n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]