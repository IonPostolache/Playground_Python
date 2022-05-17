"""Problem 1
Implement a program that will launch a specified process and periodically (with a provided time interval)
collect the following data about it:
CPU usage (percent);
Memory consumption: Working Set and Private Bytes (for Windows systems) or Resident Set Size and
Virtual Memory Size (for Linux systems);
Number of open handles (for Windows systems) or file descriptors (for Linux systems).
Data collection should be performed all the time the process is running. Path to the executable file for
the process and time interval between data collection iterations should be provided by user.
Collected data should be stored on the disk. Format of stored data should support automated parsing
to potentially allow, for example, drawing of charts."""
import psutil
import os

def main():
    # Output current CPU load as a percentage.
    print('System CPU load is {} %'.format(get_cpu_usage_pct()))
    # Output current CPU frequency in MHz.
    print('CPU frequency is {} MHz'.format(get_cpu_frequency()))
    # Output current RAM usage in MB
    print('RAM usage is {} MB'.format(int(get_ram_usage() / 1024 / 1024)))


def get_cpu_usage_pct():
    """
    Obtains the system's average CPU load as measured over a period of 500 milliseconds.
    :returns: System CPU load as a percentage.
    :rtype: float
    """
    return psutil.cpu_percent(interval=0.5)

def get_cpu_frequency():
    """
    Obtains the real-time value of the current CPU frequency.
    :returns: Current CPU frequency in MHz.
    :rtype: int
    """
    return int(psutil.cpu_freq().current)


def get_ram_usage():
    """
    Obtains the absolute number of RAM bytes currently in use by the system.
    :returns: System RAM usage in bytes.
    :rtype: int
    """
    return int(psutil.virtual_memory().total - psutil.virtual_memory().available)


#os.startfile(path[, operation][, arguments][, cwd][, show_cmd])
#os.startfile(r'C:\Developer in QA ENG (update 2021-08-11).docx')
os.startfile('C:\Program Files\Windows NT\Accessories\wordpad.exe')


for proc in psutil.process_iter():
    if proc.name() == 'wordpad.exe':
        print("process name is wordpad")
        try:
            pinfo = proc.as_dict(attrs=['pid'])
            pinfo_val=pinfo['pid']
        except psutil.NoSuchProcess:
            pass
        else:
            print(pinfo)


p = psutil.Process(pinfo_val)
print(p.cpu_percent(interval=1.0))

if __name__ == "__main__":
    main()

