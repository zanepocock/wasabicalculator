"""
TODO: Implement CLI tools

Wasabi Calculator

Usage:
  wasabicalc.py expected_fees <amount> <number of past rounds to account for>
  wasabicalc.py expected_time <amount> <number of past rounds to account for>
  wasabicalc.py expected_rounds <amount> <number of past rounds to account for>
  wasabicalc.py expected_change <amount> <number of past rounds to account for>

Options:
  -h --help      Show this screen.
"""

import os, sys, time, datetime, requests, json, math

# All global variables below are recent - pull from API later
MIXES_PER_DAY = 15
MAX_JOIN_SIZE = 0.0998345
COORDINATOR_FEES_PER_ROUND = 0.0042
NUMBER_OF_PARTICIPANTS = 41

"""
TODO: Implement API calls

# Connect to Wasabi API
wasabi_api = requests.get("https://www.wasabiwallet.io/api/v2/btc/ChaumianCoinJoin/states")

past_ten_mixes = [
    {"time_elapsed": 1685037, "join_size": 0.0998345, "coordinator_fees": 0.0042, "participant_count": 41},
    {"time_elapsed": 1685037, "join_size": 0.0998345, "coordinator_fees": 0.0042, "participant_count": 41},
    {"time_elapsed": 1685037, "join_size": 0.0998345, "coordinator_fees": 0.0042, "participant_count": 41},
    {"time_elapsed": 1685037, "join_size": 0.0998345, "coordinator_fees": 0.0042, "participant_count": 41},
    {"time_elapsed": 1685037, "join_size": 0.0998345, "coordinator_fees": 0.0042, "participant_count": 41},
    {"time_elapsed": 1685037, "join_size": 0.0998345, "coordinator_fees": 0.0042, "participant_count": 41},
    {"time_elapsed": 1685037, "join_size": 0.0998345, "coordinator_fees": 0.0042, "participant_count": 41},
    {"time_elapsed": 1685037, "join_size": 0.0998345, "coordinator_fees": 0.0042, "participant_count": 41},
    {"time_elapsed": 1685037, "join_size": 0.0998345, "coordinator_fees": 0.0042, "participant_count": 41},
    {"time_elapsed": 1685037, "join_size": 0.0998345, "coordinator_fees": 0.0042, "participant_count": 41}
]

##################
## PROCESS DATA ##
##################

# Is there a new pool since last checked?
    ...
    time.sleep(10)
    
    # If yes, json.dumps time, fee, utxo size, number of participants
    if new_pool = True:
        past_ten_mixes.append({
            "time_elapsed": time.time,
            "join_size": join_size,
            "coordinator_fees": fees,
            "participant_count": participant_count
        })
    
    # Calculate time elapsed for pool
    
    # Calculate fee per participant
    def fees_per_participant():
        fee_per_utxo = total_fees / participants_number
        return fee_per_utxo
        # json.dumps fee_per_utxo
"""
def truncate(number, digits) -> float:
    stepper = pow(10.0, digits)
    return math.trunc(stepper * number) / stepper

########################
## CALCULATE MIX TIME ##
########################

# Calculate total amount you can mix in a day (e.g. 1.5 BTC)
def value_per_day(MIXES_PER_DAY, MAX_JOIN_SIZE):
    value = MIXES_PER_DAY * MAX_JOIN_SIZE
    return value

# Calculate total days to complete, taking user wealth as input
def days_to_complete(wealth, value):
    days = float(wealth)/float(value)
    return days

# Also give total hours to complete for smaller amounts
def hours_to_complete(days):
    hours = days*24
    return hours

# Also give the total number of CoinJoin mixes
def number_of_mixes(wealth, MAX_JOIN_SIZE):
    rounds =  float(wealth)/MAX_JOIN_SIZE
    return rounds

########################
## CALCULATE FEE COST ##
########################

# Total paid for coordinator fees in last CoinJoin transaction (e.g. 0.0042BTC)
# TODO: Get from API
#def most_recent_fee_total():
    #total_fees = requests.get("https://www.wasabiwallet.io/api/v2/btc/ChaumianCoinJoin/...")
        
# Multiply average participant fee (e.g 0.0001024) by number of rounds required to CoinJoin total balance
def my_total_fee(COORDINATOR_FEES_PER_ROUND, NUMBER_OF_PARTICIPANTS, rounds):
    txn_fee = COORDINATOR_FEES_PER_ROUND / NUMBER_OF_PARTICIPANTS
    fees = txn_fee * rounds
    return fees
    
# Calculate change that will be left over (less than minimum required)
def change_to_mix(rounds, MAX_JOIN_SIZE, fees, wealth):
    total_outputs = (rounds * MAX_JOIN_SIZE) + fees
    change = float(wealth) - float(total_outputs)
    return change

def main():
    while True:
        try:
            wealth = float(input ("Enter how much you want to CoinJoin: "))
        except ValueError:
            print("When I ask for a number, give me a number. Come on!")
        else:
            value = value_per_day(MIXES_PER_DAY, MAX_JOIN_SIZE)
            days = days_to_complete(wealth, value)
            hours = hours_to_complete(days)
            if days < 1:
                total_time = hours
                denomination = "hours"
            else:
                total_time = days
                denomination = "days"
            rounds = number_of_mixes(wealth, MAX_JOIN_SIZE)
            # Round down to integer so only whole rounds are accounted for and change is given
            rounds = int(rounds)
            fees = my_total_fee(COORDINATOR_FEES_PER_ROUND, NUMBER_OF_PARTICIPANTS, rounds)
            change = change_to_mix(rounds, MAX_JOIN_SIZE, fees, wealth)
            print(f"\n\n\n################# COINJOIN ESTIMATOR #################\n\n  Amount to Coinjoin:             {wealth} BTC\n  Time estimate:                  {truncate(total_time, 2)} {denomination}\n  Fees estimate:                  {truncate(fees, 9)} BTC\n\n######################################################\n\n  Max mix per day:                {truncate(value, 3)} BTC\n  Number of CoinJoin rounds:      {rounds} rounds\n  Change/dust:                    {truncate(change, 3)} BTC\n\n######################################################\n\n")
            break

if __name__ == '__main__':
    main()