#!/bin/bash

cat playlists/fr.m3u8 > fr.m3u8
tail -n +2 playlists/tf1plus.m3u8 >> fr.m3u8
wget https://jmp2.uk/SamsungTVPlus/fr.m3u8 -O - >> fr.m3u8

exit 0
