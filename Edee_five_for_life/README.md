# Before Cracking:

Run the instance:

[](./instanceUp.png)

Go to instance:
[](./try1.png)

# Initial Trials

So I try to manully do the submission with the encoded test by using some online MD5 encoder. It turns out that no matter what I tried, I always received a message of too slow!

So I think maybe this is not the correct way to do. I start to think what is the hacker way to hack. The nature of this challenge is making GET and POST requests. So I think maybe a script is another way to do.

# Trial with Scripts

I did some reseach and decided use `requests`, `hashlib` and `beautifulSoup 4` to complete this script. [Click Here](./script.py)

# Result
After running this script, I indeed successfully got the flag. But this script is not 100% guarantee to succeed every time.