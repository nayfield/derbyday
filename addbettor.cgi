#!/usr/bin/python

import redis
import sys
import cgi, cgitb
cgitb.enable()

form = cgi.FieldStorage()

print "Content-type:text/html\r\n\r\n"
print "<html><head>"
print "<title>DerbyDay add bettor</title>"
print "</head><body>"
print '<p style="font-size:22px">'

if "newbettor" in form:
    myr=redis.Redis()
    myr.sadd('derby:bettors', form.getfirst("newbettor"))
    print "added new bettor", form.getfirst("newbettor")
    print '<p>'
    print '[<a href="placebet.cgi">Back to Place Bet</a>]'
else:
    print '<form action="addbettor.cgi" method="post" style="font-size:22px">'
    print 'Bettor: <input type="text" name="newbettor">'
    print '<input type="submit" value="Add">'
    print '</form>'
    print '<p>'
    print '[<a href="placebet.cgi">Cancel</a>]'

print '</p>'
print "</body></html>"
