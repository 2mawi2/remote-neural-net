#include <sys/socket.h>
#include <arpa/inet.h>
#include <cstring>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <netdb.h>
#include <unistd.h>
#include <printf.h>
#include <iostream>


int main(int argc, char **argv) {
    struct sockaddr_in addr{};
    char buffer[1024] = {0};
    addr.sin_family = AF_INET;
    inet_aton("127.0.0.1", &addr.sin_addr);
    addr.sin_port = htons(5555);
    int sock = socket(PF_INET, SOCK_STREAM, 0);

    if (connect(sock, (struct sockaddr *) &addr, sizeof(addr)) < 0) {
        std::cout << "neural net service is not running "
                  << "Please make sure to execute the nn server before running the agent "
                  << std::endl;
        return 1;
    }

    auto message = "1 1.7733:8.8899:1.7733:1.7733:1.7733:1.7733 0.8877";
    for (int i = 0; i < 1; ++i) {
        send(sock, message, strlen(message), 0);
        auto received = read(sock, buffer, 1024);
        std::cout << "received " << received << std::endl;
    }

    close(sock);

    return 0;
}