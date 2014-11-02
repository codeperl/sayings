class Router(object):

    def __init__(self, config):
        self.config = config

    def add_routes(self):

        #home view
        self.config.add_route('home', '/')
        self.config.add_route('home_block_leading_container', '/home_block/leading_container')

        #administration role
        self.config.add_route('administration_role', '/administration/role')
        self.config.add_route('administration_role_add', '/administration/role/add')
        self.config.add_route('administration_role_edit', '/administration/role/edit/{slug}')
        self.config.add_route('administration_role_view', '/administration/role/view/{slug}')
        self.config.add_route('administration_role_remove', '/administration/role/remove/{slug}')

        #administration group
        self.config.add_route('administration_group', '/administration/group')
        self.config.add_route('administration_group_add', '/administration/group/add')
        self.config.add_route('administration_group_edit', '/administration/group/edit/{slug}')
        self.config.add_route('administration_group_view', '/administration/group/view/{slug}')
        self.config.add_route('administration_group_remove', '/administration/group/remove/{slug}')

        #administration group block
        self.config.add_route('administration_group_block_add_instruction', '/administration/group_block/add/instruction')

        #administration user
        self.config.add_route('administration_user', '/administration/user')
        self.config.add_route('administration_user_add', '/administration/user/add')
        self.config.add_route('administration_user_edit', '/administration/user/edit/{slug}')
        self.config.add_route('administration_user_view', '/administration/user/view/{slug}')
        self.config.add_route('administration_user_remove', '/administration/user/remove/{slug}')

        #administration company profile
        self.config.add_route('administration_company_profile', '/administration/company_profile')
        self.config.add_route('administration_company_profile_add', '/administration/company_profile/add')
        self.config.add_route('administration_company_profile_edit', '/administration/company_profile/edit/{slug}')
        self.config.add_route('administration_company_profile_view', '/administration/company_profile/view/{slug}')
        self.config.add_route('administration_company_profile_remove', '/administration/company_profile/remove/{slug}')

        #administration individual profile
        self.config.add_route('administration_individual_profile', '/administration/individual_profile')
        self.config.add_route('administration_individual_profile_add', '/administration/individual_profile/add')
        self.config.add_route('administration_individual_profile_edit', '/administration/individual_profile/edit/{slug}')
        self.config.add_route('administration_individual_profile_view', '/administration/individual_profile/view/{slug}')
        self.config.add_route('administration_individual_profile_remove', '/administration/individual_profile/remove/{slug}')

        #administration page
        self.config.add_route('administration_page', '/administration/page')
        self.config.add_route('administration_page_add', '/administration/page/add')
        self.config.add_route('administration_page_edit', '/administration/page/edit/{slug}')
        self.config.add_route('administration_page_view', '/administration/page/view/{slug}')
        self.config.add_route('administration_page_remove', '/administration/page/remove/{slug}')

        #administrator product
        self.config.add_route('administration_product', '/administration/product')
        self.config.add_route('administration_product_add', '/administration/product/add')
        self.config.add_route('administration_product_edit', '/administration/product/edit/{slug}')
        self.config.add_route('administration_product_view', '/administration/product/view/{slug}')
        self.config.add_route('administration_product_remove', '/administration/product/remove/{slug}')

        #administration service
        self.config.add_route('administration_service', '/administration/service')
        self.config.add_route('administration_service_add', '/administration/service/add')
        self.config.add_route('administration_service_edit', '/administration/service/edit/{slug}')
        self.config.add_route('administration_service_view', '/administration/service/view/{slug}')
        self.config.add_route('administration_service_remove', '/administration/service/remove/{slug}')

        #blog view
        self.config.add_route('blog', '/blog')
        self.config.add_route('blog_view', '/blog/{identity}')
        self.config.add_route('blog_add', '/blog/add')
        self.config.add_route('blog_edit', '/blog/edit/{slug}')
        self.config.add_route('blog_delete', '/blog/delete/{slug}')

        #blog post view
        self.config.add_route('blog_post', '/blog/{identity}/post')
        self.config.add_route('blog_post_view', '/blog/{identity}/post/{slug}')
        self.config.add_route('blog_post_add', '/blog/{identity}/post/add')
        self.config.add_route('blog_post_edit', '/blog/{identity}/post/edit/{slug}')
        self.config.add_route('blog_post_delete', '/blog/{identity}/post/delete/{slug}')

        #forum post view
        self.config.add_route('forum', '/forum')
        self.config.add_route('forum_about', '/forum/about')

        #static page view
        self.config.add_route('static_page_about', '/static_page/about')
        self.config.add_route('static_page_contact', '/static_page/contact')

        #application view
        self.config.add_route('application_top_navigation', '/application/top_navigation')
        self.config.add_route('application_breadcrumb', '/application/breadcrumb')
        self.config.add_route('application_footer', '/application/footer')

        #http common page
        self.config.add_route('http_common_page_not_found', '/http_common_page/not_found')

        return self

    def get_config(self):
        return self.config