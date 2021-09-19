import os,sys

ssdbackup_path="C:\\Users\\cxd\\Desktop\\SSD Backup\\DesktopHDD\\TXT_ODT"
desktop_path="C:\\Users\\cxd\\Desktop\\TXT_ODT"
ssdbackup_list=os.listdir(ssdbackup_path)
desktop_list=os.listdir(desktop_path)
ssd_unique = [ssditem for ssditem in ssdbackup_list if ssditem not in desktop_list]
desktop_unique = [desktopitem for desktopitem in desktop_list if desktopitem not in ssdbackup_list]
print(ssd_unique)
print(desktop_unique)
both_unique = ssd_unique + desktop_unique
print(both_unique)
