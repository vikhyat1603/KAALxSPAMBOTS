
import glob
from pathlib import Path
from KaalX.utils import load_plugins
import logging
from . import MK1, MK2, MK3, MK4, MK5, MK6, MK7, MK8, MK9, MK10

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


path = "KaalX/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("\n𝗞𝗮𝗮𝗹𝐗 𝐃𝐄𝐏𝐋𝐎𝐘𝐄𝐃 𝐒𝐔𝐂𝐂𝐄𝐒𝐒𝐅𝐔𝐋𝐋𝐘 😎🤘🏻\nMy Master ---> @raj_singh_rc")

if __name__ == "__main__":
    MK1.run_until_disconnected()
    
if __name__ == "__main__":
    MK2.run_until_disconnected()

if __name__ == "__main__":
    MK3.run_until_disconnected()
    
if __name__ == "__main__":
    MK4.run_until_disconnected()

if __name__ == "__main__":
    MK5.run_until_disconnected()
    
if __name__ == "__main__":
    MK6.run_until_disconnected()
    
if __name__ == "__main__":
    MK7.run_until_disconnected()

if __name__ == "__main__":
    MK8.run_until_disconnected()
    
if __name__ == "__main__":
    MK9.run_until_disconnected()

if __name__ == "__main__":
    MK10.run_until_disconnected()    
