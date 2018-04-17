# GaussMode
Optimizes the fit of a Gaussian laser mode to an intensity image from a beam profiling camera.

Run in text mode by executing "optimize.py" and entering the desired image file in the main function.

Run in a GUI by executing "appGaussMode.py". In this case the image is displayed and the optimization loop executed when a valid filename is entered in the 'Filename' field and the 'Go!' button is pressed. Uses TraitsUI and Chaco.

Three sample images are included: image1.bmp, image2.bmp, and image3.bmp. The beam fit parameters given by a reference Octave program that this was derived from are: [160, 128, 28, 19, 0], [174, 137, 28, 18, 0], and [164, 118, 25, 14, 0], respectively.

This Python implementation gives very close to the same values for these images.
