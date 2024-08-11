import subprocess


def start_server(script_path): 
    p = subprocess.Popen(["pwsh", script_path], stdout=subprocess.PIPE)





