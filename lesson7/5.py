import re

s = """64 bytes from 216.58.215.110: icmp_seq=0 ttl=54 time=30.391 ms
    pass
64 bytes from 216.58.215.110: icmp_seq=1 ttl=54 time=30.667 ms
64 bytes from 216.58.215.110: icmp_seq=2 ttl=54 time=33.201 ms
64 bytes from 216.58.215.110: icmp_seq=3 ttl=54 time=30.140 ms
64 bytes from 216.58.215.110: icmp_seq=4 ttl=54 time=31.822 ms"""


def get_ping_info(random_str):
    first_arg = re.compile(r'seq=(\d+)').findall(random_str)
    sec_argr = re.compile(r'time=(\d+\.\d+)').findall(random_str)
    return tuple(zip(first_arg, sec_argr))

print(get_ping_info(s))