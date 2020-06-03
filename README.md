# Ecotype RAPL DEBUG

## Installation

Run the `misc/prepare.sh` script to install the following dependencies:
- NAS benchmark
- CoreFreq
- Python3 and pip

```
bash misc/prepare.sh
```

## Running the debugging script

```
python3 read_sensors.py
```

## Run corefreq-cli dashboard

```bash
corefreq-cli 
```

## Run the benchmark

```bash
mpiexec -np 40 /root/NPB3.4.1/NPB3.4-MPI/bin/ep.D.x 
```

## Change the CPU frequency

```bash
cpupower frequency-set --min 1700M --max 1799M
```

## Observation

On ecotype, when I set a target frequency >= 1799 MHz, the frequency target is ignored and the CPU works at 2000 MHz:

```shell
root@ecotype-39:~# cpupower frequency-set --min 1700M --max 1799M
```

results in:
```shell
cpu_consumption:
 > dram => 3.569553
 > package-1 => 52.251548
 > package-0 => 52.594254
frequencies:
 > current => 1999.951000
 > min => 1700.000000
 > max => 1799.000000
```

While

```shell
root@ecotype-39:~# cpupower frequency-set --min 1700M --max 1798M
```

results in:
```shell
cpu_consumption:
 > dram => 3.871070
 > package-1 => 46.257631
 > package-0 => 46.514573
frequencies:
 > current => 1799.939500
 > min => 1700.000000
 > max => 1798.000000
```

## Acknowledgements

The code present in this repository is greatly inspired by:
- [https://metebalci.com/blog/a-minimum-complete-tutorial-of-cpu-power-management-c-states-and-p-states/](https://metebalci.com/blog/a-minimum-complete-tutorial-of-cpu-power-management-c-states-and-p-states/)
- [https://github.com/amanusk/s-tui](https://github.com/amanusk/s-tui)
