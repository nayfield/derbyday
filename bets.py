#!/usr/bin/python

import redis
import sys

myr=redis.Redis()

if sys.argv[1] == 'list':
	for horse in myr.keys('derby:bet:*'):
		for bettor in myr.hkeys(horse):
			print horse.split(':')[2], "-", bettor, "-", myr.hget(horse, bettor)

elif sys.argv[1] == 'del':
	bettor=sys.argv[2]
	horse=sys.argv[3]
	bet = myr.hget(('derby:bet:'+horse),bettor)
	print "Refund", bettor, bet
	print myr.hdel(('derby:bet:'+horse),bettor)

else:
	print "Usage:", sys.argv[0], "add|list|del"
	print "  list"
	print "  del rod secretariat"
