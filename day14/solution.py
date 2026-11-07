def _in_range(rule, port):
    # TODO: return True if port is within [rule["from_port"], rule["to_port"]]
    raise NotImplementedError

def port_allowed(rules, port, source_cidr):
    # TODO: True if some rule covers port AND its cidr is "0.0.0.0/0" or equals source_cidr
    raise NotImplementedError

def world_open_ports(rules):
    # TODO: return the sorted list of distinct ports opened to 0.0.0.0/0
    raise NotImplementedError

def has_open_ssh(rules):
    # TODO: return True if port 22 is open to the whole internet
    raise NotImplementedError
