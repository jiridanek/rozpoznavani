---
title: "Výsledky"
layout: "default"
modified:
---

Nejlepší dva klasifikační algoritmy dosáhly celkové správnosti 99.5 % na testovacích datech.

## Vyhodnocení dat

Ke zpracování jsme se rozhodli použít algoritmus Naive Bayes, neboť ten je schopen kromě třídy navíc poskytnou i pravděpodobnost, s jakou instance do určené třídy náleží. Analýzou histogramu pravděpodobností jsme manuálně určili práh 95 %. Instance klasifikované pod tímto prahem jsme prohlásili za nespolehlivé a snímky, ve kterých se vyskytla jedna nebo více nespolehlivých instancí nezahrnuli do výsledné datové řady. V případě, že dva nebo více po sobě jdoucích snímků obsahovaly to stejné číslo, do datové řady jsme zahrnuli pouze první z nich. Datovou řadu jsme exportovali do formátu CSV (Comma-separated Values) a vytvořili graf v programu Microsoft Excel 2007.

## Závěr

Vytvořili jsme sadu skriptů v programovacím jazyce Python s použitím knihovny PIL [3], které je možné použít k analýze videosekvencí podobného charakteru, jako jsou klipy displeje měřícího přístroje, které jsme používali pro testování my.

Při použití na jiných datech bude pravděpodobně nutné provést úpravy v procesu předzpracování obrazu, zejména znovu nalézt vhodný práh. Všechny další kroky mohou zůstat nezměněny.

Pokud vyneseme hodnoty získané analýzou našeho videa do grafu, dostaneme názorný obrázek, který dobře odpovídá v literatuře popsanému měření [1].

### Výřez z námi vytvořeného grafu

![Obrázek po segmentaci](images/protokol.png)

### Graf z literatury

![Obrázek po segmentaci](images/skripta.png)

## Poděkování

Chtěli bychom poděkovat doktorskému studentu FI Pavlu Karasovi za radu ohledně metod zpracování obrazu, které nám poskytl na začátku řešení projektu.

## Použitá literatura

* [1] SOPOUŠEK Jiří a Jiří Křivohlávek, Titulní strana předmětu C4680 Fyzikální chemie - laboratorní cvičení (interaktivní osnova), 2011
* [2] SOILLE, Pierre. Morphological image analysis: principles and applications. 2nd ed., corr. 2nd print. Berlin: Springer, c2004, xvi, 391 s. ISBN 3540429883.
* [3] Python Imaging Library Handbook. Dostupné online: http://effbot.org/imagingbook/pil-index.htm