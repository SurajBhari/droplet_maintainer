# Droplet Maintainer

![Python](https://img.shields.io/badge/Python-3670A0?style=flat&logo=python&logoColor=ffdd54)
![DigitalOcean](https://img.shields.io/badge/DigitalOcean-0080FF?style=flat&logo=digitalocean&logoColor=white)
![Discord](https://img.shields.io/badge/Discord_alerts-5865F2?style=flat&logo=discord&logoColor=white)

This is a simple script that will stop and start DigitalOcean Droplet instances if it fails to GET a particular URL. This is useful for maintaining Droplets that are not behind a load balancer.

See also the AWS sibling: [ec2_maintainer](https://github.com/SurajBhari/ec2_maintainer).


## Flowchart
```mermaid
graph TD
  A[Start] --> B[Initialize variables]
  B --> C[Enter while loop]
  C --> D{URL reachable for T amount?}
  D -->|Yes| C
  D -->|No| E[Restart the Droplet<br>handle unreachable URL]
  E --> C
```


## Configuration

Since whole point is to maintain Droplet instnace. this is made to be hosted on a different machine. that have no connection to the Droplet instance you are monitoring.

You can get digitalocean_token from [Application & API page](https://cloud.digitalocean.com/account/api/tokens).
```
{
    "i-03cdcee6a9ea8be78": {
        "location": {
            "url": "https://streamsnip.com",
            "headers": {},
            "response_code" : 200,
            "timeout" : 10
        },
        "digitalocean_token": "",
        "interval": 60,
        "tolerance" : 10,
        "discord": "https://discord.com/api/webhooks/1205223388512124990/ub640V3iN-"
    }
}
```


## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

## Crontab
```bash
@reboot cd /root/droplet_maitainer && nohup python3 main.py & 
```

