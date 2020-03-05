import sys
import glob
import serial

Serial = serial.Serial
BAUD_RATE = 9600

def list():
    """Lists serial port names
        Raises: EnvironmentError
            On unsupported or unknown platforms
        Returns:
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


def encode(address, word):
    """Encodes address and word according to the standard:
        <address> <word>\n
        Both the address and the word are encoded in a 16-character long string
        representing 8 bytes of data"""
    return "{:0>16X} {:0>16X};".format(address, word).encode()


def send(data, pname, **kwargs):
    """Sends ROM data though the selected serial port.
    Args:
        data (iterable(tuple(address, word))): data to send to the serial port
        port (str): port name
        **kwargs: keyword arguments for port opening
    Returns:
        True if operation was completed successfully, False otherwise
    """
    port = serial.Serial(pname, BAUD_RATE, **kwargs)
    #try:
    #    port.open()
    #except serial.SerialException:
    #    port.close()
    #    print('Could not open port')
    #    return False

    # # Send SOT byte to signal transmission start
    # port.write(chr(2).encode())
    for addr, word in data:
        print(encode(addr, word))
        port.write(encode(addr, word))
    # Send EOT byte to signal transmission end
    #port.write(chr(4).encode())
    port.close()
    return True
