#!/bin/bash -e

source /Users/creich/sendsms/bin/activate

echo "sendsms activated"

if [ -s "/Users/creich/web_scraping/massey_peabody/nfl_flag.txt" ];
then
  echo "nfl already done"
else
  echo "running NFL"
  cd /Users/creich/web_scraping/massey_peabody/
  /usr/local/bin/scrapy crawl NFL_mp
  python nfl_send_message.py
fi


if [ -s "/Users/creich/web_scraping/massey_peabody/cfb_flag.txt" ];
then
  echo "cfb already done"
else
  echo "running CFB"
  cd /Users/creich/web_scraping/massey_peabody
  /usr/local/bin/scrapy crawl CFB_mp
  python cfb_send_message.py
fi
