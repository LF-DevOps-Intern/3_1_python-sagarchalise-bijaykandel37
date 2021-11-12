#!/usr/bin/env bash

function initiateVenv(){
     #To start virtual environment
    
     python3 -m venv myvirtualenv #creates virtual environment
     source myvirtualenv/bin/activate
     echo 'created virtual environment myvirtualenv'
     echo 'the version of python installed is' 
     python -V #displays python version
}
function installpackages()
{
    #to install mentioned package 
    python -m pip install requests

    #to install packages mentioned in the text file.
    xargs sudo apt-get install <packages.txt
    echo 'packages from text file packages.txt have been installed'
}

function main()
{
    initiateVenv 
    installpackages
}
main $@