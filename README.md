# Emotion Detection Using Neural Networks on Embedded Systems

For detailed information on the implementation, refer to the [report](https://github.com/EnricoZanetti/Embedded-EmotionNN/blob/main/report/IoT_Project_Report.pdf) in the repository.

## Overview

This repository contains the implementation of a project aimed at optimizing a neural network for real-time emotion detection using the OpenMV Cam H7 Plus, a resource-constrained edge device, and the Edge Impulse platform.

The project includes setting up the hardware and software environments, collecting and preprocessing the FER2013 dataset, applying transfer learning, and optimizing the model for deployment on the OpenMV Cam H7 Plus. The system was tested and achieved an accuracy of 51.0% in classifying emotions. Face detection was integrated to improve accuracy by focusing on relevant image regions. Real-time data transmission and visualization were implemented using UART communication protocol, MQTT and Grafana, demonstrating potential for continuous monitoring of emotional states. Data were then fetched from the broker by using Node Red and transmitted to a InfluxDB database for persistent storage. The project showcases the feasibility of deploying emotion detection on edge devices and highlights areas for future improvement, such as enhancing model accuracy, real-time feedback, security, and integration with additional sensors.

![Pipeline of the project](https://github.com/EnricoZanetti/Emotion-Detection-Using-Neural-Networks-on-Embedded-Systems/blob/main/images/IoT-pipeline.png)

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Dataset](#dataset)
- [Methodology](#methodology)
- [Results](#results)
- [Challenges and Limitations](#challenges-and-limitations)
- [Future Improvements](#future-improvements)
- [Conclusion](#conclusion)
- [License](#license)
- [References](#references)

## Installation

### Requirements
- OpenMV Cam H7 Plus
- OpenMV IDE
- Python 3.12.4
- Edge Impulse account
- MQTT broker (e.g., Mosquitto)
- Node-Red
- InfluxDB
- Grafana

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/EnricoZanetti/Embedded-EmotionNN
   cd Emotion-Detection-Using-Neural-Networks-on-Embedded-Systems
   ```

2. **Create a virtual environment and install dependencies:**
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Set up OpenMV Cam H7 Plus:**
   - Install the OpenMV IDE and follow the setup instructions for the OpenMV Cam H7 Plus.
   - Upload the `main.py` script to the OpenMV Cam's memory.

4. **Configure Edge Impulse:**
   - Sign up for an Edge Impulse account and follow the instructions to create a new project.
   - Upload the FER2013 dataset to Edge Impulse and follow the impulse design and model training steps.

5. **Configure MQTT, Node-Red, InfluxDB, and Grafana:**
   - Set up an MQTT broker and configure it to receive data from the OpenMV Cam.
   - Set up an InfluxDB instance and create a database to store the emotion detection data.
   - Upload the `node-red-flows.json` file into Node-Red to fetch data from the MQTT broker, process it and send it to the database.
   - Configure a Grafana dashboard to visualize the real-time data.

## Dataset

The FER2013 (Facial Expression Recognition 2013) dataset is used for training the neural network. This dataset contains approximately 35,000 grayscale images of facial expressions categorized into seven emotions: Happy, Sad, Fearful, Neutral, Angry, Surprise, and Disgust. For this project, the Disgust class was discarded due to the low number of images.

## Methodology

1. **Work Environment Preparation:**
   - Set up the OpenMV Cam H7 Plus and configure development environments.
   - Create virtual environments and install necessary requirements.

2. **Dataset Collection and Preprocessing:**
   - Download the FER2013 dataset from [Kaggle](https://www.kaggle.com/datasets/ananthu017/emotion-detection-fer/data).
   - Preprocess the dataset, including resizing and normalizing images. Due to the limitation of the Edge Impulse account, the dataset was reduced from 35,000 images to 30,000. Be careful to maintain the number of images balanced for each class.

3. **Impulse Design and Transfer Learning:**
   - Use Edge Impulse to design the impulse, including processing and learning blocks.
   - Apply transfer learning to adapt a pre-trained model for emotion detection.

4. **Model Selection and Retraining:**
   - Use the EON Tuner to select the best model for the OpenMV Cam H7 Plus.
   - Retrain the selected model to improve accuracy.

5. **Deployment:**
   - Deploy the trained model to the OpenMV Cam H7 Plus.
   - Run the `main.py` script on the OpenMV Cam to perform real-time emotion detection.

6. **Data Transmission and Visualization:**
   - Run the `openmv_emotion_mqtt_publisher.py` script on a PC to retreive the classified emotion by using UART communication protocol.
   - Use MQTT to transmit detected emotions to an MQTT broker.
   - Store the data in an InfluxDB database and visualize it using a Grafana dashboard.

## Results

The project achieved an accuracy of 51.0% in classifying emotions on the OpenMV Cam H7 Plus. The real-time data transmission and visualization components demonstrated the potential for continuous monitoring of emotional states.

## Challenges and Limitations

- Limited training epochs due to Edge Impulse account restrictions.
- Serial port transmission can be improved by using wireless communication protocols such as UDP and a WiFi shield.
- Lack of real-time feedback for the user during emotion detection.

## Future Improvements

- Enhance model accuracy with larger and more diverse datasets.
- Longer training time can improve model's accuracy.
- Develop a user interface for real-time feedback.
- Implement enhanced security measures for data transmission.
- Integrate additional sensors for a more comprehensive analysis of emotional states.
- Explore deployment on alternative platforms with greater computational power.

## Conclusion

This project showcases the feasibility of deploying emotion detection on edge devices and highlights areas for future improvement. The system has potential applications in human-computer interaction, healthcare, and security, enhancing the interaction between humans and machines in meaningful ways.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## References

- FER2013 dataset: [Kaggle](https://www.kaggle.com/c/challenges-in-representation-learning-facial-expression-recognition-challenge/data)
- OpenMV Cam H7 Plus: [OpenMV](https://openmv.io/products/openmv-cam-h7-plus)
- Edge Impulse: [Edge Impulse](https://www.edgeimpulse.com/)
- MQTT: [Eclipse Mosquitto](https://mosquitto.org/)
- InfluxDB: [InfluxDB](https://www.influxdata.com/)
- Grafana: [Grafana](https://grafana.com/)
