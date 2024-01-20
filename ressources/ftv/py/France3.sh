#!/bin/bash

input_file="ressources/ftv/py/France2.m3u8"
output_dir="ressources/ftv/py"

if [ ! -f "$input_file" ]; then
    echo "Input file $input_file not found!"
    exit 1
fi

if [ ! -d "$output_dir" ]; then
    echo "Output directory $output_dir not found!"
    exit 1
fi

fr3_content=$(cat "$input_file" | sed 's/France_2/France_3/g; s/hls_fr2/hls_fr3/g')

echo "$fr3_content" > "$output_dir/France3.m3u8"

