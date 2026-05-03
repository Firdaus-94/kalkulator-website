#!bin/bash
clear

echo " ®=======================® "
echo "  pembuat:Gilbert          "
echo "  batas telp:3             "
echo "  tidak bisa pake 08/+62   "
echo "  Example:885876xxxxx      "
echo " ®=======================® "
figlet TELp | lolcat
echo '
[1], prank
[2], Exit tools
'
echo
read -p "masukan pilihan anda : " pil
if [[ $pil == 1 ]]; then
read -p "masukan no target : " nomor
link="https://id.jagreward.com/member/verify-mobile/$nomor"
curl -s $link
else
echo 'terima kasih udah pake tools gue'
exit
fi
echo
