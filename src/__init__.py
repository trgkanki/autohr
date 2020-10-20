# Copyright (C) 2020 Hyun Woo Park
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# -*- coding: utf-8 -*-
#
# autohr v20.10.20i59
#
# Copyright: trgk (phu54321@naver.com)
# License: GNU AGPL, version 3 or later;
# See http://www.gnu.org/licenses/agpl.html

import re

from aqt.editor import Editor
from anki.hooks import wrap

from .utils import openChangelog
from .utils import uuid  # duplicate UUID checked here


def beforeSaveNow(self, callback, keepFocus=False, *, _old):
    def newCallback():
        # self.note may be None when edwitor isn't yet initialized.
        # ex: entering browser
        if self.note:
            note = self.note
            for key in note.keys():
                html = note[key]
                html = re.sub(r"-{3,}", "<hr>", html)
                note[key] = html

            if not self.addMode:
                note.flush()
                self.mw.requireReset()

        callback()

    return _old(self, newCallback, keepFocus)


Editor.saveNow = wrap(Editor.saveNow, beforeSaveNow, "around")
