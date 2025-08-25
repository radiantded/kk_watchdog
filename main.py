import sys

from config import get_settings
from src.watchdog import Watchdog


instance = sys.argv[1]

watchdog = Watchdog(settings=get_settings())

runmap = {
    "producer": watchdog.produce,
    "consumer": watchdog.consume,
}


if __name__ == "__main__":
    try:
        if instance not in runmap:
            raise ValueError(f"Instance {instance} not in {runmap.keys()}")
        runmap[instance]()
    except KeyboardInterrupt:
        print("Bye")
