#!/bin/bash

python3 parser/Equidia.py equidia > ressources/equidia/hls/Equidia.m3u8
python3 parser/Equidia.py trot > ressources/equidia/hls/Racingtrot.m3u8
python3 parser/Equidia.py galop > ressources/equidia/hls/Racinggalop.m3u8
python3 parser/Equidia.py mag > ressources/equidia/hls/Racingmag.m3u8
python3 parser/Equidia.py racing1 > ressources/equidia/hls/Racing1.m3u8
python3 parser/Eequidia.py racing2 > ressources/equidia/hls/Racing2.m3u8
python3 parser/Equidia.py racing3 > ressources/equidia/hls/Racing3.m3u8
python3 parser/Equidia.py racing4 > ressources/equidia/hls/Racing4.m3u8
python3 parser/Equidia.py racing5 > ressources/equidia/hls/Racing5.m3u8

exit 0
