# PHPipam
This repo contains PHPipam integration to VRA, using ABX Python actions
Note that I am in now way a programmer, so please use this for demo purpose only, and/or
reuse it in your own enviroment, for inspiration.
This is first draft. So expect more details later. 

## Postman 
Contains some Postman examples, to test the API.
There is both a Postman enviroment file, and a collection.

## ABX 
Contains the code, required to do the integration.

Zip the files, and import them into VRA, to use them, or just copy the code, into your own action.

## Screenshoots 
Contains screenshoots of different configurations.

## Docker
Docker Compose file, to run PHPipam.
Change all Passwords, hosts and path. All mentioned with !!!value!!!
Note this is the same as the public PHPipam Containers, just modified, to get access to the config
files in www container, to allow for HTTPconnections. 
The original can be found here : https://hub.docker.com/r/phpipam/phpipam-www

## Custom
I have created a cusom field, that i polulate, from the VM deployment. 
It's required today, or else the script will fail. 
The idea behind this, is to have an app id input, for every request, so all applications can 
be easely tracket. This is created, with inspiration from a real customer usecase. 
![Custom Settings](https://github.com/rhjensen79/PHPipam/blob/master/Screenshoots/Custom_Field.png)


## Quick Guide

1. Deploy PHPipam and make sure API over http is allowed. (Guide will follow later)
   This can be done, by adding $api_allow_unsafe = true; to the end of config.docker.php in the 
   /phpipam-wwww data directory.
   Note this is only if you are using the docker-compose file, since the compose file don't allow port 443.
   For production use, please don't use this!

2. Create a PHPipam app and key

3. Update the ABX script, and import it into a new action og copy the code.

4. Create a subscription, and make sure the phpipam.py matches the event in the PHPipa function.

5. Make sure there is a tag in the VM deployment, with requestid (or else the script will fail)

I uses thee following in the input section :

```
requestid:
    type: string
    description: Request ID for approval
    title: Request ID
    default: 123456
```

With a tag in the VM section :

```
tags:
    - key: requestid
      value: '${input.requestid}'
```

6. Deploy a VM and test it. 


A blog post, with a more detailed description to how to use this, will be created as well. 
Create an issue, if you find problems. 
