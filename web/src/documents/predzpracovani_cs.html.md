---
title: "Předzpracování obrazu"
layout: "default"
modified:
---

## 1. Prahování

Využíváme faktu, že pixely příslušející číslicím na displeji voltmetru jsou dobře odlišitelné od pozadí na základě své barvy. Zvolili jsme následující práh v prostoru barev HSV (Hue Saturation Value)

    H ∈ (150, 185)
    S ∈ (0, 50)
    V ∈ (0, 65)

Pixely, jejichž barva leží v tomto prahu jsme prohlásili za popředí, ostatní za pozadí. Obdrželi jsme binární obraz, kde vybarvené pixely odpovídaly číslicím displeje a nevybarvené pixely tvoří pozadí.

Prostor barev HSV je vhodný proto, že struktura tohoto barevného prostoru reflektuje lidské představy o barvě lépe než prostor RGB, navíc konverze mezi těmito barevnými prostory je velice jenoduchá. Vhodnost zvoleného prahu jsme vyhodnotili pomocí vizualní inspekce. Ukázalo se, že tento práh dobře odfiltruje sledovaná čísla od pozadí.

## 2. Segmentace

Protože pixely tvořící jednotlivé číslice na sebe bezprostředně navazují, zatímco mezi číslicemi jsou mezery, prahovaný obraz jsme segmentovali podle spojených komponent. Pro vyloučení šumu jsme ze zpracování vyřadili segmenty menší než 6x6 pixelů. Každý takto získaný segment představuje jednu číslici.

![Obrázek po segmentaci](images/4.png)

## 3. Konstrukce atributů
Použili jsme primárně dva atributy popsané v Interim reportu:

-   levý, pravý, horní a spodní profil segmentu (tento atribut se podle literatury [2] dá dobře využít právě k rozpoznávání číslic)
-   hodnoty všech pixelů segmentu.

Aby byly tyto atributy vzájemně porovnatelné, přeškálovali jsme před jejich výpočtem každý segment na rozměry 20x40 pixelů.

Kromě výše popsaných jsme navíc přidali další dva atributy:

-   atribut poměr šířky a výšky segmentu, který umožňuje klasifikačnímu algoritmu lépe odlišit číslici 1 od číslice 8
-   atribut procentualní podíl černých pixelů v obdélníkovém segmentu má pomoci lépe odlišit číslice 0 a 8.