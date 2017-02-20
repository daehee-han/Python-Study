class ContactInfo:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def print_info(self):
        print('{0} : {1}'.format(self.name, self.email))


if __name__ == '__main__':
    sangwon = ContactInfo('홍상원', 'qpakzk@gmail.com')
    hanbit = ContactInfo('hanbit', 'noreply@hanb.co.kr')

    sangwon.print_info()
    hanbit.print_info()