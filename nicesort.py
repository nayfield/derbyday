import re

# courtesy  http://nedbatchelder.com/blog/200712.html#e20071211T054956
def nsorted(l):
	convert = lambda text: int(text) if text.isdigit() else text
	alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
	return sorted(l, key = alphanum_key)
