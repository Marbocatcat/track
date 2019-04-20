#!/bin/env python3

from track import Track
import argparse
import os

sample_tracking = 92612999965481511051325324


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('tracking')
    args = parser.parse_args()

    package = Track(args.tracking)
    os.system('clear')
    package.track_factory()


if __name__ == '__main__':
    main()
