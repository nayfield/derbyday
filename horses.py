#!/usr/bin/python

import redis
import sys

myr=redis.Redis()

if sys.argv[1] == 'add':
	for horse in xrange(2,len(sys.argv)):
		print 'adding', horse
		print myr.sadd('derby:horses', sys.argv[horse])

elif sys.argv[1] == 'list':
	print myr.smembers('derby:horses')

elif sys.argv[1] == 'del':
	for horse in xrange(2,len(sys.argv)):
		print 'deleting', horse
		print myr.srem('derby:horses',sys.argv[horse])

elif sys.argv[1] == 'load':
	myr.delete('derby:horses')
	for horse in open(sys.argv[2]):
		print myr.sadd('derby:horses', horse.rstrip())
	
