from main_module import emailProcess, print_msg

def main():
    emails = ['luongtoi1999@gmail.com', 'lemyhoa@gmail.com', 'minhtam99@gmail.com']
    for email in emails:
        email_name, email_domain = emailProcess(email)
        print_msg(email_name, email_domain)

if __name__ == '__main__':
    main()