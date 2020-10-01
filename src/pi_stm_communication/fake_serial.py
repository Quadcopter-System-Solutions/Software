"""
 fake_serial.py
 http://www.science.smith.edu/dftwiki/index.php/PySerial_Simulator
 A very crude simulator for PySerial assuming it is emulating an Arduino.
"""

class Serial:
    """ a Serial class emulator """


    def __init__( self, port='COM1', baudrate = 19200, timeout=1,
                  bytesize = 8, parity = 'N', stopbits = 1, xonxoff=0,
                  rtscts = 0):
        self.name    = port
        self.port    = port
        self.timeout  = timeout
        self.parity   = parity
        self.baudrate = baudrate
        self.bytesize = bytesize
        self.stopbits = stopbits
        self.xonxoff  = xonxoff
        self.rtscts   = rtscts
        self._is_open  = True
        self._received_data = ""
        self._data = "It was the best of times.\nIt was the worst of times.\n"

    def is_open( self ):
        """ returns True if the port to the Arduino is open.  False otherwise """
        return self._is_open

    def open( self ):
        """ opens the port """
        self._is_open = True

    def close( self ):
        """ closes the port """
        self._is_open = False

    def write( self, string ):
        """ writes a string of characters to the Arduino """
        print( 'Arduino got: "' + string + '"' )
        self._received_data += string

    def read( self, num_char=1 ):
        """ reads num_char characters from the fake Arduino. Actually n characters
            are read from the string _data and returned to the caller.
        """
        string = self._data[0:num_char]
        self._data = self._data[num_char:]
        # print( "read: now self._data = ", self._data )
        return string

    def readline( self ):
        """ reads characters from the fake Arduino until a \n is found. """
        return_index = self._data.index( "\n" )
        if return_index != -1:
            string = self._data[0:return_index+1]
            self._data = self._data[return_index+1:]
            return string
        return ""

    def __str__( self ):
        """ returns a string representation of the serial class """
        return  "Serial<id=0xa81c10, open=%s>( port='%s', baudrate=%d," \
               % ( str(self.is_open), self.port, self.baudrate ) \
               + " bytesize=%d, parity='%s', stopbits=%d, xonxoff=%d, rtscts=%d)"\
               % ( self.bytesize, self.parity, self.stopbits, self.xonxoff,
                   self.rtscts )
