CECS 327 - Term Project

The goal of this assignment is to become familiar with peer to peer (P2P) networks and having a client act as a server. You may work on this project in pairs.
Design a program which allows two or more computers to synchronize files across a local area network (LAN). Each computer should run its own local instance of the client software, and the files which will be synchronized should be able to be synchronized multi-directionally.

Example: Nodes P1, P2, . . . Pn have clients C1, C2, . . . Cn installed on each node respectively. F1, F2, . . . Fn are sets of files where F1 is the set of files on node P1, F2 is the set of files on node P2, and so forth. The goal of your program should be the unification of all sets of files, F, so that Pi, Ci ∪ {Fj} on each client.

Peer-to-Peer Project - CECS 327 Summer 2021 

With respect, this lab assignment was very challenging. Our group initially decided to discus which language was bes to code this project in. We ended up decideding to go with using Python due to our coding skills being best in that language. One of the main struggles we had as a group was trying to find a way to discover new IPs in the LAN, and maintain file exchanges and sysnchronization. Overall, the hardest part was understanding the problem as a whole. There are several ways peer-to-peer architectures can be implemented, and that was the issue we had. With each of us having our own implementations, it was hard to decide which route was best to take. Respectfully, we each coded and shared our work in hopes of take out bits and pieces to make an effective solution for this project. As a result, this made it easier to see and observe the different routes to take, and now it was time to decide which solution was best. We ended up going with Matt's solution as a baseline and built up from there to show a solid prototype of our project, as it was able to make a connection to our server and recognize the client. Throughout the project, we all had issues with getting the file synchronizer to work properly although we do have the methods to make it run properly in our main and external branches. Our methods were implemented in hopes to be able to display the current working directory of the first client computer using OS commands, prompt the user to choose while file to send, and finally copy the file (file name, contents, etc) into the current working directory of the second client computer. However, as mentioned earlier, we had trouble trying to find other computers on the network using their IPs, so we were not able to test the connectivity of multiple clients on a shared network. Because of this, we also weren't able to test out our file manager and attempt to share files to one another as much as we hoped for. Ultimately, our goal was to have a peer-to-peer network in which each node could potentially act as a client and server simultaneously in which every node could make and respond to request from any other node on the network. Due to complexity of the project, shorter time frame to work with, and lack of experience in Linux OS, we struggle to complete and show a P2P decentralized network.
 
Operation: 
1. Run server.py
2. Run client.py






