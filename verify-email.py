#!/usr/bin/env python
'''
Copyright (C) 2015-Present Juan Espinoza

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''
import subprocess
import sys
import telnetlib

if len(sys.argv) == 1:
    print "ERROR:\tYou must provide an email address you wish to validate."
    sys.exit(1)

rcpt = 'rcpt to:<%s>\n' % str(sys.argv[1])
domain = str(sys.argv[1]).split('@')[1]

server = (subprocess.check_output(['dig', '+short', domain,'MX'])).split('\n')
server.pop()
server.sort()
server = (server[0]).split(' ')[1].rsplit('.', 1)[0]

#============================[ TELNET SESSION ]=================================
telnet = telnetlib.Telnet(server, "25")
telnet.write('ehlo computer.com\n')
telnet.write('mail from:<otto@earth.org>\n')
telnet.write(rcpt)
telnet.write('quit\n')

return_code = (telnet.read_all().split('\n')[-3]).split(' ')[0]

if return_code != '250':
    print '%r is *NOT* a valid recpient on %s' % (str(sys.argv[1]), domain)
    sys.exit(2)
else:
    print '%r is a valid recpient on %s' % (str(sys.argv[1]), domain)
    sys.exit(0)
