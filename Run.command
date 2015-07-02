#!/usr/bin/env bash

# Load the RiskRoller directory
cd ${0%/*}

# Run RiskRoller
python RiskRoller.py

# Keep terminal open upon completion of Bash script
$SHELL
