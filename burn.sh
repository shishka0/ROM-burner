#!/bin/bash

# Check presence of python3
if [[ $(command -v python3) == '' ]]
then
    echo "Python3 is not installed or could not be found"
    exit -1
fi

python3 ROM_Burner.py $@
