import ctypes
import sys
import subprocess
import config
version=1

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def main():
    print("Kenvix DISM-Based Data Backup Utilities. version", version)
    DISM /Capture-Image /ImageFile:"Code-Root.wim" /CaptureDir:"C:\Work-Station" /Name:"Code-Root" /Description:Kenvix-Code  /ConfigFile:wimscript.ini /Compress:max
    subprocess.call("dism")
    pass

if __name__ == "__main__":
    if is_admin():
        # Code of your program here
        main()
    else:
        # Re-run the program with admin rights
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)