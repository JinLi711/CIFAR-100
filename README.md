# CIFAR-100
This repository is a short implication of CNN for the CIFAR-100 dataset. 
I used Keras to predict 100 classes and 20 subclasses.
The model considers multioutput class and subclass.

# Results
Accuracy for class: 14%

Accuracy for superclass: 28%

The results are not good, mainly because the CNN is not deep, and I do not have the hardware to run neural networks for millions of parameters.

# Things Done In The Model
Just in case anyone wants to see an example of how to do the things below:

Batch normalization

Drop out

Seperable Conv

Data Augmentation

Early Stopping

Decreasing Learning Rate

# Things to Improve On
Use pretrained base.

Implement Inception V3 module.

Try skip connect.
