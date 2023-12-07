from rest_framework.permissions import BasePermission, SAFE_METHODS
from rolepermissions.permissions import register_object_checker
from rolepermissions.checkers import has_permission as has_permis
from account import roles
from rest_framework.exceptions import PermissionDenied


# this function makes only the first letter of the string lowercase
func = lambda s: s[:1].lower() + s[1:] if s else ''


class IsAdminOrReadOnly(BasePermission):
    message = 'Sorry! Only admin has access to this! :)'

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        elif has_permis(request.user, 'add_information'):
            return request.method in ['GET', 'HEAD', 'OPTIONS', 'POST'] or view.action in ['create', 'update', 'partial_update']
        
        # raise PermissionDenied("Sorry! Only admin has access to this.")
    
    def has_object_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if has_permis(request.user, 'add_information'):
            return request.method in ['GET', 'HEAD', 'OPTIONS', 'POST'] or view.action in ['create', 'update', 'partial_update']
            

class TransactionPermission(BasePermission):
    message = 'Access Denied! :)'

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return request.method in SAFE_METHODS
        if has_permis(request.user, 'assign_transactions'):
            return request.method in ['GET', 'HEAD', 'OPTIONS', 'POST'] or view.action in ['create', 'update', 'partial_update']
        
        return request.method in SAFE_METHODS




class AdminPermission(BasePermission):
    """
    Allows access only to admin users.
    """
    message = 'Sign in as an admin to have access.'
    def has_permission(self, request, view):
        return func(request.user.role) == 'admin'

    def has_object_permission(self, request, view, obj):
        if func(request.user.role) == 'admin':
            # Admin can perform any action except changing the ID or similar restrictions
            restricted_actions = ['change']
            if view.action in restricted_actions:
                return False
            return True
        return False

class MemberPermission(BasePermission):
    """
    Allows access to member users for specific actions.
    """
    def has_permission(self, request, view):
        return func(request.user.role) == 'member'

    def has_object_permission(self, request, view, obj):
        if func(request.user.role) == 'member':
            if view.action in ['update', 'partial_update']:
                # Members can only update their own profiles
                return obj.id == request.user.id
            elif view.action in ['create', 'list', 'retrieve']:
                # Members can read information about books, authors, and publishers
                # They can also write reviews and reserve available books
                return True
        return False

class StaffPermission(BasePermission):
    """
    Allows access to staff users for specific actions.
    """
    def has_permission(self, request, view):
        return func(request.user.role) == 'staff'

    def has_object_permission(self, request, view, obj):
        if func(request.user.role) == 'staff':
            if view.action in ['create', 'list', 'retrieve']:
                # Staff can read information about books, authors, and publishers
                return True
        return False