@echo off
set /p DOMAIN="Enter Domain: "
set /p UserPro="Enter Username for this domain: "
start /B Runas /profile /user:%DOMAIN%\%UserPro% "C:\MULTI SCRIPT RUN TOOL\Network search tool.bat"

