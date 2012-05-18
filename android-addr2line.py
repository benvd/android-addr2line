#!/usr/bin/python                                                                                                                                                                                                                                                                
import sys
import re
import subprocess

ADDR2LINE_BINARY='' # full path to arm-linux-androideabi-addr2line
LIBRARY='' # full path to your .so file

def main():
    print 'Paste the stack trace. CTRL-D to submit. CTRL-C to exit.'

    lines = []
    while True:
        try:
            line = raw_input()
        except KeyboardInterrupt:
            sys.exit()
        except EOFError:
            break
        lines.append(line)

    print ''

    for line in lines:
        address = get_address(line)
        if address is not None:
            source = get_source_line(address)
            if source is not None:
                print '%s %s (%s)' % (address, source[1], source[0])

def get_address(line):
    search = re.search('#[0-9]{2} +pc +([0-9A-Fa-f]{8}) +/data', line)
    if search is None:
        return None
    else:
        return search.groups(1)[0]

def get_source_line(address):
    output = subprocess.check_output([ADDR2LINE_BINARY, '-C', '-f', '-e', LIBRARY, address]).split('\n')
    return (output[0], output[1])

if __name__ == '__main__':
    main()
