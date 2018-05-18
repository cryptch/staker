# Stake Watcher
Python script to check wallet stake status and active it if need

## Getting Started
Use this script to validate current stake status and activate automatically if is inactive using cron.

### Simple example
```
./staker.py
```

### Description
Is required to add some coin information in config.py file:
- COIND_NAME: daemon prefix coin name
- COIND_TYPE: daemon has -cli file or only d file
- UNLOCK_PASS: daemon unlock password
- UNLOCK_ONLY_STAKE: daemon has stake only unlock feature?

More COIND_* parameters, see Coind repository in https://gitlab.com/cryptch/coind

### Prerequisites
- Python 3
- Coind

### Installing
- Clone this repository
- Run ./setup.sh: Install Python and Coind dependencies

### Optional
- Add ./cron.sh to croin: Simple script to execute staker and write a log in ~/out.log

#### cron.sh command example:
```
0 * * * * ~/staker/cron.sh
```
Will execute every hour.

PS: For cron use, need to write daemon full path using COIND_PATH config parameter, or use bash instead Ubuntu/Debian default dash 

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details