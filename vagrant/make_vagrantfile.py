#!/usr/bin/env python
import re
import subprocess
from shutil import which


def retrieve_info(identifier, text):
    pattern = re.compile(fr"(?<={re.escape(identifier)}:).*.")
    matches = pattern.findall(text)

    return matches[0].strip() if matches else ""


def get_usb_devices():
    usb_devices = subprocess.check_output(["VBoxManage", "list", "usbhost"])
    usb_devices = usb_devices.decode("utf-8").replace("\r", "")
    usb_devices = usb_devices.split("\n\n")

    devices = []
    for device in usb_devices:
        vid = retrieve_info("VendorId", device)
        pid = retrieve_info("ProductId", device)
        manufacturer = retrieve_info("Manufacturer", device)
        product = retrieve_info("Product", device)

        if len(pid) == 13 and len(vid) == 13 and product and manufacturer:
            devices.append({
                "vid": vid[8:12],
                "pid": pid[8:12],
                "manufacturer": manufacturer,
                "product": product
            })

    return devices


def check_env(name, cmd, msg=None):
    print(name, end="")
    if which(cmd) is not None:
        print(" [OK]")
    else:
        print(" [ERROR]")
        print(f"  -> {name} wasn't found on your system.")
        if msg is not None:
            print(msg)

        exit(1)


if __name__ == "__main__":
    print("Checking for the required utilities...")
    vg_msg = ("    Please ensure that Vagrant is installed and available on\n"
              "    your system path.")
    check_env("Vagrant", "vagrant", msg=vg_msg)
    vb_msg = ("    VBoxManage (part of the VirtualBox CLI) wasn't found\n"
              "    on your system path. Please ensure that VirtualBox is\n"
              "    installed and VBoxManage is on your system path.")
    check_env("VirtualBox", "VBoxManage", msg=vb_msg)
    print("")

    print("---")
    print("Welcome to `splatbot` setup wizard.")
    print("As part of the first step in this process, you will select the USB Bluetooth adapter that will be used.")
    print("Please ensure that your adapter is plugged into this computer.")
    print("")

    input("Press <enter> key to continue.")
    print("")

    print("USB Devices:")
    print("---")
    devices = get_usb_devices()
    for idx, device in enumerate(devices):
        print(f"{idx:3}. {device['product']} ({device['manufacturer']})")
    print("")

    is_valid = False
    while not is_valid:
        choice = input(f"Please choose your Bluetooth adapter from the above list. [0-{len(devices)-1}] ")
        if choice.isdigit() and int(choice) < len(devices):
            is_valid = True
        else:
            print(f"Invalid choice. Please choose a number from 0 to {len(devices)-1}.")
    adapter_info = devices[int(choice)]
    print("")

    is_valid = False
    while not is_valid:
        choice = input("Would you like to install `splatbot` from <0> PyPI or <1> local project? [0-1] ")
        if choice in {"0", "1"}:
            is_valid = True
        else:
            print("Invalid choice. Please choose a number from 0 or 1.")
    print("")

    print("Configuring...")
    with open("Basefile", "r", encoding="utf-8") as fp:
        vagrantfile = fp.read()
    usb_filter = f"""vb.customize ["usbfilter", "add", "0",
        "--target", :id,
        "--name", "{adapter_info['product']} ({adapter_info['manufacturer']})",
        "--vendorid", "{adapter_info['vid']}",
        "--productid", "{adapter_info['pid']}",
        "--manufacturer", "{adapter_info['manufacturer']}",
        "--product", "{adapter_info['product']}"
    ]"""
    vagrantfile = vagrantfile.replace("{{USB_FILTER}}", usb_filter)
    if choice == "0":
        vagrantfile = vagrantfile.replace("{{SHELL_CONFIG}}", "pip install splatbot")
    else:
        vagrantfile = vagrantfile.replace("{{SHELL_CONFIG}}", "cd /splatbot && pip install -e .")
    with open("Vagrantfile", "w", encoding="utf-8") as fp:
        fp.write(vagrantfile)
    print("Done!")
    print("")

    print("You can now create `splatbot` guest machine with `vagrant up`.")
    print("After booting up, the Vagrant machine can be access with `vagrant ssh`.")
