1. request vlan id from user
2. log into vyos primary
3. query hostname and vrrp to ensure expected (primary, 1a) 
4. ? forgot
5. run show config commands to get outputs


show configuration commmands | grep 'set firewall group network-group NET-4-VLANXXX'
show configuration commands | grep VLANXXX-4-IN
show configuration commands | grep VLANXXX-4-OUT
show configuration commands | grep 'set interfaces ethernet eth3 vif XXX'
show configuration commands | grep 'set firewall ipv4 forward filter rule XXX'
show configuration commands | grep 'set firewall ipv4 forward filter rule XXX'
show configuration commands | grep 'set firewall ipv4 input filter rule XXX'
show configuration commands | grep "set service dhcp-relay interface 'eth3.XXX'"
show configuration commands | grep 'set high-availability vrrp group VLANXXX-4'
show configuration commands | grep "set high-availability vrrp sync-group CLUSTER-1 member 'VLANXXX-4'"

6. dump to file
7. request mop commnad list file
8. diff against mop command list
9. show diffs and also alert if there is any missing commands

