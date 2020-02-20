import sys
import glob
import serial

Serial = serial.Serial


def list():
    """Lists serial port names
        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ["COM{}".format(i + 1) for i in range(16)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result


def send(data, port, **kwargs):
    """Sends ROM data though the selected serial port. Data is formatted as follows"
        <address> <word>\n
    Args:
        data (iterable(tuple(address, word))): data to send to the serial port
        port (str): port name
        **kwargs: keyword arguments for port opening
    Returns:
        True if operation was completed successfully, False otherwise
    """
    port = serial.Serial(port, **kwargs)
    try:
        port.open()
    except serial.SerialException:
        port.close()
        return False

    for addr, word in data:
        port.write("{} {}\n".format(addr, word).encode())
    port.close()
    return True
