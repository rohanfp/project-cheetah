import sys
import json
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

competitor_name = sys.argv[1]

cheetah_status_off = json.load(open('data/cheetah_status_OFF.json'))[competitor_name]
cheetah_status_on = json.load(open('data/cheetah_status_ON.json'))[competitor_name]

ip_address_list = list(cheetah_status_off)
cheetah_status_off_ip_address_executions = [len(cheetah_status_off[ip_address]) for ip_address in ip_address_list]
cheetah_status_on_ip_address_executions = [len(cheetah_status_on[ip_address]) for ip_address in ip_address_list]

x = np.arange(len(ip_address_list))
width = 0.25

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, cheetah_status_off_ip_address_executions, width, label='OFF')
rects2 = ax.bar(x + width/2, cheetah_status_on_ip_address_executions, width, label='ON')

ax.set_ylabel('Executions')
ax.set_title('Scores by Execution and IP address')
ax.set_xticks(x)
ax.set_xticklabels(x)
ax.set_xlabel('IP Address')
ax.legend()

fig.tight_layout()

plt.savefig(f'data/{competitor_name}.png')