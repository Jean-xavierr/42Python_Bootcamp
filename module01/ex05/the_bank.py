
class Account(object):

    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        Account.ID_COUNT += 1

    def transfer(self, amount):
        self.value += amount


class Bank(object):

    def __init__(self):
        self.account = []
        self.default_name = 1000
        self.default_id = 1000

    def get_account(self, origin):
        if isinstance(origin, int):
            for account in self.account:
                if account.id == origin:
                    return account
        elif isinstance(origin, str):
            for account in self.account:
                if account.name == origin:
                    return account

    def is_valid_account(self, account) -> bool:
        if not isinstance(account, Account):
            print('Error: the account doesn\'t have an Account instance.')
            return False
        account_info = dir(account)
        if len(account_info) % 2 == 0 or  \
           'zip' not in account_info and  \
           'addr' not in account_info or  \
           'name' not in account_info or  \
           'id' not in account_info or    \
           'value' not in account_info or \
           list(filter(lambda x: x.startswith('b'), account_info)):
            print('Error: corrupted account.')
            return False
        return True

    def add(self, account: Account) -> bool:
        if not self.is_valid_account(account):
            self.fix_account(account)
        self.account.append(account)
        return True

    def is_valid_transfer(self, origin, dest, amount) -> bool:
        if not isinstance(origin, (int, str)):
            print('Error: instance origin.')
            return False
        elif not isinstance(dest, (int, str)):
            print('Error: instance destination.')
            return False
        elif not isinstance(amount, (int, float)):
            print('Error: instance amout.')
            return False
        elif amount < 0:
            print('Error: amout cann\'t be less than 0.')
            return False
        return True

    def transfer(self, origin, dest, amount) -> bool:
        """
        @origin: int(id) or str(name) of the first account
        @dest: int(id) or str(name) of the destination account
        @amount: float(amount) amount to transfer
        @return True if success, False if an error occured
        """
        if not self.is_valid_transfer(origin, dest, amount):
            return False

        origin_account = self.get_account(origin)
        dest_account = self.get_account(dest)
        if origin_account.value < amount:
            print('Error: origin account don\'t '
                  'have enought monney for this transfer.')
            return False
        dest_account.value += amount
        origin_account.value -= amount
        return True

    def fix_account(self, account="") -> bool:
        """
        fix the corrupted account
        @account: int(id) or str(name) of the account
        @return True if sucess, False if an error occured"""
        if self.is_valid_account(account):
            return True
        account_info = dir(account)
        startswith_b = list(filter(lambda x: x.startswith('b'), account_info))
        for elem in startswith_b:
            delattr(account, elem)
        if 'zip' not in account_info and 'addr' not in account_info:
            account.zip = 'default-zip'
        if 'name' not in account_info:
            account.name = 'default-name' + self.default_name
            self.default_name += 1
        if 'id' not in account_info:
            account.id = 'default-id' + self.default_id
            self.default_id += 1
        if 'value' not in account_info:
            account.value = 0
        if len(account_info) % 2 == 0:
            account.default_attr = 0
        print('Fix account: True')
        return True


if __name__ == "__main__":
    bank = Bank()

    john = Account(
                    'William John',
                    zip='100-064',
                    rother="heyhey",
                    ref='58ba2b9954cd278eda8a84147ca73c87',
                    info=None,
                    other='This is the vice president of the corporation',
                    lol="lolilol"
    )

    bank.add(john)

    bank.add(Account(
        'Jane',
        zip='911-745',
        value=1000.0,
        ref='1044618427ff2782f0bbece0abd05f31'
    ))

    jhon = Account(
        'Jhon',
        zip='911-745',
        value=1000.0,
        ref='1044618427ff2782f0bbece0abd05f31'
    )

    bank.add(jhon)

    print("testing a valid transfer")
    print(jhon.value)
    bank.transfer("Jane", "Jhon", 500)
    print(jhon.value)
    bank.transfer("Jane", "Jhon", 1000)
    print(jhon.value)
