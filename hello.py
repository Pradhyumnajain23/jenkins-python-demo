import platform
import sys
import datetime

def system_info():
    print("=== Jenkins Python Build ===")
    print(f"Python Version : {sys.version}")
    print(f"Platform       : {platform.system()} {platform.release()}")
    print(f"Machine        : {platform.machine()}")
    print(f"Build Time     : {datetime.datetime.now()}")
    print("============================")

def simple_calculation():
    print("\nRunning sample calculation...")
    numbers = [10, 20, 30, 40]
    total = sum(numbers)
    print(f"Numbers : {numbers}")
    print(f"Sum     : {total}")

if __name__ == "__main__":
    system_info()
    simple_calculation()