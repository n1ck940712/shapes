from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        print('has_object_permission')
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user

    # def has_permission(self, request, view):
    #     print('has_permission')
    #     print(self, request, view)
    #     return True