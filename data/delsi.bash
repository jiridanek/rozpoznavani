#!/ust/bin/env bash
mkdir delsi
ffmpeg -i VID_20110323_110105.3gp -r 15 -f image2 delsi/delsi_r10_%06d.png  
