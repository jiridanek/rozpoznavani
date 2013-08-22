---
title: "Hlavní strana"
layout: "default"
isPage: true
---

Náš projekt se zabývá rozpoznáváním číslic ve videozáznamu. Námi použitý videozáznam zachycuje displej digitálního voltmetru, který měří elektrický potenciál na elektrodě při Bělousově--Žabotínského reakci.

## BZ reakce

Bělousova--žabotinskeho reakce je souhrny název pro skupinu chemických reakci, které vycházejí z původního pokusu provedeného Bělousem. Jedná se o první objevenou oscilační reakci, z toho důvodu je reakce významná pro vývoj chemie. Nejefektivnější varianta této reakce se provádí v Petriho misce a při jejím průběhu vznikají na hladině tekutiny v misce barevné v case a prostoru proměnlivé vzory připomínající struktury na motýlích křídlech.

![Bělousova--Žabotinského reakce](images/Bzr_fotos.jpg)

Předmětem zájmu při této reakci je časový průběh změn pH v reakční nádobě, zprostředkovaný změnou elektrického potenciálu mezi měřící elektrodou v nádobě a referenční elektrodou. Význam měřené hodnoty není pro tento úkol podstatný.

## Cíle

* Za využití metod strojového učení zpracovat několik desítek minut trvající záznam displeje do formátu umožňujícího zkoumání jevu (tj. graf).
* Nástroje vytvořené v tomto projektu by měly být použitelné pro podobné zpracování videí podobnými technickými prostředky za srovnatelných světelných podmínek.

## Použité nástroje

* Python 2.7
* PIL (Python Imaging Library)
* FFmpeg
* Weka 3.7