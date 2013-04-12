### Vytvoření snímků z videa

ve složce data spustit bashovy skript `delsi.bash`, který vytvoří složku `delsi` a pomocí ffmpeg v ní vytvoří obrázky odpovídající snímkům videa

### Zpracování snímků

ve složce `prozacatek` spustit `python extract_set.py`

## Popis

postupné zpracování obrázků vypadá takhle

### původní obrázek

<img src="http://jirkadanek.github.com/rozpoznavani/prozacatek/dokumentace/img/vstup.png">

### prahování

        def drop_uninteresting_colors(self):
          size = self.im.size
          for x in xrange(size[0]):
            for y in xrange(size[1]):
              r = self.pix[x,y][0] / 255
              g = self.pix[x,y][1] / 255
              b = self.pix[x,y][2] / 255
              hsv = colorsys.rgb_to_hsv(r,g,b)
              h = hsv[0]*360
              s = hsv[1]*100
              v = hsv[2]*100
              #print v
              if h > 150 and h < 185:
                if s >= 50:
                  if v >= 65:
                    self.pix[x,y] = P_PRESENT
                    continue
              self.pix[x,y] = P_ABSENT

<img src="http://jirkadanek.github.com/rozpoznavani/prozacatek/dokumentace/img/vstup_drop_uninteresting_colors.png">

### filtrování

smyslem je zbavit se malých izolovaných fleků, které by v dalším kroku byly rozpoznány jako další nadpočetné číslice

        def do_filtering(self):
          self.im = self.im.filter(ImageFilter.MaxFilter())
          self.im = self.im.filter(ImageFilter.MinFilter())
          self.im = self.im.filter(ImageFilter.ModeFilter(5))

<img src="http://jirkadanek.github.com/rozpoznavani/prozacatek/dokumentace/img/vstup_do_filtering.png">

### izolování číslic

prochází obrázek po sloupcích, vybere obdélníkovou oblast

myslím, že jsem to, stejně jako pak to rozpoznávání, prostě vykopíroval odsud http://www.wausita.com/captcha/

        def find_numerals(self,image = None):
          if image:
            pix = image.load()
            im = image
          else:
            pix = self.pix
            im = self.im
          img_size = im.size
          w = img_size[0]
          h = img_size[1]
          cnt_nf = 0
          in_znak = False
          znaky = []
          z_x = 0
          y_min = h+1
          y_max = -1
          for x in xrange(w):
            found = False
            for y in xrange(h):
              if pix[x,y] == P_PRESENT:
                found = True
                y_min = min(y_min, y)
                y_max = max(y_max, y)
                cnt_nf = 0
            if found:
              if in_znak == False:
                in_znak = True
                z_x = x
            else:
              cnt_nf = cnt_nf + 1
              if in_znak == True and cnt_nf > 3:
                znaky.append(Group(z_x, y_min, x-cnt_nf, y_max))
                in_znak = False
                cnt_nf = 0
                y_min = h+1
                y_max = -1
          if in_znak:
            znaky.append(Group(z_x, y_min, w-cnt_nf, y_max))
          #FAIL global rozmery_grup
          #raise Exception
          return [g for g in znaky if (g.wx-g.x) > 4 and (g.hy-g.y) > 6]

<img src="http://jirkadanek.github.com/rozpoznavani/prozacatek/dokumentace/img/vstup_find_numerals2.png">

### rotace

proložíme přímku středy těch číslic, každá číslice se orotuje o úhel který ta přímka svírala s osou X

<img src="http://jirkadanek.github.com/rozpoznavani/prozacatek/dokumentace/img/vstup_zarotovani.png">

### rozpoznávání

ten skript používá vzory číslic ve složce vec, které jsem nějak vytípal z videa. Jedná se o učení z instanci, vektorové vyhledávání, nearest neighbour či co to věc. My na to budeme mít Weku.

## Výstup toho pythonu vypadá nějak takhle

        0.1,1175,27.1960784314,5
        0.2,1175,24.9044117647,5
        0.3,1175,24.9044117647,5
        0.4,1175,24.9044117647,5
        0.5,1177,37.300890937,7
        0.6,1177,23.5576036866,7
        0.7,1177,23.9778801843,7
        0.8,1177,23.8783410138,7
        0.9,1175,25.2610294118,5
        1.0,1175,25.4448529412,5
        1.1,1177,25.3482142857,7
        1.2,1175,25.0882352941,5
        1.3,1175,25.5477941176,5
        1.4,1177,36.4711520737,7
        1.5,1175,40.9901960784,5

první číslo je __čas__, druhý je __rozpoznaná hodnota__, třetí __konfidence__ na té číslici, kde byla nejmenší, poslední hodnota je ta __nejméně jistá číslice__

když se to dá do grafu, tak je to něco takovéhodle

<img src="http://jirkadanek.github.com/rozpoznavani/prozacatek/dokumentace/img/vystup.png" width="100%">

celý graf, postupně se přibližujeme

<img src="http://jirkadanek.github.com/rozpoznavani/prozacatek/dokumentace/img/vystup_zoom1.png" width="100%">

=======

<img src="http://jirkadanek.github.com/rozpoznavani/prozacatek/dokumentace/img/vystup_zoom2.png" width="100%">

když se ten graf ještě projde ručně a odmažou se mimo ležící body, vypadá to už docela pěkně

<img src="http://jirkadanek.github.com/rozpoznavani/prozacatek/dokumentace/img/vystup_zeditovany.png" width="100%">

pro to mazání mimoležících bodů je pár velmi krátkých skriptů ve složce filtrování, ale pro vytvoření posleního grafu byla hlavní ruční práce, aby "to vypadalo jak má".