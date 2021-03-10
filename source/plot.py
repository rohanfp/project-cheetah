import sys
import json
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

cheetah_output = json.load(open('data/cheetah_output.json'))
ip_address_counts = {}

for i in range(len(cheetah_output)):
    competitor_name, ip_address = cheetah_output[i].split(",")
    if competitor_name not in ip_address_counts:
        ip_address_counts[competitor_name] = {}
    if ip_address not in ip_address_counts[competitor_name]:
        ip_address_counts[competitor_name][ip_address] = 1
    ip_address_counts[competitor_name][ip_address] += 1

competitor_name_list = list(ip_address_counts)


for competitor_name in competitor_name_list:
    ip_address_list = list(ip_address_counts[competitor_name])
    ip_address_execution_count_list = list(ip_address_counts[competitor_name].values())
    
    x = np.arange(len(ip_address_list))
    width = 0.25

    fig, ax = plt.subplots()
    rects1 = ax.bar(x, ip_address_execution_count_list, width, label='Execution counts')

    ax.set_ylabel('Executions')
    ax.set_title('Execution v/s IP address')
    ax.set_xticks(x)
    ax.set_xticklabels(ip_address_list)
    ax.set_xlabel('IP Address')
    ax.legend()

    fig.tight_layout()
    
    plt.xticks(rotation = (45), fontsize = 10, ha='center')
    plt.savefig(f'data/{competitor_name}.png', bbox_inches='tight', dpi=300)
