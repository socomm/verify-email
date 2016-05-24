# Overview #

**verify-email** is command-line utility designed to help verify an e-mail 
address.

Simply provide the user's email address and the script will connect to the 
user's domain mail-exchange server, via SMTP, and verify the user's mailbox 
exists.

# License #

GPLv3, with full license available in LICENSE file.

# Requirements and Dependencies #

This program requires the following python modules:

- sys
- subprocess
- telnetlib

# Usage #

./verify-email.py user_name@example.com

Script will return 0 on valid email address, non-zero on invalid email address.
