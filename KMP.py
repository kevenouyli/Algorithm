def partial_table(p):
	'''''partial_table("ABCDABD") -> [0, 0, 0, 0, 1, 2, 0]'''
	prefix = set()
	postfix = set()
	ret = [0]
	for i in range(1,len(p)):
		prefix.add(p[:i])
		# print('prefix:',prefix)
		postfix = {p[j:i+1] for j in range(1,i+1)}
		# print('postfix:',postfix)
		ret.append(len((prefix&postfix or {''}).pop()))
	print(ret)
	return ret

def kmp_match(s, p):
	m = len(s); n = len(p)
	cur = 0#起始指针cur
	table = partial_table(p)
	while cur<=m-n:
		for i in range(n):
			if s[i+cur]!=p[i]:
				cur += max(i - table[i-1], 1)
				break
			elif i==n-1:
				return cur
			else:
				next

	return False

print (kmp_match("BBC ABCDAB ABCD23ABCDABDE", "ABCDABD"))
print("BBC ABCDAB ABCD23ABCDABDE"[17])