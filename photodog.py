#!/usr/bin/env python3
import argparse
import datetime
import os
import sys
from exif import Image, DATETIME_STR_FORMAT


def get_images(path, first, last):
    """Find all images alphabetically between the first and last (inclusive)"""
    files = os.listdir(path)
    files.sort()
    selected = []
    index = files.index(first)
    for i in range(index, len(files)):
        selected.append(files[i])
        if files[i] == last:
            break
    return selected


def calculate_dates(images, start, interval):
    """Iterate over found images and increase the time by the interval for each"""
    current = start
    result = {}
    for image in images:
        result[image] = current
        current = current + datetime.timedelta(seconds=interval)
    return result


def dryrun(plan):
    """Print out the found images and calculated times"""
    print('Dryrun - would set the following:')
    print('---------------------------------')
    for image in plan:
        print(f'{image} - {plan[image]}')


def write_dates(plan, input_dir, output_dir):
    """Write the images to the output dir with the updated times"""
    for image in plan:
        with open(os.path.join(input_dir, image), 'rb') as input_file:
            source_image = Image(input_file)
            source_image.datetime_original = plan[image].strftime(DATETIME_STR_FORMAT)

            with open(os.path.join(output_dir, image), 'wb') as output_file:
                output_file.write(source_image.get_file())
                print(f'Writing {output_file.name} - {source_image.datetime_original}')


def main(args):
    images = get_images(args.input_dir, args.first, args.last)
    start_date = datetime.datetime.fromisoformat(args.initial_date)
    plan = calculate_dates(images, start_date, args.interval)

    if args.dryrun:
        dryrun(plan)
        sys.exit()

    write_dates(plan, args.input_dir, args.output_dir)


if __name__ == '__main__':
    ap = argparse.ArgumentParser(
        description='Photo Date Order Generator - Generate and bulk update ordered EXIF dates for JPGs')
    ap.add_argument('--input_dir', help='Path where the source images reside')
    ap.add_argument('--output_dir', help='Path to write the updated images')
    ap.add_argument('--initial_date', help='ISO datetime to set the first file to. ie "2022-04-19 13:00"')
    ap.add_argument('--interval', type=int, help='Number of seconds to increase for each subsequent file')
    ap.add_argument('--first', help='First filename to start at')
    ap.add_argument('--last', help='Last filename to stop at')
    ap.add_argument('--dryrun', action='store_true', help='Only print out the calculated values')
    args = ap.parse_args()
    main(args)
