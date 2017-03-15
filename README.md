# Parse_json_introspection_data
python script to parse the json introspection data of overcloud nodes

# Install

~~~
pip install introspectionparser
~~~

# Manual install

~~~
# Clone this repo
git clone https://github.com/ervikrant06/Parse_json_introspection_data

# Install
python setup.py install
~~~

# Requirements

(Ignore if installing using pip)

~~~
pip install prettytable
~~~

# Usage of script

- To get the CPU information.

~~~
$ python parsing_introspection_data.py inspector_data-5d25193b-340c-4d4b-80fe-5b4437d2b904
1: all_interfaces
2: boot_interface
3: cpu_arch
4: cpus
5: error
6: extra
7: interfaces
8: inventory
9: ipmi_address
10: local_gb
11: macs
12: memory_mb
13: root_disk
Enter one numeric value: 6
1: cpu
2: disk
3: firmware
4: ipmi
5: memory
6: network
7: system
Enter one numeric value: 1
+-------------+-----------+-------+---------------+------------+--------+---------+---------+-------------+-------------------------------------------+
| physicalcpu |   clock   | cores | enabled_cores | frequency  | physid | product | threads |    vendor   |                  version                  |
+-------------+-----------+-------+---------------+------------+--------+---------+---------+-------------+-------------------------------------------+
|  physical_0 | 100000000 |   12  |       12      | 2100000000 |   3    |   Xeon  |    24   | Intel Corp. | Intel(R) Xeon(R) CPU E5-4650 v3 @ 2.10GHz |
|  physical_1 | 100000000 |   12  |       12      | 2100000000 |   7    |   Xeon  |    24   | Intel Corp. | Intel(R) Xeon(R) CPU E5-4650 v3 @ 2.10GHz |
|  physical_2 | 100000000 |   12  |       12      | 2100000000 |   17   |   Xeon  |    24   | Intel Corp. | Intel(R) Xeon(R) CPU E5-4650 v3 @ 2.10GHz |
|  physical_3 | 100000000 |   12  |       12      | 2100000000 |   1a   |   Xeon  |    24   | Intel Corp. | Intel(R) Xeon(R) CPU E5-4650 v3 @ 2.10GHz |
+-------------+-----------+-------+---------------+------------+--------+---------+---------+-------------+-------------------------------------------+
~~~

- To get the disk information. 

~~~
$ python parsing_introspection_data.py inspector_data-5d25193b-340c-4d4b-80fe-5b4437d2b904
1: all_interfaces
2: boot_interface
3: cpu_arch
4: cpus
5: error
6: extra
7: interfaces
8: inventory
9: ipmi_address
10: local_gb
11: macs
12: memory_mb
13: root_disk
Enter one numeric value: 6
1: cpu
2: disk
3: firmware
4: ipmi
5: memory
6: network
7: system
Enter one numeric value: 2
+-----------+----------------+------+--------+---------------------+----------------------------------------+
| disk_name |     model      | size | vendor | SMART/serial_number |                 wwn-id                 |
+-----------+----------------+------+--------+---------------------+----------------------------------------+
|    sda    | LOGICAL VOLUME | 299  |   HP   |         None        | wwn-0xxxxxxxxxxxxxxxx7ee025f6375d5d488 |
|    sdb    |      2145      | 3298 |  IBM   |   020320003116XX00  |                  None                  |
|    sdc    |      2145      | 3298 |  IBM   |   020320003116XX00  |                  None                  |
|    sdd    |      2145      | 3298 |  IBM   |   020320003116XX00  |                  None                  |
|    sde    |      2145      | 3298 |  IBM   |   020320003116XX00  |                  None                  |
|    sdf    |      2145      | 3298 |  IBM   |   020320003116XX00  |                  None                  |
|    sdg    |      2145      | 3298 |  IBM   |   020320003116XX00  |                  None                  |
|    sdh    |      2145      | 3298 |  IBM   |   020320003116XX00  | wwn-0xxxxxxxxxxxxxxxx458000000000009ed |
|    sdi    |      2145      | 3298 |  IBM   |   020320003116XX00  | wwn-0xxxxxxxxxxxxxxxx458000000000009ef |
+-----------+----------------+------+--------+---------------------+----------------------------------------+
~~~

- Similarly other switches can be used to fetch the information from introspected data. 
