print ('Starting...')
a = int(input('How many MB> '))
end = a*10*10*10*10*10
f = open('testfile.try.txt', 'w')
start = 0
while (start < end):
	f.write('testfile \n')
	start = start + 1
	print ('(Till End missing ',end / start, '%  from ' ,end, ' till ', start)
f.close()
