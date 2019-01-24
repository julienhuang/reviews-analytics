#留言分析程式pratice
# step01:讀取檔案
data = []
count = 0
with open('reviews.txt', 'r') as reviews:
	for line in reviews:
		data.append(line)
		count += 1 # 等同於 "count = count + 1"的快寫法
		if count % 1000 == 0:  # "%"的意思是"求餘數", 也就是count除以1000之後的餘數等於0
			print(len(data)) #每讀1000行就印出一次長度
print(len(data)) #印出data長度
print(data[0])
print('-----------------')
print(data[1])
