"""
Author: Matthew Schafer
Date: June 5, 2023
Description: A script to generate a random Cisco IOS command question, get an answer from GPT-3, 
             and create a memory in Personal.ai with the question and answer.
   SAMPLE CLI OUTPUT AS FOLLOWS:
Processing command: show standby brief
Memory data for 'show standby brief': {'Text': "Question: \n        1. **Command Operation**: How does the Cisco IOS command 'show standby brief' work? Can you provide a detailed explanation of its functionality?\n        2. **Syntax and Parameters**: What is the syntax for using this command and what parameters are available?\n        3. **Alternate Commands**: Are there any alternate commands that can accomplish similar tasks to 'show standby brief'?\n        4. **Practical Use Cases**: Could you provide some practical use cases or real-world scenarios where 'show standby brief' might be used?\n        5. **Command Efficiency**: What are some tips or tricks to use the 'show standby brief' more efficiently or to get the most out of it?\n        6. **Uncommon Knowledge**: Is there any uncommon knowledge or lesser-known facts about 'show standby brief' that might be useful to know?\n        7. **Learning Resources**: What resources are available for further learning about 'show standby brief'? Can you recommend any online tutorials, courses, or documentation?\n        8. **Troubleshooting**: What are some common issues or errors that might arise when using 'show standby brief' and how can they be resolved?\n        9. **Command Variations**: Are there variations of 'show standby brief' in different versions or models of Cisco hardware? If so, how do they differ?\n        10. **Security Considerations**: What are the security implications or potential risks of using 'show standby brief'?\n        \nAnswer: 1. 'Show standby brief' is a Cisco IOS command that is used to display a summary of the configured Hot Standby Router Protocol (HSRP) active and standby routers on a specific interface. The output shows the interface name, IP address, group number, priority, and current state of the HSRP router. This command helps network administrators identify any standby devices that may have become active and provides an overview of the redundancy configuration.\n\n2. The syntax for using 'show standby brief' is as follows:\n\n   `show standby brief [interface]`\n\n   where `interface` is an optional parameter to specify the interface for which the HSRP status should be displayed. If the `interface` parameter is not provided, all interfaces will be displayed.\n\n3. An alternate command that can be used for a similar task is 'show standby state'. This command also displays the HSRP state information but provides more detailed output, including timers, virtual MAC address, and standby preempt.\n\n4. 'Show standby brief' is useful in scenarios where administrators need to quickly identify which router is active and which is standby in a HSRP group. It can also be used to verify that an interface is configured for HSRP correctly and that the standby router is operational.\n\n5. To get the most out of 'show standby brief', administrators can use the command in conjunction with other HSRP-related commands, such as 'show standby state', 'show standby', and 'show ip interface brief'. Properly configuring and maintaining HSRP is key to ensuring network redundancy and high availability.\n\n6. One lesser-known fact about 'show standby brief' is that it only displays HSRP status information for the IPv4 protocol. For IPv6 HSRP configurations, the command 'show ipv6 standby brief' should be used.\n\n7. There are many resources available for further learning about 'show standby brief', including Cisco's official documentation, online tutorials, and courses. The Cisco Learning Network and Cisco Press active and which is standby in a HSRP group. It can also be used to verify that an interface is configured for HSRP correctly and that the standby router is operational.\n\n5. To get the most out of 'show standby brief', administrators can use the command in conjunction with other HSRP-related commands, such as 'show standby state', 'show standby', and 'show ip interface brief'. Properly configuring and maintaining HSRP is key to ensuring network redundancy and high availability.\n\n6. One lesser-known fact about 'show standby brief' is that it only displays HSRP status information for the IPv4 protocol. For IPv6 HSRP configurations, the command 'show ipv6 standby brief' should be used.\n\n7. There are many resources available for further learning about 'show standby brief', including Cisco's official documentation, online tutorials, and courses. The Cisco Learning Network and Cisco Press are great resources for those looking to dive deeper into HSRP and other networking technologies.\n\n8. Common issues or errors that may arise when using 'show standby brief' include outdated or incorrect configuration and interface or protocol mismatches. These can be resolved by reviewing and updating the HSRP configuration, verifying interface status, and troubleshooting any underlying network issues.\n\n9. Variations of 'show standby brief' may exist in different versions or models of Cisco hardware, but the functionality should be consistent across platforms. It is important to verify the specific command syntax and parameters for each device.\n\n10. The security implications or potential risks of using 'show standby brief' are minimal, as the command only displays information related to HSRP configuration and status. However, it is always important to secure access to network devices and limit who can view sensitive information.</p>", 'Tags': ['Cisco', 'Cisco IOS', 'Command', 'show standby brief']}
Memory creation status for 'show standby brief': Memblock Created        
             
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
