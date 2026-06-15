# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright (C) 2018 OSGeo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################

from django.db.models import Subquery
from django.views.generic import TemplateView

from geonode.favorite.models import Favorite
from geonode.security.utils import get_resources_with_perms


DATASET_RESOURCE_TYPE = "dataset"


class TrainingPageView(TemplateView):
    """Renders the Training datasets catalogue page.

    Adds the per-filter dataset counts (My resources, Favorites, Featured) 
    to the template context so the same numbers shown in the
    ResourcesGrid filters can be displayed inline next to the page title.
    """

    template_name = "geonode-mapstore-client/pages/training.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user
        datasets = get_resources_with_perms(user).filter(resource_type=DATASET_RESOURCE_TYPE)

        # Featured is a global flag and is available to anonymous users too.
        featured_count = datasets.filter(featured=True).count()

        if user.is_authenticated:
            my_resources_count = datasets.filter(owner=user).count()
            favorites_count = datasets.filter(
                pk__in=Subquery(
                    Favorite.objects.filter(
                        user=user,
                        content_type__model=DATASET_RESOURCE_TYPE,
                    ).values_list("object_id", flat=True)
                )
            ).count()
        else:
            # The matching filters in the sidebar are disabled for anonymous
            # users, so report zero rather than running user-scoped queries.
            my_resources_count = 0
            favorites_count = 0

        context["training_counts"] = {
            "my_resources": my_resources_count,
            "favorites": favorites_count,
            "featured": featured_count
        }
        return context
