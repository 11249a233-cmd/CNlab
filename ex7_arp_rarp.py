class ARP_RARP_Simulator:
    def __init__(self):
        self.arp_table = {
            "192.168.1.1": "00:0a:95:9d:68:16",
            "192.168.1.2": "00:0a:95:9d:68:17",
            "192.168.1.3": "00:0a:95:9d:68:18"
        }

        self.rarp_table = {
            v: k for k, v in self.arp_table.items()
        }

    def arp_request(self, ip_address):
        print("ARP Request:", ip_address)
        mac_address = self.arp_table.get(ip_address)

        if mac_address:
            print("ARP Reply:", mac_address)
        else:
            print("IP address not found")

    def rarp_request(self, mac_address):
        print("RARP Request:", mac_address)
        ip_address = self.rarp_table.get(mac_address)

        if ip_address:
            print("RARP Reply:", ip_address)
        else:
            print("MAC address not found")

if __name__ == "__main__":
    simulator = ARP_RARP_Simulator()

    simulator.arp_request("192.168.1.1")
    simulator.arp_request("192.168.1.100")

    simulator.rarp_request("00:0a:95:9d:68:16")
    simulator.rarp_request("00:0a:95:9d:68:99")
