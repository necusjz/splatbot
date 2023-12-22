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

Several Vagrant commands that might be useful:
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

## Pathing
We optimize pathing efficiency by treating the plotting process as a variant of [Traveling Salesman Problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem) (TSP). It's a classic optimization problem where the goal is to find the shortest possible route that visits a given set of cities and returns to the original city.

If you want to solve it without returning to the start, it essentially becomes the problem of finding a [Hamiltonian Path](https://en.wikipedia.org/wiki/Hamiltonian_path), which visits each city exactly once. To further scale down, we divide the image into 8x3 parts (with _patch size of 40_) and label the contiguous region as a city.

## Benchmark
We provide a dataset collected from [ikasumi.art](https://ikasumi.art/) to easier achieve performance test on your pathing algorithm:

![](https://raw.githubusercontent.com/necusjz/p/master/splatbot/dataset.png)

The results will be shown in the pipeline (via _pytest -s -v --color=yes tests/_):
```text
+------------------+-----------+------------+--------------+
| Benchmark        | Current   | Previous   | Result       |
+==================+===========+============+==============+
| jellyfish.png    | 17078     | 44514      | 2.61x faster |
+------------------+-----------+------------+--------------+
| judd.png         | 32728     | 52616      | 1.61x faster |
+------------------+-----------+------------+--------------+
| kanji.png        | 41557     | 55961      | 1.35x faster |
+------------------+-----------+------------+--------------+
| marie.png        | 43280     | 53238      | 1.23x faster |
+------------------+-----------+------------+--------------+
| octoling.png     | 38008     | 54232      | 1.43x faster |
+------------------+-----------+------------+--------------+
| sakura.png       | 63809     | 66214      | 1.04x faster |
+------------------+-----------+------------+--------------+
| skyline.png      | 61949     | 63751      | 1.03x faster |
+------------------+-----------+------------+--------------+
| splattershot.png | 34804     | 52910      | 1.52x faster |
+------------------+-----------+------------+--------------+
| Geometric Mean   | N/A       | N/A        | 1.33x faster |
+------------------+-----------+------------+--------------+
```

## Contributing
We love contributions! Before submitting a Pull Request, it's always good to start with a new issue first.

## License
This repository is licensed under MIT. Full license text is available in [LICENSE](https://github.com/necusjz/splatbot/blob/main/LICENSE).
