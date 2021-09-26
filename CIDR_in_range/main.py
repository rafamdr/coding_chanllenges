# Given an IPv4 address and a netmask in CIDR notation, return a boolean specifying whether the IP address is inside
# the given range.
#
# Example:
#
# $ inRange("192.168.4.27", "192.168.0.0/16")
# $ true
#
# $ inRange("192.168.4.27", "192.168.1.0/24")
# $ false
# ----------------------------------------------------------------------------------------------------------------------

def ip_cdr_to_int(ip_addr: str) -> [int, int]:
    sp_ip = list(map(int, ip_addr.replace('/', '.').split('.')))
    return (sp_ip[0] << 24) + (sp_ip[1] << 16) + (sp_ip[2] << 8) + sp_ip[3], \
           (sp_ip[4] if len(sp_ip) > 4 else 32)


def in_range(ip_addr: str, cidr_mask: str) -> bool:
    int_ip, _ = ip_cdr_to_int(ip_addr)
    int_cidr_ip, int_cidr_mask = ip_cdr_to_int(cidr_mask)
    int_cidr_mask = 0xFFFFFFFF - ((1 << int(int_cidr_mask)) - 1)
    return (int_ip & int_cidr_mask) == int_cidr_ip
# ----------------------------------------------------------------------------------------------------------------------


examples = {
    ("192.168.4.27", "192.168.0.0/16"): True,
    ("192.168.4.27", "192.168.1.0/24"): False,
}

for ex in examples:
    print('Ref...: %s -> %s : %s' % (ex, str(examples[ex]), str(in_range(ex[0], ex[1]))))
# ----------------------------------------------------------------------------------------------------------------------
