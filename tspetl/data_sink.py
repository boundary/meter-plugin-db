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
from tspapi import API


class DataSink(object):

    def __init__(self):
        pass

    def send_event(self, event):
        pass

    def send_events(self, events):
        pass

    def send_measurement(self, measurement):
        pass

    def send_measurements(self, measurements):
        pass


class APIDataSink(DataSink):

    def __init__(self, email, api_token, api_host):
        super(APIDataSink, self).__init__()
        self._api = API(email=email, api_token=api_token, api_host=api_host)

    def send_event(self, event):
        pass

    def send_events(self, events):
        pass

    def send_measurement(self, measurement):
        self._api.measurement_create(metric=measurement.metric,
                                     value=measurement.value,
                                     source=measurement.source,
                                     timestamp=measurement.source)

    def send_measurements(self, measurements):
        self._api.measurement_create_batch(measurements)


class RPCDataSink(DataSink):

    def __init__(self):
        super(APIDataSink, self).__init__()

    def send_event(self, event):
        pass

    def send_events(self, events):
        pass

    def send_measurement(self, measurement):
        pass

    def send_measurements(self, measurements):
        pass


class StdOutDataSink(DataSink):

    def __init__(self):
        super(APIDataSink, self).__init__()

