from rest_framework.permissions import BasePermission

# this function makes only the first letter of the string lowercase
func = lambda s: s[:1].lower() + s[1:] if s else ''

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