# Installation

```
pip install -i requirements.txt
```

# Usage

```
./draw_graph.py \
    -A -1.075 -B 0.01721 -C 1.41156 -D 6.345 \
    --min-x 0 --max-x 365 \
    --title "Tucson : Day Number and Sunrise Hours" \
    --csv-file ./Lab2-Tucson-Raw.csv \
    --csv-y-column "Sunrise Hour" \
    --csv-x-column "Day" \
    --csv-data-label "Sunrise Hours" \
    --output tucson-sunrise-predict.jpg

./draw_graph.py \
    -A 1.125 -B 0.01721 -C 1.15335 -D 18.425 \
    --min-x 0 --max-x 365 \
    --title "Tucson : Day Number and Sunset Hours" \
    --csv-file ./Lab2-Tucson-Raw.csv \
    --csv-y-column "Sunset Hour" \
    --csv-x-column "Day" \
    --csv-data-label "Sunset Hours" \
    --output tucson-sunset-predict.jpg

./draw_graph.py \
    -A 2.11 -B 0.01721 -C 1.34271 -D 12.16 \
    --min-x 0 --max-x 365 \
    --title "Tucson : Day Number and Daylight Length" \
    --csv-file ./Lab2-Tucson-Raw.csv \
    --csv-y-column "Daylight Length" \
    --csv-x-column "Day" \
    --csv-data-label "Daylight Length" \
    --output tucson-daylight-length-predict.jpg
```
