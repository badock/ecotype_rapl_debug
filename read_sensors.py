import time

from lib.sensors.cpu import get_power_consumption, get_frequencies


def print_consumption():
    cpu_consumption = get_power_consumption()
    print("cpu_consumption:")
    for k, v in cpu_consumption.items():
        print(" > %s => %f" % (k, v))
    cpu_frequencies = get_frequencies()
    print("frequencies:")
    print(" > current => %f" % (cpu_frequencies.current))
    print(" > min => %f" % (cpu_frequencies.min))
    print(" > max => %f" % (cpu_frequencies.max))


if __name__ == "__main__":

    while True:
        print_consumption()
        time.sleep(1.0)

    sys.exit(0)
