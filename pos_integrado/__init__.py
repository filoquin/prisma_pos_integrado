import serial
import serial.tools.list_ports

import binascii
import curses.ascii
import logging
from . import plot_data
plots = plot_data.plots 
#from plot_data import plots
logging.basicConfig(level=logging.DEBUG)



class posIntegrado(object):
    ascii_names = curses.ascii.controlnames
    # ascii.controlnames
    STX = "\x02"
    ETX = "\x03"
    NUL = "\x00"
    ACK = "\x06"

    TES = "\x02\x54\x45\x53\x00\x00\x03\x41"
    TAR = "\x02\x54\x41\x52\x04\x00\x30\x30\x30\x30\x03\x40"
    OKIDOKI = "\x06"

    ser_connection = False
    ser_port = 'COM5'
    ser_speed = 19200

    def ensure_connect(self):
        if not self.ser_connection or not self.ser_connection.isOpen():
            self.connect()

    def connect(self):
        self.ser_connection = serial.Serial(
            self.ser_port, self.ser_speed)#, timeout=1 
        return self.ser_connection.isOpen()

    def close(self):
        if self.ser_connection:
            self.ser_connection.close()
            return self.ser_connection.isOpen()
        return False

    def auto_select_port(self,usb_id='1234:0101'):
        ports = self.list_ports()
        result = list(filter(lambda x: usb_id in x[2] , ports))
        if len(result):
            self.set_port(result[0][0])
            return True
        return False

    def list_ports(self):
        res = []
        ports = serial.tools.list_ports.comports()
        for port, desc, hwid in sorted(ports):
            res.append((port, desc, hwid))
        return res 

    def set_port(self, port):
        logging.info('Port is set to %s' % port)
        self.set_port = port

    def set_speed(self, speed):
        self.set_speed = speed

    def generate_lrc(self, real_msg_with_etx):
        lrc = 0
        for char in real_msg_with_etx:
            lrc ^= ord(char)
        return lrc

    def send_one_byte_signal(self, signal):
        ascii_names = curses.ascii.controlnames
        assert signal in ascii_names, 'Wrong signal'
        char = ascii_names.index(signal)
        self.serial_write(chr(char))
        logging.info('Signal %s sent to terminal' % signal)

    def get_one_byte_answer(self, expected_signal):
        assert isinstance(
            expected_signal, str), 'expected_signal must be a string'
        ascii_names = curses.ascii.controlnames
        one_byte_read = self.serial_read(1)
        expected_char = ascii_names.index(expected_signal)
        if one_byte_read == chr(expected_char):
            return True
        else:
            return False

    def serial_write(self, text):
        assert isinstance(text, str), 'text must be a string'
        raw = text.encode()
        logging.info("%s raw send to terminal" % raw)
        logging.info("%s send to terminal" % text)
        self.ser_connection.write(raw)

    def serial_read(self, size=1):
        raw = self.ser_connection.read(size)
        msg = raw.decode('ascii')
        logging.info("%s raw received from terminal" % raw)
        logging.info("%s received from terminal" % msg)
        return msg

    def makeComand(self, command, params=''):

        if not len(params):
            params = self.NUL + self.NUL
        else :
            params = chr(len(params)) + self.NUL + params
            #params = '\x68\x00' + params

        cmd = (command + params) + self.ETX
        lrc = self.generate_lrc(cmd)
        return self.STX + cmd + chr(lrc)

    def render_args(self, matrix, args):
        arg_string = ''
        for arg in matrix:
            arg_string += arg[2].format(args[arg[0]])
        return arg_string

    def pos_execute(self, cmd_name, **args):
        self.ensure_connect()
        if len(plots[cmd_name]['cmd_args']):
            args = self.render_args(plots[cmd_name]['cmd_args'], args)
        else:
            args = ''

        cmd = self.makeComand(
            cmd_name, args)
        self.serial_write(cmd)
        line = self.ser_connection.read_until(b'\x03')
        # print ("-> %r" % line)
        self.send_one_byte_signal('ACK')
        self.ser_connection.read(1)
        if line == b'\x06':
            return line
        return self.rtn_parce_dict(line,plots[cmd_name]['res_start'], plots[cmd_name]['res_matrix'])


    def rtn_parce_dict(self, res, start, matrix):
        #print("-> %r" % res)
        ascii_res = res.decode('ascii')[start:]
        if ascii_res == self.ETX:
            return False
        res = {}
        for item in matrix:
            # print(item)
            if item[3] == 'N':
                res[item[0]] = int(ascii_res[item[1]:item[1]+item[2]])
            else:
                res[item[0]] = ascii_res[item[1]:item[1]+item[2]].strip()
            #print (res[item[0]])
        return res
