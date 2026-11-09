# tcpdump

Capture and read packets. Capturing needs root or the `CAP_NET_RAW` capability, so the commands below use `sudo`. Reading a saved capture does not need root. `-nn` disables name and port-name resolution, which is faster and shows raw addresses.

### List interfaces tcpdump can capture on

```bash
tcpdump -D
```

### Capture on an interface without name resolution

```bash
sudo tcpdump -i <interface> -nn
```

### Capture traffic to or from a host

```bash
sudo tcpdump -i <interface> -nn host 203.0.113.10
```

### Capture traffic on a port

```bash
sudo tcpdump -i <interface> -nn port <port>
```

### Capture only TCP SYN packets

```bash
sudo tcpdump -i <interface> -nn 'tcp[tcpflags] & tcp-syn != 0'
```

### Capture only DNS traffic

```bash
sudo tcpdump -i any -nn udp port 53
```

### Capture a fixed number of packets

```bash
sudo tcpdump -i <interface> -nn -c 100
```

### Write a capture to a pcap file

```bash
sudo tcpdump -i <interface> -nn -w <capture.pcap> port <port>
```

Stop with Ctrl-C. Open the file later in Wireshark or with `-r`.

### Read a pcap file

```bash
tcpdump -nn -r <capture.pcap>
```

### Print packet payloads as ASCII

```bash
sudo tcpdump -i <interface> -nn -A port <port>
```

Only useful for unencrypted protocols such as plain HTTP.

### Show packet contents as hex and ASCII

```bash
sudo tcpdump -i <interface> -nn -X port <port>
```
