data = []
count = 0
with open ('reviews.txt' , 'r') as f:
	for line in f:
		data.append(line)
		count = count + 1
		#if count % 1000 == 0:
			#print(len(data))
print('檔案讀取完了,總共有', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
	#print(sum_len)

print('平均是', sum_len/len(data), '字數')

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '留言小於一百個字')
print(new[0])


good = []
good_count = 0
for d in data:
	if 'good' in d:
		good.append(d)
		good_count = good_count + 1
print(good_count)