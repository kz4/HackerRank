def main(destination, t, tuples):
	stack = []
	station_tuples = {}

	for leave, arrive, t1, t2 in tuples:
		if leave not in station_tuples:
			station_tuples[leave] = []
		station_tuples[leave].append((leave, arrive, t1, t2))

	found = False
	min_time = 1 << 32

	stack.append((1, 0))

	while stack:
		station, time = stack.pop(0)
		if station in station_tuples:
			for leave , arrive, t1, t2 in station_tuples[station]:
				if time + t >= t1 and t1 >= time:
					if arrive == destination:
						found = True
						min_time = min(min_time, t2)
					else:
					    stack.append((arrive, t2))

	if found:
		print 'YES', min_time
	else:
		print 'NO'


if __name__ == '__main__':
	n, m, t = map(int, raw_input().split())
	pairs = []
	for i in range(m):
		x, y, t1, t2 = map(int, raw_input().split())
		if x > 0 and x < n + 1 and y > 0 and y < n + 1:
			pairs.append((x,y,t1,t2))

	main(n, t, pairs)
