# Wasabi Wallet Estimator
*NOTE: This is not usable yet. I should have a basic version running over the weekend*

Wasabi Wallet's CoinJoin is fantastic, but it can take a while with large hodlings.
This is a basic python script you can use to calculate a very rough estimate of the time and fees required to CoinJoin an arbitrary amount of BTC.

## Usage
```
$ git clone https://github.com/zanepocock/wasabicalculator.git
$ python wasabicalc.py
```

*Example output*

DemoEnviron:wasabicalc Demo$ python wasabicalc.py
Enter how much you want to CoinJoin: 4.78495960

```
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
- [x] Bare bones logic with hard-coded variables from recent days
- [x] Set outputs to x decimal points
- [x] Make output look better
- [x] Fix negative change bug
- [x] Validate user input before using it
- [ ] Tidy up main() function
- [ ] Tidy up float logic
- [ ] Hook up CLI commands
- [ ] Plug into API