n = int(input())
i = 1
odd_list = []
while i <=n:
	if i%2 == 1:
		odd_list.append(i)
	i+=1
print(odd_list)