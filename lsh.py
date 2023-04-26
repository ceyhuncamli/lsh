import os
import subprocess

# 1. Create sudo user
username = "your_username"
password = "your_password"
os.system(f"useradd -m {username}")
os.system(f"echo '{username}:{password}' | chpasswd")
os.system(f"usermod -aG sudo {username}")

# 2. Use secure shell protocol (SSH) - Assumes OpenSSH is installed
os.system("systemctl enable ssh")
os.system("systemctl start ssh")

# 3. Setup a basic firewall (ufw)
os.system("apt install ufw")
os.system("ufw enable")
os.system("ufw allow ssh")

# 4. Disable unwanted Linux services
services_to_disable = ["service1", "service2"]
for service in services_to_disable:
    os.system(f"systemctl disable {service}")
    os.system(f"systemctl stop {service}")

# 5. Disable ICMP
os.system("echo 'net.ipv4.icmp_echo_ignore_all = 1' >> /etc/sysctl.conf")
os.system("sysctl -p")

# 6. Enable SELinux
os.system("apt install selinux-utils")
os.system("setenforce 1")

# 7. Install and configure Fail2Ban
os.system("apt install fail2ban")
os.system("systemctl enable fail2ban")
os.system("systemctl start fail2ban")

# 8. Keep kernel and packages updated
os.system("apt update && apt upgrade -y")

# 9. Disable USB and Thunderbolt devices
os.system("echo 'blacklist usb-storage' >> /etc/modprobe.d/blacklist.conf")
os.system("echo 'blacklist thunderbolt' >> /etc/modprobe.d/blacklist.conf")

# 10. Enforce strong password policies
os.system("apt install libpam-pwquality")
os.system("echo 'password requisite pam_pwquality.so retry=3 minlen=10 difok=3' >> /etc/pam.d/common-password")

# 11. Restricting use of previous passwords
os.system("echo 'password sufficient pam_unix.so use_authtok md5 shadow remember=5' >> /etc/pam.d/common-password")

# 12. Purge unnecessary packages to minimize vulnerabilities
os.system("apt autoremove -y")

# 13. Set up password aging
os.system("chage -M 60 -m 7 -W 7 {username}")

# 14. Disable unwanted SUID and SGID binaries
os.system("find / -perm -4000 -o -perm -2000 -exec chmod u-s,g-s {} \;")

# 15. Logging and auditing
os.system("apt install auditd")
os.system("systemctl enable auditd")
os.system("systemctl start auditd")

# 16. Perform regular backups (Configure as needed)
# os.system("...")

# 17. Restricting use of previous passwords (Already done in step 11)

# 18. Monitor listening network ports
os.system("apt install net-tools")
os.system("netstat -tuln")

# 19. Separate disk partitions for Linux system (Requires manual configuration)
# os.system("...")

print("Linux server sıkılaştırma işlemi tamamlandı.")
