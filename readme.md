## SETUP
1. Open ```client.py``` file
2. Change ```id, from_address, to_address, amount``` as you wish.
3. Create a file named same as your ```from_address``` wallet address and put your ```private key``` in this file

## Run the app
In this case I use python 3.7.3 to run the application.

If you wish to run the app using python, you should install dependencies:
```shell
pip install web3
```

Run the server by:
```shell
python vault.py <path>
```
OR
```shell
./vault.py <path>
```

Example:
```shell
./vault.py ./socket
```

Run the client by:
```shell
python client.py <path>
```

Example
```shell
./client.py ./socket
```

If you got an error ```permission denied: ./vault.py``` or ```permission denied: ./client.py```, you should make those file executable by running:
```shell
chmod +x vault.py || chmod +x client.py
```

## Run as excecutable
Executable app is located at ```dist``` directory, before run the program, make sure you have created file to store ```private key``` as mentioned at point 3 above inside this directory.
You can run the binary as follow:
```shell
./vault
```

### Credit:

[Real Python](https://realpython.com/python-sockets)

[Web3py](https://github.com/ethereum/web3.py)