# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright (C) 2017 OSGeo
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

from django.urls import include, path, re_path

from geonode.urls import handler500, urlpatterns as geonode_urlpatterns  # noqa
from geonode_project.views import my_custom_view

# Do not remove handler500 import. It is required to re-export
# the custom error page handler for the GeoNode project
# related issue: https://github.com/GeoNode/geonode-project/issues/570

"""
# You can register your own urlpatterns here
urlpatterns = [
    url(r'^/?$',
        homepage,
        name='home'),
 ] + urlpatterns
"""

urlpatterns = [
    re_path(r"^mycustomurl/$", my_custom_view, name="my_custom_url"),
    path("comments/", include("geonode_project.comments.urls")),
    path(
        "environmental-observations/",
        include("geonode_project.environmental_observations.urls"),
    ),
] + geonode_urlpatterns
