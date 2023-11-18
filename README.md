# splatbot
Automate drawing detailed plaza posts in Splatoon based on BlueZ, and optimize its efficiency by treating it as a Travelling Salesman Problem (TSP).

## Installation
[BlueZ](http://www.bluez.org/) is a Bluetooth protocol stack included with the official Linux kernel distributions. If you have a Linux machine with a Bluetooth connection, then things become easier:
```bash
$ sudo pip install splatbot
```

If you're using macOS or Windows, an external Bluetooth adapter is needed and please follow the instructions below:
1. Install [VirtualBox](https://www.virtualbox.org/wiki/Downloads).
2. Install [VirtualBox Extension Pack](https://www.virtualbox.org/wiki/Downloads).
3. Install [Vagrant](https://developer.hashicorp.com/vagrant/install).
4. Clone splatbot and create a Vagrantfile:
    ```bash
   $ git clone https://github.com/necusjz/splatbot.git
   $ cd splatbot
   $ ./make_vagrantfile.py
    ```

After that, a Vagrantfile will be generated and the current directory is the location where you run any Vagrant command.

## Usage
Roughly speaking, it can be divided into two phases:
1. Generate macros representing the actual drawing process:
    ```bash
    $ splatbot macro -i <image>
    ```
2. Start drawing and you'll see the current progress:
    ```bash
    $ splatbot start -i <macro>
    ```

Press the sync button on your controller(s) and wait until the screen shows the "Press L+R on the controller." menu.

### Vagrant commands
Create and configure guest machines according to your Vagrantfile:
```bash
$ vagrant up
```

SSH into a running Vagrant machine and give you access to a shell:
```bash
$ vagrant ssh
```

Shut down the running machine Vagrant is managing:
```bash
$ vagrant halt
```

Stop the running machine Vagrant is managing and destroy all resources that were created during the machine creation process:
```bash
$ vagrant destroy
```

## Contributing
We love contributions! Before submitting a Pull Request, it's always good to start with a new issue first.

## License
This repository is licensed under MIT. Full license text is available in [LICENSE](https://github.com/necusjz/splatbot/blob/main/LICENSE).
