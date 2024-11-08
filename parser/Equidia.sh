#!/bin/bash

python3 parser/equidia.py equidia > ressources/equidia/hls/equidia-live.m3u8
python3 parser/equidia.py trot > ressources/equidia/hls/equidia-racingtrot.m3u8
python3 parser/equidia.py galop > ressources/equidia/hls/equidia-racinggalop.m3u8
python3 parser/equidia.py mag > ressources/equidia/hls/equidia-racingmag.m3u8
python3 parser/equidia.py racing1 > ressources/equidia/hls/equidia-racing1.m3u8
python3 parser/equidia.py racing2 > ressources/equidia/hls/equidia-racing2.m3u8
python3 parser/equidia.py racing3 > ressources/equidia/hls/equidia-racing3.m3u8
python3 parser/equidia.py racing4 > ressources/equidia/hls/equidia-racing4.m3u8
python3 parser/equidia.py racing5 > ressources/equidia/hls/equidia-racing5.m3u8

exit 0
