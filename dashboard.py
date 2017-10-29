# encoding: utf-8
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _  # 翻译
from jet.dashboard import modules
from jet.dashboard.dashboard import Dashboard, AppIndexDashboard
from jet.utils import get_admin_site_name


class CustomIndexDashboard(Dashboard):
    columns = 2  # 列数

    def init_with_context(self, context):
        self.available_children.append(modules.LinkList)
        self.available_children.append(modules.Feed)

        site_name = get_admin_site_name(context)
        # append a link list module for "quick links"
        self.children.append(modules.LinkList(
            _('Quick links'),
            layout='stacked',  # values stacked and inline
            draggable=True,
            deletable=True,
            collapsible=True,
            children=[
                [_('Return to site'), '/admin'],
                ['Change password', reverse('%s:password_change' % site_name)],
                ['Log out', reverse('%s:logout' % site_name)],
            ],
            column=1,  # 坐标
            order=0
        ))

        # append an app list module for "Applications"
        self.children.append(modules.AppList(
            _('Producer'),
            # exclude=('producer.*',),
            column=0,
            order=0
        ))

        # append a recent actions module
        self.children.append(modules.RecentActions(
            'Recent Actions',
            # _('Recent Actions'),
            10,
            column=0,
            order=1
        ))

        # append another link list module for "support".
        self.children.append(modules.LinkList(
            _('Learning Tutorials'),
            children=[
                {
                    'title': _('Linkedsee license project'),
                    'url': 'https://gitlab.linkedsee.com/enterprise/license',
                    'external': True,
                },
                {
                    'title': _('Django "django-users" mailing list'),
                    'url': 'http://groups.google.com/group/django-users',
                    'external': True,
                },
                {
                    'title': _('Django irc channel'),
                    'url': 'irc://irc.freenode.net/django',
                    'external': True,
                },
            ],
            column=1,
            order=1
        ))

