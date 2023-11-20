from flask import current_app
from flask_login import current_user
from flask_principal import identity_loaded, identity_changed, ActionNeed, RoleNeed, Permission, Identity, AnonymousIdentity
from enum import Enum

# Custom roles and actions
class Role(str, Enum):
    admin = "admin"
    mod = "mod"
    wanner = "wanner"

class Action(str, Enum):
    create = "create"
    edit = "update"
    delete = "delete"
    view = "list and read"

# Needs
__admin_role_need = RoleNeed(Role.admin)
__mod_role_need = RoleNeed(Role.mod)
__wanner_role_need = RoleNeed(Role.wanner)

__create_action_need = ActionNeed(Action.create)
__edit_action_need = ActionNeed(Action.edit)
__delete_action_need = ActionNeed(Action.delete)
__view_action_need = ActionNeed(Action.view)

# Permissions
require_admin_role = Permission(__admin_role_need)
require_mod_role = Permission(__mod_role_need)
require_wanner_role = Permission(__wanner_role_need)

require_create_permission = Permission(__create_action_need)
require_edit_permission = Permission(__edit_action_need)
require_delete_permission = Permission(__delete_action_need)
require_view_permission = Permission(__view_action_need)

@identity_loaded.connect
def on_identity_loaded(sender, identity):
    identity.user = current_user
    if hasattr(current_user, 'role'):
        if current_user.role == Role.admin:
            # Role needs
            identity.provides.add(__admin_role_need)
            # Action needs
            identity.provides.add(__edit_action_need)
            identity.provides.add(__delete_action_need)
            identity.provides.add(__view_action_need)
        elif current_user.role == Role.mod:
            # Role needs
            identity.provides.add(__mod_role_need)
            # Action needs
            identity.provides.add(__delete_action_need)
            identity.provides.add(__view_action_need)
        elif current_user.role == Role.wanner:
            # Role needs
            identity.provides.add(__wanner_role_need)
            # Action needs
            identity.provides.add(__create_action_need)
            identity.provides.add(__edit_action_need)
            identity.provides.add(__delete_action_need)
            identity.provides.add(__view_action_need)
        else:
            current_app.logger.debug("Unkown role")