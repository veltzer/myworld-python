#!/usr/bin/python3

import os # for walk
import os.path # for join
import hashlib # for md5
import logging # for basicConfig, getLogger
import functools # for partial

logging.basicConfig()
logger=logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def md5sum(filename):
    with open(filename, mode='rb') as f:
        d = hashlib.md5()
        for buf in iter(functools.partial(f.read, 128), b''):
            d.update(buf)
    return d.hexdigest()

def main():
    exist_hash={}
    hashmap={}
    folder='.'

    for path, dirs, filenames in os.walk(folder):
        for filename in filenames:
                fullname=os.path.join(path, filename)
                h=md5sum(fullname)
                if h in exist_hash:
                    hashmap[h]=[ exist_hash[h], fullname ]
                else:
                    exist_hash[h]=fullname

    for k,v in hashmap.items():
        print(f'hash: {k}')
        for i,f in enumerate(v):
            print(f'{i}) keep {f}')
        print('s) skip')
        print('q) quit')
        inp=input('choice> ')
        if inp.isdigit():
            p=int(inp)
            if p>=0 and p<len(v):
                os.unlink(v[p])
            else:
                print('error in input')
            continue
        if inp=='s':
            print('skip requested')
            continue
        if inp=='q':
            print('quit requested')
            break

if __name__=='__main__':
    main()
