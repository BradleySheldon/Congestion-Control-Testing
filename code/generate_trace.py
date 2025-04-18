# generate_trace.py

def write_trace(filename, rate_mbps, duration_sec):
    bits_per_packet = 1500 * 8
    packets_per_sec = (rate_mbps * 1_000_000) / bits_per_packet
    interval_usec = int(1_000_000 / packets_per_sec)

    with open(filename, "w") as f:
        t = 0
        while t < duration_sec * 1_000_000:
            f.write(f"{int(t)}\n")
            t += interval_usec

write_trace("trace_50mbps.up", rate_mbps=50, duration_sec=60)
write_trace("trace_50mbps.down", rate_mbps=50, duration_sec=60)
