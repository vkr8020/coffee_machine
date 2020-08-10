## Coffee Machine Simulation:

### Setup:
```
git clone https://github.com/vkr8020/coffee_machine.git
cd coffee_machine
pip3 install -e . (If pip3 is not available try installing it using "sudo apt-get -y install python3-pip" or alternatively setup using PYTHONPATH)
export PYTHONPATH=${PYTHONPATH}:${HOME}/<dir_path>/coffee_machine (run this only if above command doesn't work)
python3 coffee_machine/main.py coffee_machine/inp/main_inp.json
```
### Assumptions and Key Points: ###
  * Parallelism has been implemented to serve N beverages at a time through the corresponding N outlets.
  * If more requests come at the same time , then it will wait for any outlet to be free and then serves that beverage accordingly.
  * Assumed that only those beverages that are mentioned in the json file can be prepared.
  * All item quantities are assumed to be in ml.
  * Implemeted a functionality to refill an ingredient and show inventory.
  * Whenever an inventory item is below 5ml, the system raises a warning and requests for a refill.
  * Input(user beverage request etc) is taken from stdin.
  * All important messages are redirected to stdout.
  * Due to parallelism, stdout output may be not clear please refer to the generated logfile for more details.
  * logs are available in logs/ dir (ex: cat logs/sample.log)
