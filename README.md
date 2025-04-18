# Congestion-Control-Testing

# Pantheon Automation Scripts

These scripts were used to generate trace files and automate experiments for congestion control protocol comparison using Stanford's Pantheon framework.

## Requirements
- Python 3.x
- Pantheon cloned locally: https://github.com/StanfordSNR/pantheon
- Mahimahi installed (`sudo apt install mahimahi`)
- Linux kernel with `bbr` and `vegas` modules (e.g., Ubuntu 18.04+)

## Included Scripts

### 1. generate_trace.py
Generates realistic Mahimahi-compatible traces in microseconds for 50 Mbps bandwidth.

To run:
```bash
python3 generate_trace.py
