#!/usr/bin/env python3

import sys

for line in sys.stdin:
    if line.startswith('>'):
        print(line[:-1])
    else:
        mutaline = ''
        count = 0
        for letter in line:
            count += 1
            if count % 11 == 0:
                if letter.lower() == 'g':
                    mutaline += 't'
                else: mutaline += 'g'
            else:
                mutaline += letter
        print(mutaline[:-1])
