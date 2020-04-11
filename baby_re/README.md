## Before cracking

download the zip file

## Cracking

-   use password `hackthebox` to open the zip file to obtain the `baby` file
-   open ghidra and import `baby` file
-   filter `htb`
-   from main function in source code grab the following four ciphers
    > 594234427b425448
    > 3448545f5633525f
    > 455f5354
    > 7d5a
    > ![](./1.png)
-   decode cipher by using hex decoder, get the following:

    > 594234427b425448=YB4B{BTH
    > 3448545f5633525f=4HT*V3R*
    > 455f5354=E_ST
    > 7d5a=}Z

-   reverse the deoced text to grab the flag

## Result

HTB{B4BY_R3V_TH4TS_EZ}
![](./re.png)
