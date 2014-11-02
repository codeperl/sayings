from pyramid.view import view_config
from sayings.models.repositories.group_repository import GroupRepository
from sayings.configs.application_configurations import request_method


class GroupBlock(object):
    def __init__(self, request):
        self.request = request
        self.group_repository = GroupRepository()

    @view_config(route_name='administration_group_block_add_instruction',
                 renderer='sayings:templates/administration/group_block/add_instruction.jinja2')
    def add_instruction(self):
        return {}