@echo off
set /p IpOrPcname= "Enter the IP address or the Hostname: "
ping -a %IpOrPcname%
Pause 5
tracert %IpOrPcname%
Pause 5
winrs -r:%IpOrPcname% arp -a
Pause 5
GETMAC /s %IpOrPcname%
Pause 5
ECHO "USE THIS COMMAND TO GET THE DEVICES BIT LOCKER INFORMATION "manage-bde -protectors C: -get""
ECHO "USE THIS COMMAND TO GET THE ARP TABLE""
winrs -r:%IpOrPcname% cmd.exe
Pause 20



