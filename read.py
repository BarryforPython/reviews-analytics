data = []
count = 0 # 可以透過計數來知道程式目前執行的進度
with open ('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1 # 快寫法 完全等於 count = count + 1
        if count % 1000 == 0: # %是求餘數的意思 count跟1000的餘數 = 0
            print(len(data))
print(len(data))

print(data[0])
print('-------------')
print(data[1])
