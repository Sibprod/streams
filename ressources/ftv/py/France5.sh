#!/bin/bash

input_file="ressources/ftv/py/fr2.m3u8"
output_dir="ressources/ftv/py"

if [ ! -f "$input_file" ]; then
    echo "Input file $input_file not found!"
    exit 1
fi

if [ ! -d "$output_dir" ]; then
    echo "Output directory $output_dir not found!"
    exit 1
fi

fr5_content=$(cat "$input_file" | sed 's/France_2/France_5/g; s/hls_fr2/hls_fr5/g')

echo "$fr5_content" > "$output_dir/France5.m3u8"
