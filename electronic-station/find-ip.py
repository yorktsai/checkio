# http://www.checkio.org/mission/find-ip/

def checkio(text):
    """
        find all IPs
    """
    ips = text.split(" ")
    rt = []
    for ip in ips:
        parts = ip.split(".")
        if len(parts) != 4:
            continue
            
        is_valid = True
        for part in parts:
            if not part.isnumeric() or len(part) <= 0 or len(part) > 3 or (len(part) > 1 and part[0] == "0"):
                is_valid = False
                break
                
            if int(part) < 0 or int(part) > 255:
                is_valid = False
                break
                
        if is_valid:
            rt.append(ip)
            
    return rt

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("192.168.1.1 and 10.0.0.1 or 127.0.0.1") == \
        ["192.168.1.1", "10.0.0.1", "127.0.0.1"], "All correct"
    assert checkio("10.0.0.1.1 but 127.0.0.256 1.1.1.1") == \
        ["1.1.1.1"], "Only 1.1.1.1"
    assert checkio("167.11.0.0 1.2.3.255 192,168,1,1") == \
        ["167.11.0.0", "1.2.3.255"], "0 and 255"
    assert checkio("267.11.0.0 1.2.3.4/16 192:168:1:1") == \
        [], "I don't see IP"
    assert checkio("00250.00001.0000002.1 251.1.2.1") == \
        ["251.1.2.1"], "Be careful with zeros"

