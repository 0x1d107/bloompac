all: proxy.pac checkbloom.js
proxy.pac:proxy.pac.in bloom.json bloom.js
	cpp -nostdinc -CC -P -undef proxy.pac.in > proxy.pac
checkbloom.js:checkbloom.js.in bloom.json bloom.js
	cpp -nostdinc -CC -P -undef checkbloom.js.in > $@
bloom.json: ct.json mkbloom.py
	python3 mkbloom.py > bloom.json
ct.json:
	bash fetchct.sh
clean:
	rm -f checkbloom.js proxy.pac ct.json
.PHONY: clean
