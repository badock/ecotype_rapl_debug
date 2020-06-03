import glob
import os
import logging
import time
import psutil

from src.helper_functions import cat

MICRO_JOULE_IN_JOULE = 1000000.0


def read_cpu_power_consumption():
    reading = {}

    basenames = glob.glob('/sys/class/powercap/intel-rapl:*/')
    basenames = sorted(set({x for x in basenames}))

    pjoin = os.path.join

    for path in basenames:
        name = None
        try:
            name = cat(pjoin(path, 'name'), fallback=None, binary=False)
        except (IOError, OSError, ValueError) as err:
            logging.warning("ignoring %r for file %r",
                            (err, path), RuntimeWarning)
            continue
        if name:
            try:
                energy_file_path = pjoin(path, 'energy_uj')
                energy_joule = float(cat(energy_file_path)) / MICRO_JOULE_IN_JOULE

                reading[name] = {
                    "timestamp": time.time(),
                    "value": energy_joule
                }

            except (IOError, OSError, ValueError) as err:
                logging.warning("ignoring %r for file %r",
                                (err, path), RuntimeWarning)
    return reading


def get_power_consumption():
    reading1 = read_cpu_power_consumption()
    time.sleep(1.0)
    reading2 = read_cpu_power_consumption()

    reading = {}

    for k, d1 in reading1.items():
        if k not in reading2:
            raise Exception("key" + k + " is not present in reading2")
        d2 = reading2.get(k)

        v = (d2.get("value") - d1.get("value")) / (d2.get("timestamp") - d1.get("timestamp"))
        reading[k] = v

    return reading


def get_frequencies():
    frequencies = psutil.cpu_freq()
    return frequencies
