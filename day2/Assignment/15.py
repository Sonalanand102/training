"""
Given:
statuses = [200, 200, 404, 500, 201, 200, 403]


Count how many responses were:
- Successful (200 or 201)
- Client errors (400–499)
- Server errors (500–599)
Expected output should look like:
Successful: 4
Client Errors: 2
Server Errors: 1

"""

statuses = [200, 200, 404, 500, 201, 200, 403]

sucessfull = 0
client_erros = 0
server_errors = 0

for i in statuses:
    if i == 200 or i ==201:
        sucessfull += 1

    elif 400 <= i <= 499:
        client_erros += 1

    elif 500 <= i <= 599:
        server_errors += 1

print("sucessfull", sucessfull)

print (f"client errors", {client_erros})

print(f"server_errors", {server_errors})
