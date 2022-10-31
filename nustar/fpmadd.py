import subprocess


if __name__=="__main__":
    subprocess.call("addascaspec fpm.dat fpmsrc.pha fpmsrc.rsp fpmbkg.pha", shell=True)
    subprocess.call("mv fpmbkg.pha ../../../analysis", shell=True)
    subprocess.call("mv fpmsrc.pha ../../../analysis", shell=True)
    subprocess.call("mv fpmsrc.rsp ../../../analysis", shell=True)

