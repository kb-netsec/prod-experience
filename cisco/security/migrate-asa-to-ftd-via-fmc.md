This will detail the exercise of migrating a legacy ASA5510 firwall to newer Cisco FTD hardware.

The built in FMT on FMC virtual appliance only supported migrating from other FTD devices, so needed to use desktop FMT. 

Steps taken during migration:

1. Launch FMT
2. Provide FMC IP
3. Select FTD device
4. Verify source and target are firewall modes are the same


To verify ASA mode is the same as the target FTD device mode: 

```
show firewall
```
You can use the CLI on the FTD device as well or the FMC GUI; navigate to Devices > Device Management in the FMC UI, click the pencil icon to edit the device, click the Device tab and check the "Mode" field in the General tile.

5. Selected default features to migrate
6. Started rule conversion
7. Mapped ASA interfaces > FTD interfaces
8. Map ASA Security Zones and Interface Groups > FTD Security Zones and Interface Groups

Now would be a good time to pause and discuss the creation of Security Zones and Interface Groups on the FMC: 

Created global outside, inside, and management routed security zones in FMC Objects > Object Management > Interface > Add > Security Zone
Added global outside, inside, and management routed interface groups in FMC Objects > Object Management > Interface > Add > Interface Group




I started by bulling the ASA config manually and uploading it to the tool after verifying there were no secrets or hashes in the config. 

Next, since I'm targeting an FTD device that's registered to a virtual FMC appliance, I selected the on-prem FMC option and provided the management IP address. 



# Reconfigure VPN Tunnel

The old ASA was using IKEv1 to stand up a tunnel between this ASA and a peer. In addition, the peer was updating their firewall as well, necessitating a rebuild of the VPN tunnel. A policy based peer-to-peer VPN topology was selected in the FMC GUI for simplicity. 

Using the ASA running config to select Endpoint options in the Edit VPN Topology Menu:

Device: <redacted-host>
Interface: outside
IP Address: 
This IP is Private: 
Connection Type: 
Certificate Map: 
Protected Networks: 
Enable NAT Traversal:
Exempt VPN traffic from NAT:
Inside interfaces directly connected to the internal network: 




