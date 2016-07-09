# ColonyCounter

*samplefilecreator* is used to create the *bg.txt* and *info.data* files used by *opencv_createsamples*.
It is also used to resize the positive images to a mean size or an user defined size, resized image are stored in a new dir called *pos_resized*.

## Usage

```
$ python samplefilecreator.py
usage: samplefilecreator.py [--help] [-p [PATH]] [--jpg] [--png] [--neg]
                            [--pos] [-w [WIDTH]] [-h [HEIGHT]] [-m]

Directory structure:
    /dir
        /neg
            img1.jpg
            img2.jpg
        /pos
            img1.jpg
            img2.jpg

optional arguments:
  --help                show this help message and exit
  -p [PATH], --path [PATH]
                        path to dir to process or current path of script is
                        used
  --jpg                 file output is jpg (default)
  --png                 file output is png
  --neg                 generate bg file for negative images
  --pos                 generate file for positive images (default)
  -w [WIDTH], --width [WIDTH]
                        width of resized images
  -h [HEIGHT], --height [HEIGHT]
                        height of resized images
  -m, --mean            use mean size of old images for resized images
```

#### bg.txt then contains:

```
neg/img1.pg
neg/img2.jpg
```
#### info.data then contains:

```
pos/img1.jpg 1 0 0 25 25
pos/img2.jpg 1 0 0 25 25
```
