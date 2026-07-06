1. request vlan id from user
2. log into vyos primary
3. query hostname and vrrp to ensure expected (primary, 1a) 
4. ? forgot
5. run show config commands to get outputs


show configuration commmands | grep 'set firewall group network-group NET-4-VLANXXX'
show configuration commands | grep VLANXXX-4-IN
show configuration commands | grep VLANXXX-4-OUT


6. dump to file
7. request mop commnad list file
8. diff against mop command list
9. show diffs and also alert if there is any missing commands

