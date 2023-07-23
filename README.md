
<p align="center">
  <a href="https://ergin.dev"><img src="https://raw.githubusercontent.com/EyupErgin/HuntRisePro/main/.img/HuntRisePro.png" width="800px" alt="HuntRisePro"></a>
</p>
<h4 align="center">Modern and Fast RisePro Command and Control Server Detection Tool<br> Version: v1.0 </h4>

---

## :scorpion:	About HuntRisePro
HuntRisePro is a specific, modern and fast command and control detection tool written to detect Command and Control (C2) servers used by the RisePro Stealer Malware. HuntRisePro provides the most reliable and fastest detection among 6 different methods determined as a result of studies on the characteristics and detectability of RisePro C2 servers.

## :notebook:	Features
HuntRisePro offers you the following features.

- Specific and fast scanner,
- Single IP address scanner,
- Multi IP address scanner,
- Extended IP info,
- Extended URL info,
- Extended Web Page info,
- Modern tabular format,
- Wide range of results,
- Multithreading support.

## :inbox_tray:	Install HuntRisePro
1. Clone the project repository or download the zip file:
```bash
git clone https://github.com/eyupergin/HuntRisePro.git
```
2. Install the required Python packages by running the following command:
```bash
pip3 install -r requirements.txt
```
## :desktop_computer:	Use HuntRisePro
HuntRisePro is used via a command-line interface. Below are examples of basic usage.

### Basic Usage
- List arguments:
```bash
python3 main.py -h
```
- To scan a single IP address:
```bash
python3 main.py -t <IP_ADDRESS>
```
- To scan IP addresses from a file:
```bash
python3 main.py -f <FILE_NAME.txt>
```

### Advanced Usage
- To perform scanning with multi-threading:
```bash
python3 main.py -f <FILE_NAME.txt> -mT <THREAD_COUNT>
```
Note: The **"-mT"** parameter allows up to **5** threads.

- To save the scanner results to a JSON file:
```bash
python main.py -t <IP_ADDRESS> -oJ <OUTPUT_FILE.json>
```
## :mag_right: Results
HuntRisePro C2 Scanner tool visualizes the scanning results in a tabular format and prints them to the console. 
Additionally, you can choose to save the results to a JSON file.

Here is an example output of the results:
```
______  __             __________________            ________                 |  Version: v1.0
___  / / /___  __________  /___  __ \__(_)______________  __ \____________    |  Developed by Eyup Sukru ERGIN
__  /_/ /_  / / /_  __ \  __/_  /_/ /_  /__  ___/  _ \_  /_/ /_  ___/  __ \   --------------------------------------
_  __  / / /_/ /_  / / / /_ _  _, _/_  / _(__  )/  __/  ____/_  /   / /_/ /   |  https://ergin.dev
/_/ /_/  \__,_/ /_/ /_/\__/ /_/ |_| /_/  /____/ \___//_/     /_/    \____/    |  https://github.com/eyupergin/huntrisepro

Specific RisePro Command and Control Server Detection Tool

[INFO] Total Scanned IP Addresses: 3 | Detected C2: 3

    STATUS         IP ADDRESS      CN    ASN      PAGE TITLE       FULL URL
--  -------------  --------------  ----  -------  ---------------  --------------------------------
 1  [C2 DETECTED]  192.138.111.11  MT    AS46308  Login — RisePro  http://192.138.111.11:8081/login
 2  [C2 DETECTED]  192.138.111.11  MT    AS46308  Login — RisePro  http://192.138.111.11:8081/login
 3  [C2 DETECTED]  192.138.111.11  MT    AS46308  Login — RisePro  http://192.138.111.11:8081/login
```

---

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

### Contributing
Repo Update Date: 23-07-2023 <br>
If you would like to contribute to this project, please open an issue or submit a pull request. Any contributions and suggestions are welcome!

### Contact
If you have any questions or suggestions, please feel free to contact me.<br>
E-mail: ergindev@gmail.com <br>
Website: www.ergin.dev <br>
LinkedIn: www.linkedin.com/in/eyupergin<br>
