import json
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
with open('ct.json') as f:
	blocked = json.load(f)
	bloom_size = len(blocked)*11
	bint_size = 32
	blocksize = 1+bloom_size//bint_size
	bloom = [0]*(blocksize*len(algos))
	for b in blocked:
		for ih,hsh in enumerate(algos):
			h = hsh(b,bloom_size)
			bloom[h//bint_size+ih*blocksize] |= 1<<(h%bint_size)
	print(json.dumps({'bloom':bloom,'size':bloom_size}),end='')
