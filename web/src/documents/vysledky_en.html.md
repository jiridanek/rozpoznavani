---
title: "Results"
layout: "default"
modified:
---

The best two classification algorithms achieved the accuracy of 99.5 % on the testing dataset.

## Evaluation of the data

To process the data we decited to use the Naive Bayes algorithm for two reasons. First, it is one of the two that gave the best accuracy. Second, it provides not only the classification but also the estimate of probability of the classification being correct. By looking at the histogram of the probabilities we decided to use a treshold of 95 % and drop any frame in which any of the numerals is classified bellow this treshold. In case two or more frames in a row contained the same numeral, we used only the first one and dropped all the subsequent repetitions. The data were exported in the CSV format and plotted using the Microsoft Excel 2007 spreadsheet software.

## Conclusion

We have created a set of scripts in the Python programing language using the PIL library [3], that can be used to analyze recordings similar to the one of a digital display that we used.
If used with different videos, the image processing process may have to be changed, most importantly the treshold values. The classification steps may stay unchanged.

When the values obtained by classifying the whole video are plotted, the resulting chart looks like other measurements described in literature [1].

### Our chart

![Obrázek po segmentaci](images/protokol.png)

### Chart obtained from literature

![Obrázek po segmentaci](images/skripta.png)

## Thanks

We want to thank to Pavel Karas, a doctoral student at FI, who gave us advice about image processing methods in the early stage of this project.

## Literature

-   [1] SOPOUŠEK Jiří a Jiří Křivohlávek, Titulní strana předmětu C4680 Fyzikální chemie - laboratorní cvičení (interaktivní osnova), 2011

-   [2] SOILLE, Pierre. Morphological image analysis: principles and applications. 2nd ed., corr. 2nd print. Berlin: Springer, c2004, xvi, 391 s. ISBN 3540429883.

-   [3] Python Imaging Library Handbook. Dostupné online: http://effbot.org/imagingbook/pil-index.htm