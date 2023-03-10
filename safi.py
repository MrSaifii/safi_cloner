import os
if os.path.exists('/data/data/com.termux/files/usr/bin/pkg'):
    os.system('chmod 777 64bitsaif')
    os.system('./64bitsaif')
else:
    from script import menu
    menu()
