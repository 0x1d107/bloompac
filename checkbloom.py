import json,sys
def knrhash(s,l):
	h = 0
	d = 31
	for c in s:
		h*=d
		h+=ord(c)
		h%=l
	return h%l
def djbhash(s,l):
	h=5381
	for c in s:
		h = (h*33)^ord(c)
		h%=l
	return h%l
algos=(knrhash,djbhash)
with open('bloom.json') as f:
	bloom_j = json.load(f)
	bloom = bloom_j['bloom']
	bloom_size = bloom_j['size']
	bint_size=32
	domain=sys.argv[1]
	pcont = True
	for ih,hsh in enumerate(algos):
		h=hsh(domain,bloom_size)
		blocksize = 1+bloom_size//bint_size
		prob_cont = bloom[h//bint_size+ih*blocksize] & 1<< (h%bint_size) > 0
		pcont= pcont and prob_cont
	if pcont:
		print(domain)
