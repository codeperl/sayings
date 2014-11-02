from sayings.extensions.python.lib.enum import enum

app_config = enum(
    CSRF_PROTECTION_SECRET_KEY='klfjfuo89389*7j387^*djdjJDHKhdY^&**&&^^'
)

request_method = enum(
    GET='GET',
    POST='POST',
    PUT='PUT',
    DELETE='DELETE',
    PATCH='PATCH',
    HEAD='HEAD',
    OPTIONS='OPTIONS'
)