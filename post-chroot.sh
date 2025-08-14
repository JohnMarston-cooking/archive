echo -e "deb https://mirror.xeonbd.com/debian trixie main contrib non-free non-free-firmware\ndeb https://mirror.xeonbd.com/debian trixie-updates main contrib non-free non-free-firmware\ndeb http://security.debian.org trixie-security main contrib non-free non-free-firmware\ndeb https://mirror.xeonbd.com/debian trixie-backports main contrib non-free non-free-firmware" >> etc/apt/sources.list
apt update
apt install broadcom-sta-dkms linux-headers-6.12.38+deb13-amd64 network-manager -y
