@echo off
netsh interface ipv4 set address name="�C�[�T�l�b�g" ^
source=static^
 address=192.168.100.2^
 mask=255.255.255.0^
 gateway=192.168.100.1
pause

netsh interface ipv4 set dns name="�C�[�T�l�b�g" ^
source=static ^
address=192.168.100.1 ^
register=primary validate=no^

netsh interface ipv4 add dns name="�C�[�T�l�b�g" ^
    kg3address=xxx.xxx.xxx.xxx index=2 validate=no^
pause