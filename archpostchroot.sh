echo -e 'Server = http://mirror.limda.net/archlinux/$repo/os/$arch\nServer = https://mirror.limda.net/archlinux/$repo/os/$arch\nServer = http://mirror.xeonbd.com/archlinux/$repo/os/$arch\nServer = https://mirror.xeonbd.com/archlinux/$repo/os/$arch' > etc/pacman.d/mirrorlist
pacman-key --init
pacman-key --populate archlinux
pacman -Sy base linux linux-firmware networkmanager grub efibootmgr broadcom-wl
grub-install --target=x86_64-efi --efi-directory=boot --bootloader-id=GRUB
grub-mkconfig -o /boot/grub/grub.cfg
passwd
exit
