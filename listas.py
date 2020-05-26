Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> hostnames=["R1","R2","R3","S1","S2"]
>>> type(hostnames)
<class 'list'>
>>> len(hostnames)
5
>>> hostnames
['R1', 'R2', 'R3', 'S1', 'S2']
>>> hostnames[0]
'R1'
>>> hostnames[-6]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    hostnames[-6]
IndexError: list index out of range
>>> hostnames[5]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    hostnames[5]
IndexError: list index out of range
>>> hostnames[0]="RTR1"
>>> hostnames
['RTR1', 'R2', 'R3', 'S1', 'S2']
>>> ipaddress={"R1":"10.1.1.1","R2":"10.2.2.1","R3":"10.3.3.1"}
>>> type(ipaddress)
<class 'dict'>
>>> 