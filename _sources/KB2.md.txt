Pipelined Corner Detection Algorithm (KB2)
==========================================

*Published: February 20, 2026*

*Highlights pipelined and parallel execition, a key FPGA strength.*

*Categories: WhizniumDBE, Whiznium CV Demonstrator*


Model and source code file pointers: in \[1\] \_mdl/IexWdbeFin\_wskd.xlsx, ezdevwskd/UntWskdZuvsp/CtrWskdZuvspCorner.h, fpgawskd/zuvsp/Corner.vhd

Identification of high-contrast patterns such as barcodes is one of the oldest computer vision applications there is. In the context of the Whiznium CV demonstrator, the precise determination of the turntable's position relative of the camera is a task achieved through identifying its printed checkerboard pattern's corners.

The theory of the Harris corner detection algorithm used to this end is well-established \[\] and can be summarized as accomplishing two consecutive tasks:

1\. identification of camera pixels with large spatial differentials towards their neighbors, looking at 5x5 windows around each pixel, then attribution of the so-called Harris score to each pixel (the higher the more pronounced)

2\. selecting the pixels with the maximum -- then logarithmic - Harris score, first in their immediate 5x5 pixel surroundings, then by means of a threshold / cutoff across the entire camera frame

The FPGA implementation of 1. roughly follows \[\] and comes down to pipelining the following formula which notably features summations over two dimensions x, y or row, column.

In manual analysis, first possible parallelism is identified and then matched with the known latencies of -- here -- adder and multiplier the is to be identified and matched with known latencies as well as required register cycles to be inserted.
