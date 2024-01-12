#!/usr/bin/python3
for alpha_code in range(ord('a'), ord('z') +1):
    if chr(alpha_code) not in ('q', 'e'):
        print('{:c}'.format(alpha_code), end='')
