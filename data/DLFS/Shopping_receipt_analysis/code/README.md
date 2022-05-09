# Code Readme

Here are a few things we tried to predict the total sum of a shopping receipt.

We also tried a Mask-RCNN, but this 1) did not work and 2) was way to big to be included in this code sample

Included are:

## SimplestOfNetworks

We tried to derive the position of the sum on the shopping receipt with just a simple convolutional network. As can be seen in the output cells, this did not work too well

## DirectDerival

We then tried to directly obtain a floating-point-value representing the sum on the shopping receipt with a slightly more complex network.

Sadly, it only learnt to overfit on the data, returning mostly an average of the receipt sums.

## PretrainingRetraining

Since text recognition proved to be hard, we wrote an image generator (`create_images`) which would create several thousand example images of floating point numbers and when that wasn't enough also just single digits.

We then applied another network to it with the idea that it could transfer the skills learnt in one step to the next, more complex one.

This failed since the performance with single digits never reached an acceptable level.