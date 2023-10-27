# Raspberry Pi Pico WiFi Manager

## Description

This Python script for the Raspberry Pi Pico automates the process of connecting to multiple Wi-Fi networks. It includes features like network connection retries and LED status indicators to inform you about the Wi-Fi connection state.

## Installation

1. Install circuit python on your Raspberry Pi Pico
2. Clone this repository
3. Update the `networks` list in the script with your network names and passwords.

## Usage

1. Run the script.
2. The LED will indicate the connection status. A solid light means connection is successful while a slow blink means it is attempting to connect and no light means it has failed to connect.

## Features

- Automatically attempts to connect to multiple networks in a list
- Retries connection a configurable number of times
- LED status indicators
- Periodically checks for an active connection and attempts to reconnect if lost
