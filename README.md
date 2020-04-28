# PHPipam
This repo contains PHPipam integration to VRA, using ABX Python actions
This is first draft. So expect more details later. 

## Postman 
Contains some Postman examples, to test the API.

## ABX 
Contains the code, required to do the integration.

Zip the files, and import them into VRA, to use them, or just copy the code, into your own action.

## Screenshoots 
Contains screenshoots of different configurations.

## Docker
Docker Compose file, to run PHPipam.
Change all Passwords, hosts and path. All mentioned with !!!value!!!

Note i have changed PHPipam so i can use http and not https. 
This is not recomended for production.

## Quick Guide

1. Deploy PHPipam and make sure API over http is allowed. (Guide will follow later)

2. Create a PHPipam app and key

3. Update the ABX script, and import it into a new action og copy the code.

4. Create a subscription, and make sure the phpipam.py matches the event in the PHPipa function.

5. Deploy a VM and test it. 


A blog post, with a more detailed description to how to use this, will be created as well. 
Create an issue, if you find problems. 
