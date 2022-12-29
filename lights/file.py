import math
"""
def gradient(pattern, percent):
	i = 0
	while True:

		
		if i + 2 >= len(pattern):
			return pattern[i]
		elif percent < pattern[i+3]:
			p = (percent - pattern[i+1]) / (pattern[i+3]-pattern[i+1])
			return [pattern[i][j]+math.floor((pattern[i+2][j] - pattern[i][j])*p) for j in range(3)]
		i += 2
pattern = ((100, 50, 0), 0, (255, 255, 255), 25, (200, 0, 200), 100)
for i in range(0, 101):
	print(i, gradient(pattern, i))"""

def layer(base, top):
	return [math.floor(base[i] + (top[i] - base[i]) * (top[3]/100)) for i in range(3)]
