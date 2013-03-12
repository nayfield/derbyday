#!/usr/bin/python

import redis
import sys
import cgi, cgitb
from nicesort import nsorted

cgitb.enable()

myr=redis.Redis()

# total bets

form = cgi.FieldStorage()

print "Content-type:text/html\r\n\r\n"
print "<html><head>"
print "<title>DerbyDay Place Bet</title>"
print "</head><body>"


limit = int(myr.get('derby:betlimit'))

if "bettor" not in form:
	print '<form action="placebet.cgi" method="post" style="font-size:22px;">'
	print 'Bettor: <select name=bettor size=21 style="vertical-align:top;">'
	for bettor in nsorted(myr.smembers('derby:bettors')):
		print '<option', ('value="'+bettor+'">')
		print bettor, '</option>'
	print '</select>'

	print 'Horse: <select name=horse size=21 style="vertical-align:top;">'
	for horse in nsorted(myr.smembers('derby:horses')):
		print '<option', ('value="'+horse+'">')
		print horse, '</option>'
	print '</select>'

	print 'Bet: <select name=amount size=21 style="vertical-align:top;">'
	for amount in xrange(1,(limit+1)):
		print '<option', ('value="'+str(amount)+'">')
		print '$', amount, '</option>'
	print '</select>'

	print '<input type="submit" value="Place Bet">'

	print '</form>'

	print '<p>'
	print '[<a href="addbettor.cgi">Add a new bettor</a>]'
	print '[<a href="tote.cgi">Back to Tote</a>]'

else:
	bettor = form.getfirst("bettor")
	horse = form.getfirst("horse")
	amount = int(form.getfirst("amount"))
	out = myr.hget(('derby:bet:'+horse),bettor)
	tot = amount
	if out:
		tot = tot + int(out)
	if tot > limit:
		print '<p style="font-size:30px">Would be over limit!'
	else:
		myr.hincrby(('derby:bet:'+horse),bettor,amount)
		print '<p style="font-size:22px">'
		print "took bet for", bettor, " - $", amount, "on", horse
		#print ticket
	print '</p><p>'
	print '[<a href="tote.cgi">Back to Tote</a>]'
print '</p>'
print "</body></html>"
