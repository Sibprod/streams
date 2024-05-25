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
fr4_content=$(cat "$input_file" | sed 's/France_2/France_4/g; s/hls_fr2/hls_fr4/g')
fr5_content=$(cat "$input_file" | sed 's/France_2/France_5/g; s/hls_fr2/hls_fr5/g')
noa_content=$(cat "$input_file" | sed 's/France_2/Regions_noa/g; s/hls_fr2/hls_noa/g')
fri_content=$(cat "$input_file" | sed 's/France_2/France_Info/g; s/hls_fr2/hls_monde_frinfo/g')
gua_metro_content=$(cat "$input_file" | sed 's/France_2/1er_Guadeloupe/g; s/hls_fr2/hls_monde_1er_Gua/g')
mar_metro_content=$(cat "$input_file" | sed 's/France_2/1er_Martinique/g; s/hls_fr2/hls_monde_1er_Mar/g')
guy_metro_content=$(cat "$input_file" | sed 's/France_2/1er_Guyane/g; s/hls_fr2/hls_monde_1er_Guy/g')
may_metro_content=$(cat "$input_file" | sed 's/France_2/1er_Mayotte/g; s/hls_fr2/hls_monde_1er_May/g')
reu_metro_content=$(cat "$input_file" | sed 's/France_2/1er_Reunion/g; s/hls_fr2/hls_monde_1er_Reu/g')
nca_metro_content=$(cat "$input_file" | sed 's/France_2/1er_Nouvelle_Caledonie/g; s/hls_fr2/hls_monde_1er_NC/g')
pfr_metro_content=$(cat "$input_file" | sed 's/France_2/1er_Polynesie/g; s/hls_fr2/hls_monde_1er_Polynesie/g')
spm_metro_content=$(cat "$input_file" | sed 's/France_2/1er_Saint-Pierre_Miquelon/g; s/hls_fr2/hls_monde_1er_SPM/g')
wfu_metro_content=$(cat "$input_file" | sed 's/France_2/1er_Wallis_Futuna/g; s/hls_fr2/hls_monde_1er_WF/g')

echo "$fr3_content" > "$output_dir/France3.m3u8"
echo "$fr4_content" > "$output_dir/France4.m3u8"
echo "$fr5_content" > "$output_dir/France5.m3u8"
echo "$noa_content" > "$output_dir/France3_NoA.m3u8"
echo "$fri_content" > "$output_dir/FranceInfo.m3u8"
echo "$gua_metro_content" > "$output_dir/La1ere_guadeloupe_metro.m3u8"
echo "$mar_metro_content" > "$output_dir/La1ere_martinique_metro.m3u8"
echo "$gua_metro_content" > "$output_dir/La1ere_guyane_metro.m3u8"
echo "$may_metro_content" > "$output_dir/La1ere_mayotte_metro.m3u8"
echo "$reu_metro_content" > "$output_dir/La1ere_reunion_metro.m3u8"
echo "$nca_metro_content" > "$output_dir/La1ere_NC_metro.m3u8"
echo "$pfr_metro_content" > "$output_dir/La1ere_polynesie_metro.m3u8"
echo "$spm_metro_content" > "$output_dir/La1ere_SPM_metro.m3u8"
echo "$wfu_metro_content" > "$output_dir/La1ere_WF_metro.m3u8"

