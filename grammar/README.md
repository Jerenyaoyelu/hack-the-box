# Before Cracking:

Run the instance:
![](./1.png)

Go to instance:
![](./2.png)

# Trials

After going to the instance, I found I do not have permission by being prompted a forbidden error. So I went to inspect and walked around to see if I can find something.

Unluckily, nothing there. So I try to use Burp
![](./3.png)

Steps:

-   After Burp is up, refresh the `http://docker.hackthebox.eu:30065/`
    ![](./4.png)
-   Send to repeater, and got a response
    ![](./5.png)
-   Change `GET` request to `POST` request, and got a response
    ![](./6.png)
    > It seems like only the admin can get the flag
-   Notice that there is a token in the response, decode that as ASCII, I got:
    ![](./7.png)

-   Then I just tried to modify the decoded text and encoded it in Base64 to get a new token
    ![](./8.png)

-   After this, I went back to the request and replace the `PHPSESSID` with the new token to see what will happen.
    ![](./9.png)
    > Luckily, I got the flag

# Result

![](./res.png)
