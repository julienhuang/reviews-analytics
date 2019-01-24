#留言分析程式pratice
# step01:讀取檔案
data = []
count = 0
with open('reviews.txt', 'r') as reviews:
	for line in reviews:
		data.append(line) #將每一筆資料(line)加入data資料夾
		count += 1 # 等同於 "count = count + 1"的快寫法
		if count % 1000 == 0:  # "%"的意思是"求餘數", 也就是count除以1000之後的餘數等於0
			print(len(data)) #每讀1000行就印出一次長度
print('檔案讀取完了, 總共有: ', len(data), '筆資料') #印出data長度

print(data[0])
print('-----------------')
print(data[1])

#算每筆留言資料的平均長度
total_length = 0
for single_data in data:
	total_length += len(single_data)
avg_length = total_length / len(data)
print('平均留言長度為:', avg_length, '字數')

#篩選出長度少於100字的留言
new_list = []
for single_data in data:
	if len(single_data) < 100:
		new_list.append(single_data) #長度少於100字的裝進新的清單"new_list"
print('長度少於100字的留言一共有:', len(new_list), '筆留言')
print(new_list[0])

