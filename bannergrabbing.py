#improting  socket libraries 
import socket

# Banner Grabbing function
def grab_banner(ip, port, timeout=2):
    # error handling script 
    try:
        #socket Object
        s = socket.socket()
        # socket time out
        s.settimeout(timeout)
        #socket connection
        s.connect((ip, port))
        
        # HTTP needs needs a reuqest others send banner on connect
        if  port in [80, 8080, 8443]:
            s.send(b"HEAD / HTTP/1.0\r\nHost: " + ip.encode() + b"\r\n\r\n")
        
        banner =  s.recv(1024) # bytes recieved
        # socket  connection  closed 
        s.close()

        # decode the banner in recieved in raw bytes and decode into utf-8
        return banner.decode("utf-8", errors="ignore").strip()
    

    # No other  error conditioning 
    except Exception:
        #return nothing 
        return  None

#list of tuples of targt with port  to chekc for banners 
targets = [("10.10.10.5", 21), ("10.10.10.5", 22), ("10.10.10.5", 80)]

# loop all targets and potts in target list 
for ip, port in targets:
    # call banner grab on each iteteration
    banner = grab_banner(ip, port)

    #conditon to print banner 
    if banner:
        print(f"[+] {ip}:{port} -> {banner[:80]}")


