##Flask API



1. aplicatie flask
2. care sa expuna un endpoint   
   1. URL `/api/rpc/` chemat prin POST
   2.  exemplu de request data : `{"method": "handle_folder_read", "folder": "/tmp"}`
   3. pentru metoda `handle_folder_read` executa `la -al`
   4. output-ul comenzii este capturat si returnat in format JSON


 Exemplu de request : 

```shell script
curl -X POST -d '{"method": "handle_folder_read", "folder": "/tmp"}' http://localhost:5000/api/rpc/
```    

 Exemplu de response : 
 
```shell script
$ la -al

total 8
drwxr-xr-x 1 alexandruaprodu alexandruaprodu  512 Oct 19 16:02 .
drwxr-xr-x 1 root            root             512 Oct 19 16:02 ..
-rw-r--r-- 1 alexandruaprodu alexandruaprodu  220 Oct 19 16:02 .bash_logout
-rw-r--r-- 1 alexandruaprodu alexandruaprodu 3771 Oct 19 16:02 .bashrc
drwxr-xr-x 1 alexandruaprodu alexandruaprodu  512 Oct 19 16:02 .landscape
-rw-rw-rw- 1 alexandruaprodu alexandruaprodu    0 Oct 19 16:02 .motd_shown
-rw-r--r-- 1 alexandruaprodu alexandruaprodu  807 Oct 19 16:02 .profile
```

```JSON
{
  "output" : "-command-output-"
} 
```    
