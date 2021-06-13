from histogramEqualization import histogramEqualization
from getHistogram import getHistogram
import cv2 as cv

#inimg=cv2.imread('images\cameraman.jpg',0)


getHistogram('images\cameraman.jpg',128)


histogramEqualization('images\cameraman.jpg',256)