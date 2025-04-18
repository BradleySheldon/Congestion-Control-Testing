#!/usr/bin/env python3

import os
import subprocess
import time
from datetime import datetime

# Configurable parameters
cc_protocols = ['cubic', 'bbr', 'vegas']
profiles = {
    'profileA': {'bandwidth': '50Mbps', 'delay': '10ms'},
    'profileB': {'bandwidth': '1Mbps', 'delay': '200ms'}
}
test_duration = 60  # seconds
pantheon_path = './pantheon'  # Adjust if your path differs
output_dir = './results'

# Ensure results directory exists
os.makedirs(output_dir, exist_ok=True)

def run_test(protocol, profile_name, profile_config):
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    result_folder = f"{output_dir}/{protocol}_{profile_name}_{timestamp}"
    os.makedirs(result_folder, exist_ok=True)

    uplink_trace = f"{result_folder}/uplink.trace"
    downlink_trace = f"{result_folder}/downlink.trace"

    # Create Mahimahi trace files
    with open(uplink_trace, 'w') as f:
        f.write(f"{profile_config['bandwidth']}\n")
    with open(downlink_trace, 'w') as f:
        f.write(f"{profile_config['bandwidth']}\n")

    cmd = [
        f"{pantheon_path}/src/experiments/test.py",
        f"--schemes={protocol}",
        f"--uplink-trace={uplink_trace}",
        f"--downlink-trace={downlink_trace}",
        f"--extra-mm-link-args=--uplink-queue=droptail,1000",
        f"--extra-mm-link-args=--downlink-queue=droptail,1000",
        f"--runtime={test_duration}",
        f"--flog={result_folder}/flog.csv",
        f"--data-dir={result_folder}"
    ]

    print(f"\nRunning test for {protocol} on {profile_name}...")
    subprocess.run(" ".join(cmd), shell=True, check=True)
    print(f"✅ Completed: {protocol} on {profile_name}")

def main():
    for protocol in cc_protocols:
        for profile_name, config in profiles.items():
            try:
                run_test(protocol, profile_name, config)
            except subprocess.CalledProcessError as e:
                print(f"Error during test {protocol} on {profile_name}: {e}")
            time.sleep(5)  # brief pause between tests

if __name__ == '__main__':
    main()
