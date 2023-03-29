@echo off
set /p PCNAME="Enter Hostname: "
for %%x in (%PCNAME%) do (
	manage-bde -protectors C: -ComputerName %%x -get
)
Pause 10


