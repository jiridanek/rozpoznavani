---
title: "Main page"
layout: "default"
isPage: true
---

Our project deals with the recognition of numerical digits in a video file. The video we are using depicts a display of a digital voltmeter, which is measuring the electric potential on an electrode during Belousov--Zhabotinsky reaction.

## BZ reaction

Belousov--Zhabotinsky reaction is an umbrella term for a group of chemical reactions that originate from the original experiment by Belousov. It is the first oscilating chemical reaction that has been discoverd. The most famous version of this reaction is done on a Petri dish and it is notable for the mesmerising colorful patterns that resemble butterfly wings. The possibility of such reaction has been denied by other researches at first.

![Bělousova--Žabotinského reakce](images/Bzr_fotos.jpg)

The measured voltage reflects the temporal change of pH in the reaction vesel. The meaning of the measured value is not important for this task.

## Goals
* Use methods of machine learning and image processing to process a long recording of a display of a voltmeter and output the result in a form that allows further exploration (i.e. a chart).
* The scripts created in this project should be usable to process similar videos made in similar settings, especially in comparable lighting conditions.

## Tools

* Python 2.7
* PIL (Python Imaging Library)
* Weka 3.7