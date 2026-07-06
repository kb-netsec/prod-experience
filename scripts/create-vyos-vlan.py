# This scrpt creates a VyOS config with default policy template

# Query user for VLAN ID 
# Create vlan id variable
query user for network and mask
create network/mask variable

set firewall group network-group NET-4-VLAN838 network '172.20.38.0/24'

