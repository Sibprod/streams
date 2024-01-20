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

1GP_content=$(cat "$input_file" | sed 's/France_2/1erGuadeloupe/g; s/hls_fr2/hls_monde/g')
1MQ_content=$(cat "$input_file" | sed 's/France_2/1erMartinique/g; s/hls_fr2/hls_monde/g')
1GF=$(cat "$input_file" | sed 's/France_2/1erGuyane/g; s/hls_fr2/hls_monde/g')
1RE_content=$(cat "$input_file" | sed 's/France_2/1erReunion/g; s/hls_fr2/hls_monde/g')
1YT_content=$(cat "$input_file" | sed 's/France_2/1erMayotte/g; s/hls_fr2/hls_monde/g')

echo "$ 1GP_content" > "$output_dir/1ereGP.m3u8"
echo "$ 1MQ_content" > "$output_dir/1ereMQ.m3u8"
echo "$ 1GF_content" > "$output_dir/1ereGF.m3u8"
echo "$ 1RE_content" > "$output_dir/1ereRE.m3u8"
echo "$ 1YT_content" > "$output_dir/1ereYT.m3u8"
