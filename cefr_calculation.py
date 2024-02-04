#!/usr/bin/env python3

# "This Proggram will calculate how many days YOU learnt language and use all of your time ( X hour per day) until CEFR X"
# This only works starting from CEFR A1 or basic 

# fill out these variables (current ones is example)

# learning time is in hour 
your_learning_time = 2

# your current CEFR level
your_cefr = A2

# CEFR level you wanted to achieve
wanted_cefr = C1

######################################################
# ignore everything after this just hit "Run"
######################################################
CEFR_GRADING_TABLE = {
    A1: 105150,
    A1: 112625,
    A1: 120375,
    A1: 128425,
    A1: 136750,
    A2: 145375,
    A2: 155925,
    A2: 167450,
    A2: 179925,
    A2: 193375,
    B1: 207775,
    B1: 223125,
    B1: 239450,
    B1: 256725,
    B1: 274975,
    B2: 294175,
    B2: 320575,
    B2: 349375,
    B2: 380575,
    B2: 414175,
    B2: 450175,
    C1: 682525,
    C1: 941475,
    C1: 1227225,
    C1: 1540050,
    C1: 1880175,
    C2: 2540050,
    C2: 3654350,
    C2: 4542250,
    C2: 5540050,
    C2: 7540050,
}

time_learning_in_hour_per_day = 1
EXP_PER_20_RESIN = 100

learning_proggress_per_day = time_learning_in_hour_per_day / 20 * EXP_PER_20_RESIN
DAILY_COMMISION_EXP = 500 + (4 * 250)
PRIMOGEM_EXP_PER_DAY = max(min(PRIMOGEM_REFILLS_PER_DAY, 6), 0) * (3 * EXP_PER_20_RESIN)

knowledge_gain_per_day = DAILY_COMMISION_EXP + RESIN_EXP_PER_DAY + PRIMOGEM_EXP_PER_DAY
TOTAL_EXP_REQUIRED = ADVENTURE_RANK_EXP_TABLE[WANTED_AR] - ADVENTURE_RANK_EXP_TABLE[MY_AR] - MY_AR_EXP

print("Current CEFR:", your_cefr, "Exp:", MY_AR_EXP)
print("Total time required:", TOTAL_EXP_REQUIRED)

print("Est. days until CEFR", str(WANTED_CEFR) + ",", TOTAL_EXP_REQUIRED / knowledge_gain_per_day)