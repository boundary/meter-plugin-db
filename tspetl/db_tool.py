#
# Copyright 2016 BMC Software, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from tspetl import ETLTool


class DBTool(ETLTool):
    def __init__(self):
        pass

    @property
    def name(self):
        return 'db'

    @property
    def help(self):
        return 'import data from a relational database'

    def set_parser(self, parser):
        self._parser = parser.add_parser(self.name, help=self.help)
        self._parser.add_argument('-u', '--user', metavar='name',
                                  help="name of the user to connect to the database")
        self._parser.add_argument('-p', '--password', metavar='password',
                                  help="password of the user to connect to the database")
        self._parser.add_argument('-d', '--database', metavar='db_name',
                                  help="database to extract data from")
        self._parser.add_argument('-q', '--query', metavar='sql_query',
                                  help="SQL query to use to extract data")

    def parse_arguments(self):
        pass

    def run(self):
        print("Import CSV")
        pass