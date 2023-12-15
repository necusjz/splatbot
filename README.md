# Splatoon Bot
Automate plotting posts in [Splatoon](https://splatoonwiki.org/wiki/Splatoon) based on BlueZ, and optimize its efficiency via Traveling Salesman Problem (TSP).

The mailbox is a service in the Splatoon hub that allows players to create drawings and share them via social media. The drawings may be viewable by other players and may be displayed as signs or graffiti in the hub and in various stages in multiplayer matches.

![](https://raw.githubusercontent.com/necusjz/p/master/splatbot/mailbox.png)

## Installation
[BlueZ](http://www.bluez.org/) is a Bluetooth protocol stack included with the official Linux kernel distributions. If you have a Linux machine with a Bluetooth connection, then things become easier:
```bash
$ pip install splatbot
```

If you're using macOS or Windows, an external Bluetooth adapter is needed and please follow the instructions below:
1. Install [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
2. Install [VirtualBox Extension Pack](https://www.virtualbox.org/wiki/Downloads)
3. Install [Vagrant](https://developer.hashicorp.com/vagrant/install)
4. Clone splatbot and make a Vagrantfile:
    ```bash
   $ git clone https://github.com/necusjz/splatbot.git
   $ cd splatbot/vagrant
   $ ./make_vagrantfile.py
    ```

After that, a Vagrantfile will be generated and the current directory is the location where you run any Vagrant command.

## Usage
Generate the macro represents the actual plotting process:
 ```bash
 $ splatbot macro -i <image>
 ```

Wirelessly plotting the post on switch console or another window:
 ```bash
 $ splatbot start -i <macro> [--dry-run]
 ```

Some Vagrant commands that might be useful:
```text
Create and configure guest machines according to your Vagrantfile:
$ vagrant up

SSH into a running Vagrant machine and give you access to a shell:
$ vagrant ssh

Shut down the running machine Vagrant is managing:
$ vagrant halt

Stop the running machine Vagrant is managing and destroy all resources that were created during the machine creation process:
$ vagrant destroy
```

## Benchmark
We provide a dataset collected from [ikasumi.art](https://ikasumi.art/) to easier achieve performance test on your pathing algorithm:

![](https://raw.githubusercontent.com/necusjz/p/master/splatbot/dataset.png)

The results will be shown in the pipeline (via _pytest -s -v --color=yes tests/_):
```text
+------------------+-----------+------------+--------------+
| Benchmark        | Current   | Previous   | Result       |
+==================+===========+============+==============+
| jellyfish.png    | 108606    | 44514      | 2.44x slower |
+------------------+-----------+------------+--------------+
| judd.png         | 100660    | 52616      | 1.91x slower |
+------------------+-----------+------------+--------------+
| kanji.png        | 97159     | 55961      | 1.74x slower |
+------------------+-----------+------------+--------------+
| marie.png        | 100218    | 53238      | 1.88x slower |
+------------------+-----------+------------+--------------+
| octoling.png     | 98888     | 54232      | 1.82x slower |
+------------------+-----------+------------+--------------+
| sakura.png       | 87194     | 66214      | 1.32x slower |
+------------------+-----------+------------+--------------+
| skyline.png      | 89671     | 63751      | 1.41x slower |
+------------------+-----------+------------+--------------+
| splattershot.png | 100344    | 52910      | 1.90x slower |
+------------------+-----------+------------+--------------+
```

## Contributing
We love contributions! Before submitting a Pull Request, it's always good to start with a new issue first.

## License
This repository is licensed under MIT. Full license text is available in [LICENSE](https://github.com/necusjz/splatbot/blob/main/LICENSE).
