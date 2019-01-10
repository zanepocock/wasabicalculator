# Wasabi Wallet Estimator
*NOTE: This is not usable yet. I should have a basic version running over the weekend*

Wasabi Wallet's CoinJoin is fantastic, but it can take a while with large hodlings.
This is a basic python script you can use to calculate a very rough estimate of the time and fees required to CoinJoin an arbitrary amount of BTC.

### TODOS
- [x] Bare bones logic with hard-coded variables from recent days
- [ ] Clean up floats
- [ ] Take fees with each round as they may affect the total rounds we can make
- [ ] Set outputs to five decimal points
- [ ] Make output look better
- [ ] Hook up CLI commands
- [ ] Plug into API