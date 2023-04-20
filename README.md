# pyftpdblackhole
ftp server for test

# prerequisites

```
$ sudo pip install pyftpdlib
```

# run

```
$ sudo python3 ftpd.py 
[I 2023-04-20 11:39:18] concurrency model: async
[I 2023-04-20 11:39:18] masquerade (NAT) address: None
[I 2023-04-20 11:39:18] passive ports: None
[I 2023-04-20 11:39:18] >>> starting FTP server on 0.0.0.0:21, pid=715050 <<<
```

# action
- create temp directory
- download files in temp directory
- erase the file on download finished

# reference
- [pyftpdlib tutorial](https://pyftpdlib.readthedocs.io/en/latest/tutorial.html)
- [python tempfile](https://docs.python.org/3/library/tempfile.html)
