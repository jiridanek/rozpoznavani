Požadavky Python 2.7
PIL, python-imaging library
yum install python-imaging
yum install ImageMagick
sudo ln -s /usr/bin/display /usr/local/bin/xv

architektura

získání obrázků

ve složce s daty je příkaz pro ffmpeg, je možné hrát si se snímkovou frekvencí (10 vs 15, např.)

učící data

mkdir kratsi_sample
python -i sample_files.py
>>> sample_files("data/kratsi", "kratsi_sample", 500)

všechna data

arff naučení
náhodný výběr ze všech čísel 

mkdir kratsi_learning
python -i prepare_learning_set.py
>>> prepare_learning_set("kratsi_sample", "kratsi_learning")

0 88
1 1000
2 260
3 35
4 55
5 60
6 48
7 215
8 169
9 70

arff rozpoznání

vpodstatě stejně

dělení snímku, anotování: vytvoření arff složky 0,1,2 atd

feature construction

w/h
bílých pixelů
škálovat, matice pixelů
první bílý podél okraje

hodnocení výsledku


potom arff bez tříd, zpracovat výsledek

saving the model,loading it, -d, -l flags
http://weka.wikispaces.com/Saving+and+loading+models
http://weka.wikispaces.com/Why+do+I+get+the+error+message+'training+and+test+set+are+not+compatible'%3F

//awk '/^[^@].*,/{print $0 ",0"; next} //'

http://weka.wikispaces.com/Making+predictions

46392        1:0        6:5   +   1 
perl -ne'/^(\d+).*\d:(\d).*\d:(\d)/ && print $1'

java -classpath weka.jar weka.classifiers.bayes.NaiveBayes -l /samsung/jirka/code/rozpoznavani/bayes.model -T /samsung/jirka/code/rozpoznavani/naostro2.arff -p 0 > vysledek.txt

vytvoření modelu

java weka.classifiers.bayes.NaiveBayes -d /samsung/jirka/code/rozpoznavani/bayes.model -t /samsung/jirka/code/rozpoznavani/test.arff

vytvoření ostrých dat je stejné jako učících dat v kroku

mkdir kratsi_klasifikace
python -i prepare_learning_set.py
>>> prepare_learning_set('data/kratsi', 'kratsi_klasifikace')