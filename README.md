# Athlete Fitness Classifier

## Introduction
The Athlete Fitness Classifier is a program that outputs a binary value that predicts whether an athlete is considered fit or not, based on 11 different health criteria such as weight, height, and body fat percentage. This program was written using Python and the Numpy and Pandas libraries.

## How it works
To predict the fitness of an athlete, this classifier was trained on a training dataset of over 10,000 athletes each containing 11 different numerical health descriptors. From this training data, the classifier then creates conditional probabilities for each criterion, each representing the probability of an athlete being considered fit given their score for each specific criterion. By using the naïve Baye's algorithm, we can then combine every conditional probability to give a singular prediction of fitness for each athlete
