#! /usr/bin/bash
# original script
# opencv_createsamples -img dart.bmp -vec dart.vec  -w 20 -h 20 -num 500 -maxidev 80 -maxxangle 0.8 -maxyangle 0.8 -maxzangle 0.2
# opencv_createsamples -img dart.bmp -vec dart.vec  -w 50 -h 50 -num 1000 -maxidev 80 -maxxangle 1.2 -maxyangle 0.6 -maxzangle 0.2
opencv_createsamples -img dart.bmp -vec dart.vec  -w 20 -h 20 -num 3000 -maxidev 80 -maxxangle 1.1 -maxyangle 0.6 -maxzangle 0.2