from xmlrpc.server import SimpleXMLRPCServer

def compute(op, x, y):
        if op == '+':
            return x + y
        elif op == '-':
            return x - y
        elif op == '*':
            return x * y
        elif op == '/':
            return x / y
        else:
            print("Incorrect operation. Valid operations: +, -, *, /")

server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")
server.register_function(compute, "compute")

if __name__ == '__main__':
    try:
        print('Server running...')
        server.serve_forever()
    except KeyboardInterrupt:
        print("Shutting down server.")
