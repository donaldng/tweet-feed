# Tweet Feed

This is a twitter wrapper built with another wrapper twitterscrapper.

Most twitter wrapper doesn't offer hastags or dollartags filtering options. 

The purpose of this software is to clean up twitter live feeds which is often infested by all ads spamming bots, which makes life hard trying to consume valuable information from live feeds.


## Example tweet of an typical spam ads 

```
don't miss out on registering on Binance, before registrations close again

https://www.binance.com/?ref=123456

$BTC $ZCL $ETH $ETC $BCH $LTC $XRP $DASH $BTG $XLM $XMR $ZEC $ADA $SNT $NEO $NXT $OMG $POWR $VTC $VOX $XEM $LSK $DGB $DOGE $COVAL $XVG $GRS $AMP $strat $sc $XRB $NAV  94482
```

## Installation

```sh
git clone https://github.com/donaldng/tweet-feed.git
cd tweet-feed
virtualenv -p python3 env
. env/bin/activate
pip install -r requirements.txt
```

## Usage

```sh
python feed.py -q 'Raiden Network' --exclude Radian -l 20 --start 2018-01-15 --end 2018-02-10
```

## Command

```sh
Usage: feed.py [OPTIONS]

Options:
  -q, --query TEXT    Keyword to query. Example: Donald Trump
  -l, --limit TEXT    Limit amount of tweet. Default: no limit
  -e, --exclude TEXT  Except keywords. For multiple keyword to exclude, use
                      comma (,). Example: Apple, Orange
  --start TEXT        Query start time. Example: 2017-12-31
  --end TEXT          Query end time. Example: 2017-12-31
  --help              Show this message and exit.
```

## License

This project is licensed under the MIT License - see the LICENSE.md file for details