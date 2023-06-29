"""Melissa database core"""
# Copyright (C) 2020 - 2023  Famhawite Infosy Team, <https://github.com/lalrochhara.git>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
from typing import TYPE_CHECKING, Any

from Melissa import util

from .Melissa_mixin_base import MixinBase

if TYPE_CHECKING:
    from .Melissa_bot import Melissa


class DatabaseProvider(MixinBase):
    db: util.db.AsyncDatabase

    def __init__(self: "Melissa", **kwargs: Any) -> None:
        if sys.platform == "win32":
            import certifi

            client = util.db.AsyncClient(
                self.config.DB_URI, connect=False, tlsCAFile=certifi.where()
            )
        else:
            client = util.db.AsyncClient(self.config.DB_URI, connect=False)

        self.db = client.get_database("MelissaBot")

        # Propagate initialization to other mixins
        super().__init__(**kwargs)
