#!/usr/bin/python

import redis
import sys

myr=redis.Redis()

if sys.argv[1] == 'add':
	bettor=sys.argv[2]
	horse=sys.argv[3]
	amount=int(sys.argv[4])
	print myr.hincrby(('bet:'+horse),bettor,amount)

elif sys.argv[1] == 'list':
	for horse in myr.keys('bet:*'):
		for bettor in myr.hkeys(horse):
			print horse, bettor, myr.hget(horse, bettor)

elif sys.argv[1] == 'del':
	bettor=sys.argv[2]
	horse=sys.argv[3]
	bet = myr.hget(('bet:'+horse),bettor)
	print "Refund", bettor, bet
	print myr.hdel(('bet:'+horse),bettor)

else:
	print "Usage:", sys.argv[0], "add|list|del"
	print "  add rod secretariat 5"
	print "  list"
	print "  del rod secretariat"
