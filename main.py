import argparse
import scapy.all as scapy
import re


def ft_exit(msg):
	print(f"Error: {msg}")
	exit(1)

def is_valid_ip(ip_str):
	try:
		nums = ip_str.split('.')
		if len(nums) != 4:
			return False
		for n in nums:
			if int(n) < 0 or 255 < int(n):
				return False
		return True
	except:
		return False

def is_valid_mac(mac_str):
    mac_regex = r'^([0-9a-fA-F]{2}[:]){5}[0-9a-fA-F]{2}$'
    
    if re.match(mac_regex, mac_str):
        return True
    else:
        return False

def validate_args(args):
	try:
		if not is_valid_ip(args.ip_src):
			ft_exit("Invalid IP-src")
		if not is_valid_mac(args.mac_src):
			ft_exit("Invalid MAC-src")
		if not is_valid_ip(args.ip_target):
			ft_exit("Invalid IP-target")
		if not is_valid_mac(args.mac_target):
			ft_exit("Invalid MAC-target")
	except Exception as e:
		ft_exit(e)

def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument("src_ip", type=str, help="Src-IP")
	parser.add_argument("src_mac", type=str, help="Src-MAC")
	parser.add_argument("dest_ip", type=str, help="Dest-IP")
	parser.add_argument("dest_mac", type=str, help="Dest-MAC")
	args = parser.parse_args()

	return args

def main():
	try:
		args = parse_args()
		validate_args(args)
	except Exception as e:
		ft_exit(e)

if __name__ == "__main__":
    main()