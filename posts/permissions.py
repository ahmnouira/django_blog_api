from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        """
        Requires a user to be logged in or authenticated, in order to have access.
        """
        # authenticated users only can see list view
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        """
        Allows read-only requests but limits write permissions to only the author of the blog post.

        We access the author field via: `obj.author`
        Current user: `request.user`
        """

        # read permissions are allowed to any request so we'll always
        # allow GET, HEAD or OPTIONS requests
        if request.method in permissions.SAFE_METHODS:
            return True

        # write permissions are only allowed to the author of a post
        return obj.author == request.user
