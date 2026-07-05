While building a new VLAN on the campus firewall HA pair, I had a copy/paste error and overwrote yhe VLAM ID. Thankfully I caught this before committing and discarded, however im interested to learn if this change would have triggered an HA failover (I believe it would) 

I began configuration on the standby unit with the following:

```
set high-availability vrrp group VLAN123 address 192.168.1.1/24
set high-availability vrrp group VLAN123 advertise-interval '1'
set high-availability vrrp group VLAN123 interface 'eth3.124'
set high-availability vrrp group VLAN123 preempt-delay '300'
set high-availability vrrp group VLAN123 priority '100'
set high-availability vrrp group VLAN123 vrid '100'
set high-availability vrrp sync-group CLUSTER-1 member 'VLAN123'
```

I'm not configuring VLAN 123 here. The group contained a copy paste error and I was actually configuring VLAN 124. VLAN 124 exists on this firewall, so I was about to overwrite VLAN 123 HA address and interface configurations.
