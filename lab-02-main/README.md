# Lab 2
[Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) this repo and clone it to your machine to get started!

## Team Members
- Daniel Hotson

## Lab Question Answers

Answer for QuestionA 1: The reliability went down significantly and a lot of the numbers in
 sequence were missed. This was because we used the tc command to limit the qdisc efficiency
so data packets were lost.
Answer for QuestionA 2: The reliability was unchanged. This is because TCP allows for the 
retransmission of lost data packets.
Answer for QuestionA 3: The speed went down due to the retransmission of lost data.

Answer for QuestionC 1: argc is the number of strings passed in main pointed to by *argv[]
Answer for QuestionC 2: the file descriptor is an entry created to represent a specific file 
when opened and the file descriptor table is a list of the open files based on their descriptor
Answer for QuestionC 3: A struct is a grouped list of variable that allows for different variables
to be accessed using one call or pointer. sockaddr_in contains the variables regarding the
 transport address and port for AF_INET.
Answer for QuestionC 4: socket has the input parameters: domain, type, and protocal. If the socket
is successful it returns a nonnegative number if not it returns a -1.
Answer for QuestionC 5: bind has a description paramater the contains the socket, the pointer to
 sockaddr and the size of the address in bytes. Listen can have two parameters: a descriptor
  identifying an unconnected socket and the maximum length that the waitlist of pending connections
   can grow to.
Answer for QuestionC 6: We use while(1) to enter an infinite loop to constantly check for new input
 data. If there are multiple connections the code below will not be able to accept new info from
  both connections if they occur simultaneously.
Answer for QuestionC 7: The fork() command splits the proccesses so that multiple can run at the
 same time, meaning multiple connections could be used.
