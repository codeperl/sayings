from pyramid.view import view_config
from sayings.models.services.product_service import ProductService
from sayings.models.services.builders.forms.product_form_builder import ProductFormBuilder
from pyramid.httpexceptions import HTTPFound
from sayings.models.entities.product import Product as ProductModel
from sayings.configs.application_configurations import request_method


class Product(object):
    def __init__(self, request):
        self.request = request
        self.product_service = ProductService(request)
        self.product_form_builder = ProductFormBuilder(request)

    @view_config(route_name='administration_product', renderer='sayings:templates/administration/product/index.jinja2')
    def index(self):
        products = self.product_service.find_all()
        return {'products': products}

    @view_config(route_name='administration_product_add',
                 renderer='sayings:templates/administration/product/add.jinja2')
    def add(self):
        product = ProductModel()
        form = self.product_form_builder.build_create_form().get_form()

        if self.request.method == request_method.POST:
            if form.validate():
                form.populate_obj(product)
                self.product_service.insert(product)
                return HTTPFound(location=self.request.route_url('administration_product'))
        return {'form': form}

    @view_config(route_name='administration_product_edit',
                 renderer='sayings:templates/administration/product/edit.jinja2')
    def edit(self):
        id = int(self.request.matchdict['slug'])
        product = self.product_service.find_one_by_id(id)

        if not product:
            return HTTPFound(location=self.request.route_url('http_common_page_not_found'))

        form = self.product_form_builder.build_update_form(product).get_form()

        if self.request.method == request_method.POST:
            if form.validate():
                form.populate_obj(product)
                self.product_service.update(product)
                return HTTPFound(location=self.request.route_url('administration_product'))
        return {'form': form}

    @view_config(route_name='administration_product_view',
                 renderer='sayings:templates/administration/product/view.jinja2')
    def view(self):
        id = int(self.request.matchdict['slug'])
        product = self.product_service.find_one_by_id(id)

        if not product:
            return HTTPFound(location=self.request.route_url('http_common_page_not_found'))
        return {'product': product}

    @view_config(route_name='administration_product_remove',
                 renderer='sayings:templates/administration/product/remove.jinja2')
    def remove(self):
        id = int(self.request.matchdict['slug'])

        product = self.product_service.find_one_by_id(id)

        if not product:
            return HTTPFound(location=self.request.route_url('http_common_page_not_found'))

        self.product_service.remove(product)
        return HTTPFound(location=self.request.route_url('administration_product'))