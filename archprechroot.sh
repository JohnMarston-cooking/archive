cfdisk
mkfs.fat -F32 /dev/sda1
mkfs.ext4 /dev/sda2
mount /dev/sda2 /mnt
mount --mkdir /dev/sda1 /mnt/boot
cd /mnt
wget http://mirror.xeonbd.com/archlinux/iso/latest/archlinux-bootstrap-x86_64.tar.zst
tar xpvf archlinux-bootstrap-x86_64.tar.zst
mv /mnt/root.x86_64/* /mnt
cp --dereference /etc/resolv.conf /mnt/etc/
mount --types proc /proc /mnt/proc
mount --rbind /sys /mnt/sys
mount --make-rslave /mnt/sys
mount --rbind /dev /mnt/dev
mount --make-rslave /mnt/dev
mount --bind /run /mnt/run
mount --make-slave /mnt/run
chroot /mnt /bin/bash
