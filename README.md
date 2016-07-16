# ColonyCounter

*samplefilecreator* is used to create the *bg.txt* and *info.data* files used by *opencv_createsamples*.
It is also used to resize the positive images to a mean size or an user defined size, resized image are stored in a new dir called *pos_resized*.
For creating samples it depends on [mergevec](https://github.com/thacoon/mergevec). Just download it and extract it to the CascadeImgScript folder.

Currently the script assumes the dir structure you see below.

## General Usage

```
$ python samplefilecreator.py
usage: samplefilecreator.py [--help] [-p [PATH]] [--jpg] [--png] [--neg]
                            [--pos] [-w [WIDTH]] [-h [HEIGHT]] [-m] [-v]
                            [--num [NUM]] [-mx [MAXXANGLE]] [-my [MAXYANGLE]]
                            [-mz [MAXZANGLE]]folder

Directory structure:
    /dir
        /neg
            img1.jpg
            img2.jpg
        /pos
            img1.jpg
            img2.jpg
        /vec_files
            1.vec
            2.vec
            out.vec
        bg.txt
        info.dat

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
  -v, --vec             create a vec file of all pos images with using all neg
                        images, mergevec.py needed
  --num [NUM]           number_of_samples, 100 is default
  -mx [MAXXANGLE], --maxxangle [MAXXANGLE]
                        max_x_rotation_angle, default is 1.0
  -my [MAXYANGLE], --maxyangle [MAXYANGLE]
                        max_y_rotation_angle, default is 1.0
  -mz [MAXZANGLE], --maxzangle [MAXZANGLE]
                        max_z_rotation_angle, default is 0.1

```

## Usage Examples
```
# Generate the info.dat file in the same dir
$ python samplefilcreator.py

# Generate the info.dat file in a specific dir
$ python samplefilcreator.py -p PATH_TO_DIR

# Generate the bx.txt file in a specific dir
$ python samplefilcreator.py -p PATH_TO_DIR --neg

# On default the dir is scanned for jpg images, set png flag to scan for png
$ python samplefilcreator.py -p PATH_TO_DIR --png

# Resize the images to a specific size, they are saved in pos_resized dir
$ python samplefilcreator.py -p PATH_TO_DIR -w WIDTH -h HEIGHT

# Create samples from all images, currently the images need to be in the pos_resized dir
# For all images opencv_createsamples is run and then they get merged in one vec file (dependencies: [mergevec](https://github.com/thacoon/mergevec))
$ python samplefilcreator.py -p PATH_TO_DIR --vec

# For more info take a quick look at General Usage.
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
