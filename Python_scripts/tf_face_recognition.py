"""
This script is designed to run on the OpenMV Cam H7 Plus to perform facial emotion detection using a 
pre-trained TensorFlow Lite model. The script performs the following tasks:

1. Initializes the camera and sets it to capture images in QVGA format.
2. Loads a pre-trained TensorFlow Lite model for emotion detection.
3. Captures images and detects faces within the images.
4. Classifies the emotions of the detected faces.
5. Draws rectangles around detected faces and labels them with the detected emotion.
6. Prints the detected emotions to the terminal.

Key functionalities:
- Image capture and processing.
- Face detection using Haar cascades.
- Emotion classification using a TensorFlow Lite model.
- Visual feedback on the captured images with bounding boxes and labels.
"""

import sensor, image, time, tf

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)

clock = time.clock()

net = tf.load("trained.tflite", load_to_fb=True)
labels = [l.rstrip('\n') for l in open("labels.txt")]

while(True):
    clock.tick()

    # Take a picture and brighten things up for the frontal face detector
    img = sensor.snapshot().gamma_corr(contrast=1.5)

    # Returns a list of rects (x, y, w, h) where faces are
    faces = img.find_features(image.HaarCascade("frontalface"))

    for f in faces:

        # Classify a face and get the class scores list
        scores = net.classify(img, roi=f)[0].output()

        # Find the highest class score and lookup the label for that
        label = labels[scores.index(max(scores))]

        # Draw a box around the face
        img.draw_rectangle(f)

        # Draw the label above the face
        img.draw_string(f[0]+3, f[1]-1, label, mono_space=False)

        # Print the detected emotion to the terminal
        print("Detected emotion: ", label)

    print(clock.fps())
