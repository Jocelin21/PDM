# PDM
Program Design Method

## Purpose and Structure
The purpose of this project is to provide a reliable and efficient P2P protocol for data transfer and storage, using the UDP protocol and socket programming in Python. The project consists of the design and implementation of the protocol, the development of a demo application, testing and validation, and documentation.

3. Scenario 3:
<img src="https://cdn.discordapp.com/attachments/1090244781155823697/1090526112003674142/Sequence_Diagram_Case_3.png%22%3E">

7. Scenario 7:
<img src="https://cdn.discordapp.com/attachments/1090244781155823697/1090526160791814197/Sequence_Diagram_Case_7.png%22%3E">

6. Three-way Handshake: The first VM sends a GET command to request a file from the second VM. The second VM responds with a POST command to accept the request and initiate the file transfer. The file transfer takes place with the exchange of data packets between the two VMs.

List of Steps
- Connect the 2 Virtual Machine (VM):
1. Open the tool properties. 
2. Go to the port forwarding section.
3. Add a new port.
4. Change the protocol to User Datagram Protocol (UDP).
5. Change the host and guest ports.
6. Input the host IP address for the first VM and the guest IP address for the second VM.
7. Change the VM network to NAT Network.
8. Start both VMs and open their terminal.
9. Run the iperf command on both VM.
10. On the first VM, type: "host ip= iperf -s -p <port number> -u".
11. On the second VM, type: "client ip= iperf -c <host ip address> -u -p <port number> -b 10m".

- GET & POST
    - If VM have two IP address:
    1. Establish a connection between both VMs.
    2. Run the get.py program on both VMs.
    3. Enter the IP address and port number on both VMs.
    4. On the first VM, input the "GET" command.
    5. Enter the name of the desired file to retrieve.
    6. Specify a new name for the file
    7. On the second VM, input the "POST" command within 5 seconds after completing step 4 to complete the file transfer. Note that if the command is not entered within the allotted time, the process will time out.
    - If VM have one IP address:
    1. Establish a connection between both VMs.
    2. Run the get.py program on the first VM and get2.py on the second VM.
    3. Enter the IP address and port number on both VMs.
    4. On the first VM, input the "GET" command.
    5. Enter the name of the desired file to retrieve.
    6. Specify a new name for the file
    7. On the second VM, input the "POST" command within 5 seconds after completing step 4 to complete the file transfer. Note that if the command is not entered within the allotted time, the process will time out. 

- Packet Loss
    - If VM have two IP address:
       1. Establish a connection between both VMs.
       2. Run the packetloss2.py program on both VMs.
       3. Enter the IP address and port number on both VMs.
       4. If packet loss (probability 0.25%) does not occur, cancel the program using the control+c command until packet loss is detected.
       5. Once packet loss is detected, try running the program again as you would with the get.py file to confirm proper functionality.
    - If VM have one IP address:
       1. Establish a connection between both VMs.
       2. Run the packetloss2.py program on the first VM and packetloss3.py on the second VM.
       3. Enter the IP address and port number on both VMs.
       4. If packet loss (probability 0.25%) does not occur, cancel the program using the control+c command until packet loss is detected.
       5. Once packet loss is detected, try running the program again as you would with the get.py and get2.py file to confirm proper functionality.
       
Problems Encountered and Solution
1. Incorrect port input prevented the program from running. The issue was resolved by identifying and using the correct port number.
2. Incorrect commands. The issue was resolved by restarting and avoiding typos.
3. Unable to clone repository due to VM's unconnected network.
4. Unconnected network. This was resolved by checking the network connection of the VMs and port. 
