#!/usr/bin/python

def header(title="fixme"):
    print "Content-type:text/html\r\n\r\n"
    print "<html><head>"
    print "<title>", title, "</title>"
    print "</head><body>"

def footer():
    print '</p>'
    print "</body></html>"

#print '<table border=1 style="font-size:22px">'
#print '<tr><th>Horse</th><th>Bettor</th><th>Amount</th></tr>'
#for horse in nsorted(myr.keys('derby:bet:*')):
#    for bettor in myr.hkeys(horse):
#        print "<tr><td>", horse.split(':')[2], "</td>"
#        print "<td>", bettor, "</td>"
#        print "<td> $", myr.hget(horse, bettor), "</td>"
#print "</table>"
#
#print '<p>'
#print '[<a href="placebet.cgi">Place Bet</a>]'
#print '[<a href="tote.cgi">Tote Board</a>]'
