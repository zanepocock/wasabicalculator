# Wasabi Wallet Estimator

Wasabi Wallet's CoinJoin is fantastic, but it can take a while with large hodlings.
This is a basic python script to estimate the time and fees required to CoinJoin your BTC.

**Deprecated - see backend update**

## Usage
```
$ git clone https://github.com/zanepocock/wasabicalculator.git
$ python wasabicalc.py
```

*Example output*

```
$ python wasabicalc.py
Enter how much you want to CoinJoin: 4.78495960


################# COINJOIN ESTIMATOR #################

  Amount to Coinjoin:             4.7849596 BTC
  Time estimate:                  3.19 days
  Fees estimate:                  0.004814634 BTC

######################################################

  Max mix per day:                1.497 BTC
  Number of CoinJoin rounds:      47 rounds
  Change/dust:                    0.087 BTC

######################################################
```

### TODOS
- [x] Basic logic with hard-coded recent data
- [x] Validate user input
- [x] Fix negative change bug
- [x] Format output
- [ ] Tidy up main() function
- [ ] Tidy up float logic
- [ ] Hook up CLI commands
- [ ] Plug into API