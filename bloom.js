function knrhash(s,l){
	var h=0;
	var d=31;
	for(var i=0;i<s.length;i++){
		var c=s[i].charCodeAt(0);
		h=(h*d+c)%l;
	}
	return h%l;
}
function djbhash(s,l){
	var h=5381;
	for(var i=0;i<s.length;i++){
		var c=s[i].charCodeAt(0);
		h=((h*33)^c)%l;
	}
	return h%l;
}

function checkbloom(bloom,domain){
	const algos=[knrhash,djbhash];
	const bint_size = 32;
	var blocksize = 1+Math.floor(bloom.size/bint_size);
	var pcont = true;
	for(var ih=0;ih<algos.length;ih++){
		var h = algos[ih](domain,bloom.size);
		var prob_cont = (bloom.bloom[Math.floor(h/bint_size)+ih*blocksize] & (1 << (h%bint_size)))>0;
		pcont = pcont && prob_cont;
	}
	return pcont;
}
