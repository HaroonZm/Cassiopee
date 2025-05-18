ref={"A":"BD","B":"ACE","C":"BF","D":"AEG","E":"BDFH","F":"CEI","G":"DH","H":"EGI","I":"HF"}
for i in range(1000):
	p=raw_input()
	for i in range(len(p)-1):
		if p[i+1] not in ref[p[i]]:
			break
	else:
		print p