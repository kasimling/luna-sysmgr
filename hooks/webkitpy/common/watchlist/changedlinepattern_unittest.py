# Copyright (C) 2011 Google Inc. All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#     * Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above
# copyright notice, this list of conditions and the following disclaimer
# in the documentation and/or other materials provided with the
# distribution.
#     * Neither the name of Google Inc. nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

'''Unit tests for changedlinepattern.py.'''

import unittest
from webkitpy.common.watchlist.changedlinepattern import ChangedLinePattern


class ChangedLinePatternTest(unittest.TestCase):

    # A quick note about the diff file structure.
    # The first column indicated the old line number.
    # The second column indicates the new line number.
    # 0 in either column indicates it had no old or new line number.
    _DIFF_FILE = ((0, 1, 'hi'),
                  (1, 0, 'bye'),
                  (2, 2, 'other'),
                  (3, 0, 'both'),
                  (0, 3, 'both'),
                  )

    def test_added_lines(self):
        self.assertTrue(ChangedLinePattern('hi', 0).match(None, self._DIFF_FILE))
        self.assertTrue(ChangedLinePattern('h.', 0).match(None, self._DIFF_FILE))
        self.assertTrue(ChangedLinePattern('both', 0).match(None, self._DIFF_FILE))
        self.assertFalse(ChangedLinePattern('bye', 0).match(None, self._DIFF_FILE))
        self.assertFalse(ChangedLinePattern('y', 0).match(None, self._DIFF_FILE))
        self.assertFalse(ChangedLinePattern('other', 0).match(None, self._DIFF_FILE))

    def test_removed_lines(self):
        self.assertFalse(ChangedLinePattern('hi', 1).match(None, self._DIFF_FILE))
        self.assertFalse(ChangedLinePattern('h.', 1).match(None, self._DIFF_FILE))
        self.assertTrue(ChangedLinePattern('both', 1).match(None, self._DIFF_FILE))
        self.assertTrue(ChangedLinePattern('bye', 1).match(None, self._DIFF_FILE))
        self.assertTrue(ChangedLinePattern('y', 1).match(None, self._DIFF_FILE))
        self.assertFalse(ChangedLinePattern('other', 1).match(None, self._DIFF_FILE))
