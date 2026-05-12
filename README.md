# Smart Water Distribution & Anomaly Detection System

## Overview
A multi-node IoT system for real-time monitoring and analysis of water distribution networks, designed using a **zone-based modular architecture**. Each zone operates as an independent monitoring unit with a complete sensing stack, enabling scalable deployment across geographically distributed pipelines and storage systems.

---

## Zone Architecture
Each **zone** includes:

- **Main Sensing Unit**
  - Flow sensor  
  - BMP180 (pressure + temperature)  
  - TDS sensor  
  - pH sensor  

- **Valve Monitoring Unit**
  - MPU6050 IMU mounted on valves  
  - Detects vibration patterns indicating leaks, stress, or disturbances  

- **Tank Monitoring Unit**
  - Ultrasonic sensor for water level measurement  
  - Solar-assisted power for remote operation  

---

## Data Acquisition & Backend
- Continuous data streaming via **serial communication (PySerial)**  
- Central processing using **Flask (Python)**  
- Data structured into **zone-wise dictionaries**  
- Enables:
  - Multi-zone separation  
  - Synchronized comparison  
  - Efficient state tracking  

---

## Anomaly Detection

### Hybrid Detection Pipeline

**1. Machine Learning**
- Random Forest model  
- Trained on synthetic dataset  
- Multi-parameter classification using:
  - Flow  
  - Pressure  
  - Vibration  
  - Water quality  

**2. Rule-Based Logic**
- Pressure drop vs flow inconsistency  
- Vibration anomalies in valve nodes  
- Sudden variation in TDS and pH  
- Tank level inconsistencies  

---




# Project Gallery

## Hardware

<table>
  <tr>
    <td><img src="Images/WhatsApp Image 2026-05-02 at 10.43.24.jpeg" width="100%"/></td>
    <td><img src="Images/WhatsApp Image 2026-05-02 at 10.43.25.jpeg" width="100%"/></td>
  </tr>
  <!-- <tr>
    <td><img src="Images/WhatsApp Image 2026-05-02 at 10.43.25 (1).jpeg" width="100%"/></td>
    <td><img src="Images/WhatsApp Image 2026-05-02 at 10.43.26.jpeg" width="100%"/></td>
  </tr> -->
  <tr>
    <td><img src="Images/WhatsApp Image 2026-05-02 at 10.43.27.jpeg" width="100%"/></td>
    <td><img src="Images/WhatsApp Image 2026-05-02 at 10.43.27 (1).jpeg" width="100%"/></td>
  </tr>
  <tr>
    <td><img src="Images/WhatsApp Image 2026-05-02 at 10.43.28.jpeg" width="100%"/></td>
    <td><img src="Images/WhatsApp Image 2026-05-02 at 10.43.44.jpeg" width="100%"/></td>
    
  </tr>
  <tr>
    <td><img src="Images/WhatsApp Image 2026-05-02 at 10.43.41.jpeg" width="100%"/></td>
    <td><img src="Images/WhatsApp Image 2026-05-02 at 10.43.42.jpeg" width="100%"/></td>
  </tr>
  <tr>
    <td><img src="Images/WhatsApp Image 2026-05-02 at 10.43.43.jpeg" width="100%"/></td>
    <td><img src="Images/WhatsApp Image 2026-05-02 at 10.43.34.jpeg" width="100%"/></td>
  </tr>
</table>


## Software Dashboard


Built using **HTML and CSS**

Features:
- Live sensor data streaming  
- Zone-wise monitoring panels  
- Status indicators (normal / abnormal)  
- Real-time anomaly alerts  
- Basic trend visualization  

---



## Working Principle
The system correlates multiple sensing modalities within each zone and compares behavior across zones to detect:

- Leaks  
- Blockages  
- Contamination  
- Structural pipeline issues
- load

---
<table>
  <tr>
    <td><img src="Images/WhatsApp Image 2026-05-02 at 09.29.53.jpeg" width="100%"/></td>
    <td><img src="Images/WhatsApp Image 2026-05-02 at 09.29.53 (1).jpeg" width="100%"/></td>
  </tr>
  <tr>
    <td><img src="Images/WhatsApp Image 2026-05-02 at 09.31.04.jpeg" width="100%"/></td>
    <td></td>
  </tr>
</table>


## System Design Advantages

- **Modularity**
  - Each zone is self-contained and replicable  

- **Scalability**
  - New zones can be added without redesign  

- **Fault Isolation**
  - Issues localized to specific zones or components  

- **Reliability**
  - Multi-sensor fusion reduces false positives  

---
<table>
  <tr>
    <td><img src="Images/Screenshot 2026-04-27 194228.png" width="100%"/></td>
    <td><img src="Images/Screenshot 2026-04-27 194642.png" width="100%"/></td>
  </tr>
</table>
