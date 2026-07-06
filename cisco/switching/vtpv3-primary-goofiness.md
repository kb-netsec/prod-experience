TL;DR if you're sure the VTP server is and should be primary, do 'vtp primary vlan'


When working on a VTP Primary Server, and attempting to add a VLAN, I received the following error:

```
vlan 299
VTP VLAN configuration not allowed when device is not the primary server for vlan database.
```

Ok, weird. I know this should be the primary:

```
core-switchI#show vtp status
VTP Version capable             : 1 to 3
VTP version running             : 3
VTP Domain Name                 : core
VTP Pruning Mode                : Disabled (Operationally Disabled)
VTP Traps Generation            : Disabled
Device ID                       : bcd2.95be.d3c0

Feature VLAN:
--------------
VTP Operating Mode                : Server
Number of existing VLANs          : 42
Number of existing extended VLANs : 0
Maximum VLANs supported locally   : 4096
Configuration Revision            : 37
Primary ID                        : bcd2.95be.d3c0
Primary Description               : core-switch
```

Apparently for some reason switches will not keep their primary status after a reload/power outage. I'll see if I can reproduce this in the lab, but for now after doing vtp primary vlan, we can see the VTP Operating Mode
is changed to Primary Server:

```
core-switch#vtp primary vlan
This system is becoming primary server for feature vlan
No conflicting VTP3 devices found.
Do you want to continue? [confirm]

core-switch#show vtp status
VTP Version capable             : 1 to 3
VTP version running             : 3
VTP Domain Name                 : core
VTP Pruning Mode                : Disabled (Operationally Disabled)
VTP Traps Generation            : Disabled
Device ID                       : bcd2.95be.d3c0

Feature VLAN:
--------------
VTP Operating Mode                : Primary Server
Number of existing VLANs          : 42
Number of existing extended VLANs : 0
Maximum VLANs supported locally   : 4096
Configuration Revision            : 37
Primary ID                        : bcd2.95be.d3c0
Primary Description               : core-switch
```

Note that it can take a few moments after doing 'vtp primary vlan' while it checks to see if there are any conflicting VTP3 devices.

I found the solution for this problem in the Cisco Community forums with the search term 'cisco 9500 says it is vtp primary but cant make vlan changes'
