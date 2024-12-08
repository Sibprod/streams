#!/bin/bash

cat playlists/fr.m3u8 > fr.m3u8
tail -n +2 playlists/tf1plus.m3u8 >> fr.m3u8

exit 0
