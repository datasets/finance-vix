#!/bin/bash
mkdir -p archive
mkdir -p data
curl http://www.cboe.com/publish/ScheduledTask/MktData/datahouse/vixcurrent.csv > archive/vixcurrent.csv
cat archive/vixcurrent.csv | \
  # delete note at top
  tail -n+2 | \
  # replace whitespace
  sed "s/ //g" | \
  # change 1/2/2004 to 2004-1-2
  sed "s/^\(..\?\)\/\(..\?\)\/\(....\)/\3-\1-\2/g" | \
  # change 2004-1-2 to 2004-01-02
  sed "s/\<[0-9]\>/0&/g" \
  > data/vix-daily.csv
