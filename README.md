# ColonyCounter

*samplefilecreator* is used to create the *bg.txt* and *info.data* files used by *opencv_createsamples*.
It is also used to resize the positive images to a mean size or an user defined size, resized image are stored in a new dir called *pos_resized*.
For creating samples it depends on [mergevec](https://github.com/thacoon/mergevec). Just download it and extract it to the CascadeImgScript folder.

Currently the script assumes the dir structure you see below.

## General Usage

```
$ # The script is written for Python 3
$ python samplefilecreator/samplefilecreator.py --help
usage: samplefilecreator.py [--help] [-p [PATH]] [--jpg] [--png] [--neg]
                            [--pos] [-r] [-w [WIDTH]] [-h [HEIGHT]] [-m] [-v]
                            [--num [NUM]] [-mx [MAXXANGLE]] [-my [MAXYANGLE]]
                            [-mz [MAXZANGLE]]

Directory structure:
    /dir
        /neg
            img1.jpg
            img2.jpg
        /pos
            img1.jpg
            img2.jpg
        /vec
            1.vec
            2.vec
        bg.txt
        info.dat
        out.vec

optional arguments:
  --help                show this help message and exit
  -p [PATH], --path [PATH]
                        path to dir to process or current path of script is
                        used
  --jpg                 file output is jpg (default)
  --png                 file output is png
  --neg                 generate bg file for negative images
  --pos                 generate file for positive images (default)
  -r, --resize          resize the image to a mean value on default or to a
                        specific width and height
  -w [WIDTH], --width [WIDTH]
                        width of resized images
  -h [HEIGHT], --height [HEIGHT]
                        height of resized images
  -m, --mean            use mean size of old images for resized images
                        (default)
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
```bash
# Assuming you're in the same folder as the README.md file
# Generate the info.dat file in the same dir
$ python samplefilecreator/samplefilcreator.py

# Generate the info.dat file in a specific dir
$ python samplefilecreator/samplefilcreator.py -p PATH_TO_DIR

# Generate the bx.txt file in a specific dir
$ python samplefilecreator/samplefilcreator.py -p PATH_TO_DIR --neg

# On default the dir is scanned for jpg images, set png flag to scan for png
$ python samplefilecreator/samplefilcreator.py -p PATH_TO_DIR --png

# Resize the images to a specific size, they are saved in pos_resized dir
$ python samplefilecreator/samplefilcreator.py -p PATH_TO_DIR -r -w WIDTH -h HEIGHT

# Create samples from all images that were resized to a mean value
# For all images opencv_createsamples is run and then they get merged in one vec file (out.vec) (dependencies: [mergevec](https://github.com/thacoon/mergevec))
$ python samplefilecreator/samplefilcreator.py -p PATH_TO_DIR -r -m --vec

# Run the tests
$ python -m unittest test.test_samplefilecreator

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
