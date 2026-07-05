While building a new VLAN on the campus firewall HA pair, I had a copy/paste error and overwrote yhe VLAM ID. Thankfully I caught this before committing and discarded, however im interested to learn if this change would have triggered an HA failover (I believe it would) 

I began configuration on the standby unit with the following:

```
set high-availability vrrp group VLAN838-4 address 172.20.38.1/24
set high-availability vrrp group VLAN838-4 advertise-interval '1'
set high-availability vrrp group VLAN838-4 interface 'eth3.838'
set high-availability vrrp group VLAN838-4 preempt-delay '300'
set high-availability vrrp group VLAN838-4 priority '100'
set high-availability vrrp group VLAN838-4 vrid '100'
set high-availability vrrp sync-group CLUSTER-1 member 'VLAN838-4'
```
