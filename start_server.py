import subprocess, sys


def start_server(script_path): 
    p = subprocess.Popen(["pwsh", script_path], stdout=sys.stdout)
    p.communicate()






