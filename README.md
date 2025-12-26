# Advanced-Network-Topology
Dynamic IoT network topology visualization using Python, NetworkX, and UDP

# Advanced Network Topology Visualization
This project demonstrates dynamic IoT network topology visualization using Python, NetworkX, and UDP-based device discovery.

## Technologies Used
- Python
- NetworkX
- UDP
- Dash / Flask
- Matplotlib

## Project Architecture
- IoT devices broadcast UDP beacons
- Discovery service listens for active devices
- Dashboard dynamically updates the network topology

## How to Run

### Step 1: Install dependencies
python -m pip install dash

### Step 2: Start discovery service
python dashboard.py

### Step 3: Start IoT Devices 
To simulate multiple IoT devices, open a separate Command Prompt window for each device and run: 
python node_beacon.py


