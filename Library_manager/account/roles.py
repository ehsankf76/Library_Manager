from rolepermissions.roles import AbstractUserRole

class Admin(AbstractUserRole):
    available_permissions = {
        'add_information': True,
        'assign_transactions': True,
        'write_reviews': True,
        'read_information': True,
    }

class Staff(AbstractUserRole):
    available_permissions = {
        'assign_transactions': True,
        'read_information': True,
    }

class Member(AbstractUserRole):
    available_permissions = {
        'update_member_profile': True,
        'write_reviews': True,
        'reserve_available_books': True,
        'read_information': True,
    }