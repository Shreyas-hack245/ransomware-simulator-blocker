#!/bin/bash

# Setup: Create 10 dummy files
echo "[*] Preparing dummy files..."
mkdir -p docs
for i in {1..10}; do
    echo "This is important data in file $i" > docs/file_$i.txt
done

echo "[*] Starting attack simulation in 3 seconds..."
sleep 3

# Simulate rapid modification
for i in {1..10}; do
    echo "[Attack] Encrypting file_$i.txt..."
    echo "ENCRYPTED_CONTENT_XYZ" >> docs/file_$i.txt
    sleep 0.5 # Small delay to see the logs in real-time
done

echo "[*] Simulation complete."