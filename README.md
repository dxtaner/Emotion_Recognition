Emotion Recognition
===================

This project provides an Emotion Recognition system that identifies emotions based on the user's facial expressions.

Getting Started
---------------

These instructions will guide you to run or test the project on your local machine.

### Requirements

To run this project, you will need the following software and tools:

*   Python 3.x
*   OpenCV (Computer Vision Library)
*   Tensorflow (Machine Learning Library)

### Installation

1.  Clone this repository:

    git clone https://github.com/dxtaner/emotion_recognition.git

3.  Install the required packages:

    pip install opencv-python tensorflow

5.  Run `duygutanima.ipynb`:

Usage
-----

The API only accepts a JSON request and returns a JSON response. The request should include the `image_url` field, containing the URL of the image to be analyzed.

The API can recognize the following emotions:

*   Happy
*   Sad
*   Angry
*   Surprised
*   Fearful
*   Neutral

It returns the emotion with the highest confidence score as the result.

Preprocessing for Training Data
===============================

Number of samples: 28,709

Model Creation for Training Data
--------------------------------

Model used: Convolutional Neural Network (CNN)

### Model Structure

*   Layer 1: Conv2D layer with 64 filters of size 3x3
*   Layer 2: Conv2D layer with 64 filters of size 3x3
*   Layer 3: Conv2D layer with 32 filters of size 3x3
*   Layer 4: Conv2D layer with 32 filters of size 3x3
*   Layer 5: Conv2D layer with 32 filters of size 3x3
*   Fully Connected Layer: Dense layer with 128 neurons
*   Output Layer: Dense layer with 7 neurons

### Model Training

Training time: 25 epochs

Batch size: 100

Preprocessing for Test Data
---------------------------

Number of test samples: 3,589

Model Performance
-----------------

Accuracy: 0.53

Loss: 1.14
