# PhotoDOG

Photo Date Order Generator

## Introduction

This command line app is designed to generate and bulk update EXIF 'Shot Taken Date' information for JPGs

## Problem Statement

Sometimes photographic images are missing EXIF date information. 
Cataloging tools (e.g. OneDrive or Google Drive Photos or Windows Photos App) will then usually resort to sorting and cataloging your photos by creation or modification date.
This is usually not useful and confusing, the photos will likely also lose any ordering that they had as the creation/modification dates
for each file will probably be somewhat random.

## Solution

If the files are named in an ascending pattern that reflects the order in which the photos were taken
we can fake or approximate the information by specifying a start date for an image, and a time interval
for a number of subsequent images

## Install Prerequsites

```bash
pip install -r requirements.txt
```

## Usage

```bash
$ ./photodog.py -h
usage: photodog.py [-h] [--input_dir INPUT_DIR] [--output_dir OUTPUT_DIR] [--initial_date INITIAL_DATE] [--interval INTERVAL] [--first FIRST] [--last LAST] [--dryrun]

Photo Date Order Generator - Generate and bulk update ordered EXIF dates for JPGs

optional arguments:
  -h, --help            show this help message and exit
  --input_dir INPUT_DIR
                        Path where the source images reside
  --output_dir OUTPUT_DIR
                        Path to write the updated images
  --initial_date INITIAL_DATE
                        ISO datetime to set the first file to. ie "2022-04-19 13:00"
  --interval INTERVAL   Number of seconds to increase for each subsequent file
  --first FIRST         First filename to start at
  --last LAST           Last filename to stop at
  --dryrun              Only print out the calculated values
```

### Examples

Set the date to `2021-04-19 12:00` for `Image0005` and add 60s for every subsequent image up to `Image0034.jpg`

```bash
./photodog.py --input_dir ~/Pictures/Originals/ --output_dir ~/Pictures/Modified/ --initial_date "2021-04-19 12:00" --interval 60  --first Image0005.jpg --last Image0034.jpg
```

Show the calculated times for 15 images

```bash
$ ./photodog.py --input_dir ~/Pictures/Originals/ --output_dir ~/Pictures/Modified/ --initial_date "2022-04-19 18:30" --interval 72 --first Image0516.jpg --last Image0530.jpg --dryrun
Dryrun - would set the following:
---------------------------------
Image0516.jpg - 2022-04-19 18:30:00
Image0517.jpg - 2022-04-19 18:31:12
Image0518.jpg - 2022-04-19 18:32:24
Image0519.jpg - 2022-04-19 18:33:36
Image0520.jpg - 2022-04-19 18:34:48
Image0521.jpg - 2022-04-19 18:36:00
Image0522.jpg - 2022-04-19 18:37:12
Image0523.jpg - 2022-04-19 18:38:24
Image0524.jpg - 2022-04-19 18:39:36
Image0525.jpg - 2022-04-19 18:40:48
Image0526.jpg - 2022-04-19 18:42:00
Image0527.jpg - 2022-04-19 18:43:12
Image0528.jpg - 2022-04-19 18:44:24
Image0529.jpg - 2022-04-19 18:45:36
Image0530.jpg - 2022-04-19 18:46:48
```

