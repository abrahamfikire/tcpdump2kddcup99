#! /usr/bin/python3
import subprocess
subprocess.call("chmod 755 csv_converter.sh", shell=True)
subprocess.call("./csv_converter.sh", shell=True)

