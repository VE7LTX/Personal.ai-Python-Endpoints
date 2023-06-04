"""
Author: Matthew Schafer
Date: June 5, 2023
Description: A script to generate a random Cisco IOS command question, get an answer from GPT-3, 
             and create a memory in Personal.ai with the question and answer.
   SAMPLE CLI OUTPUT AS FOLLOWS:
Processing command: vlan
Memory data for 'vlan': {'Text': 'Question: What does the Cisco IOS command \'vlan\' do?\nAnswer: The "vlan" command in Cisco IOS creates a new virtual local area network (VLAN) or modifies an existing one. VLANs allow for the segmentation of a physical network into multiple logical networks, improving network security and performance by isolating traffic between groups of devices. The "vlan" command is used to configure VLAN membership for switch ports, enabling traffic between devices on the same VLAN and blocking traffic between devices on different VLANs.', 'SourceName': 'Python Cisco IOS Command Knowledge Generator', 'CreatedTime': 'Sun, 04 Jun 2023 10:22:51 Pacific Daylight Time', 'DeviceName': 'Change this Device Name Here', 'DomainName': 'ms-cisco-lvl-1', 'RawFeedText': '<p>Question: What does the Cisco IOS command \'vlan\' do?<br>Answer: The "vlan" command in Cisco IOS creates a new virtual local area network (VLAN) or modifies an existing one. VLANs allow for the segmentation of a physical network into multiple logical networks, improving network security and performance by isolating traffic between groups of devices. The "vlan" command is used to configure VLAN membership for switch ports, enabling traffic between devices on the same VLAN and blocking traffic between devices on different VLANs.</p>', 'Tags': ['Cisco', 'Cisco IOS', 'Command', 'vlan']}
Memory creation status for 'vlan': Memblock Created             
             
"""

import requests
import json
import random
import openai
from datetime import datetime
import pytz

# List of some Common Cisco IOS commands
cisco_ios_commands = [
    "show running-config",
    "show startup-config",
    "copy running-config startup-config",
    "config terminal",
    "enable secret",
    "show version",
    "show clock",
    "show interfaces",
    "show ip interface brief",
    "show ip route",
    "show protocols",
    "show mac address-table",
    "show vlan",
    "show controllers",
    "show users",
    "show process cpu",
    "show memory",
    "show access-lists",
    "show logging",
    "show snmp",
    "show buffers",
    "show tcp brief",
    "show ip nat translations",
    "show arp",
    "debug ip packet",
    "debug ip routing",
    "debug ip icmp",
    "no shutdown",
    "hostname",
    "ip name-server",
    "interface",
    "ip address",
    "no ip address",
    "ip helper-address",
    "ip mtu",
    "ip nat inside",
    "ip nat outside",
    "ip nat inside source list",
    "ip route",
    "ip default-gateway",
    "line vty",
    "line console",
    "login",
    "password",
    "enable password",
    "service password-encryption",
    "no service password-encryption",
    "banner motd",
    "no banner motd",
    "clock set",
    "service timestamps",
    "no service timestamps",
    "logging buffered",
    "no logging buffered",
    "access-list",
    "access-group",
    "snmp-server community",
    "snmp-server location",
    "snmp-server contact",
    "snmp-server enable traps",
    "spanning-tree mode",
    "no spanning-tree mode",
    "vlan",
    "no vlan",
    "switchport access vlan",
    "no switchport access vlan",
    "switchport mode",
    "no switchport mode",
    "channel-group",
    "no channel-group",
    "router ospf",
    "router rip",
    "router eigrp",
    "network",
    "no network",
    "area",
    "no area",
    "default-information originate",
    "no default-information originate",
    "passive-interface",
    "no passive-interface",
    "distribute-list",
    "no distribute-list",
    "maximum-paths",
    "no maximum-paths",
    "auto-summary",
    "no auto-summary",
    "debug all",
    "undebug all",
    "reload",
    "write memory",
    "clear counters",
    "clear arp-cache",
    "clear ip route",
    "ping",
    "traceroute",
    "telnet",
    "ssh",
    "crypto key generate rsa",
    "ip ssh version",
    "aaa new-model",
    "aaa authentication login",
    "username",
    "tacacs-server host",
    "radius-server host",
    "show ip bgp summary",
    "show ip bgp",
    "show standby brief",
    "show frame-relay lmi",
    "show frame-relay map",
    "show ldp neighbor",
    "show mpls forwarding-table",
    "show ipv6 interface brief",
    "show ipv6 route",
    "show inventory",
    "show redundancy",
    "show power inline",
    "show environment",
    "show cdp neighbors",
    "show cdp neighbors detail",
    "show ip arp",
    "show controllers serial",
    "show ntp status",
    "show ntp associations",
    "show interfaces status",
    "show interfaces description",
    "show ip ospf neighbor",
    "show ip ospf interface",
    "show ip ospf database",
    "show bgp ipv4 unicast summary",
    "show bgp ipv4 unicast neighbors",
    "show ip bgp ipv4 unicast",
    "show spanning-tree summary",
    "show spanning-tree detail",
    "show ip dhcp binding",
    "show ip dhcp pool",
    "show ip dhcp server statistics",
    "debug condition",
    "ip dhcp excluded-address",
    "ip dhcp pool"
]


def get_local_time():
    # Get local time in a specific format
    user_tz = datetime.now(pytz.utc).astimezone().tzinfo
    local_time = datetime.now(user_tz).strftime('%a, %d %b %Y %H:%M:%S %Z')
    return local_time

def create_memory(api_key, memory_data):
    # Make a POST request to the Personal.ai API to create a memory
    base_url = 'https://api.personal.ai/v1/memory'
    headers = {
        'Content-Type': 'application/json',
        'x-api-key': api_key
    }

    response = requests.post(base_url, headers=headers, json=memory_data)
    
    if response.status_code == 200:
        creation_status = response.json()['status']
        return creation_status
    else:
        return None

def ask_gpt(question):
    # Get an answer for a question from GPT-3 using the text-ada-003 engine
    openai.api_key = 'your-openai-api-key'

    response = openai.Completion.create(
        engine="text-ada-003",
        prompt=question,
        temperature=0.5,
        max_tokens=100
    )

    return response.choices[0].text.strip()
  
def main():
    api_key = 'your-personal-ai-api-key'
    local_time = get_local_time()

    for command in cisco_ios_commands:
        # Generate question and answer about each Cisco IOS command
        question = f"""
        1. **Command Operation**: How does the Cisco IOS command '{command}' work? Can you provide a detailed explanation of its functionality?
        2. **Syntax and Parameters**: What is the syntax for using this command and what parameters are available?
        3. **Alternate Commands**: Are there any alternate commands that can accomplish similar tasks to '{command}'?
        4. **Practical Use Cases**: Could you provide some practical use cases or real-world scenarios where '{command}' might be used?
        5. **Command Efficiency**: What are some tips or tricks to use the '{command}' more efficiently or to get the most out of it?
        6. **Uncommon Knowledge**: Is there any uncommon knowledge or lesser-known facts about '{command}' that might be useful to know?
        7. **Learning Resources**: What resources are available for further learning about '{command}'? Can you recommend any online tutorials, courses, or documentation?
        8. **Troubleshooting**: What are some common issues or errors that might arise when using '{command}' and how can they be resolved?
        9. **Command Variations**: Are there variations of '{command}' in different versions or models of Cisco hardware? If so, how do they differ?
        10. **Security Considerations**: What are the security implications or potential risks of using '{command}'?
        """

        answer = ask_gpt(question)
    
        memory_data = {
            "Text": f"Question: {question}\nAnswer: {answer}",
            "SourceName": "Python Cisco IOS Command Knowledge Generator",
            "CreatedTime": local_time,
            "DeviceName": "Change this Device Name Here",
            "DomainName": "ms-cisco-lvl-1" #Chnage to Match your AI Domain
            "RawFeedText": f"<p>Question: {question}<br>Answer: {answer}</p>",
            "Tags": ["Cisco", "Cisco IOS", "Command", command]  # Add any additional tags here
        }
    
        # Create a memory in Personal.ai with the question and answer
        creation_status = create_memory(api_key, memory_data)
    
        if creation_status is not None:
            print(f"Memory creation status for '{command}': {creation_status}")
        else:
            print(f"Error creating memory for '{command}'")

if __name__ == "__main__":
    main()
