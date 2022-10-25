import subprocess


def main():
    subprocess.call("addascaspec fpm.dat fpmsrc.pha fpmsrc.rsp fpmbkg.pha", shell=True)
    subprocess.call("mv fpmbkg.pha ../../../analysis", shell=True)
    subprocess.call("mv fpmsrc.pha ../../../analysis", shell=True)
    subprocess.call("mv fpmsrc.rsp ../../../analysis", shell=True)


if __name__=="__main__":
    main()