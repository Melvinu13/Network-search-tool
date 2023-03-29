@echo off
set /p DOMAIN="Enter Domain: "
set /p UserPro="Enter Username for this domain: "
set /p list="Enter the PC name: "
for  %%x in (%list%) do (
	ping %%x
	winrs -r:%%x "C:\Program Files (x86)\Lenovo\System Update\tvsu.exe"
	start /B Runas /profile /user:%DOMAIN%\%UserPro% "C:\Program Files (x86)\Lenovo\System Update\tvsu.exe"
)

PAUSE
