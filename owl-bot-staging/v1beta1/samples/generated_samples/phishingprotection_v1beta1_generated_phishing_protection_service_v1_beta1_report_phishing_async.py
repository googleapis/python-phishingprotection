# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
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
# Generated code. DO NOT EDIT!
#
# Snippet for ReportPhishing
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-phishingprotection


# [START phishingprotection_v1beta1_generated_PhishingProtectionServiceV1Beta1_ReportPhishing_async]
from google.cloud import phishingprotection_v1beta1


async def sample_report_phishing():
    # Create a client
    client = phishingprotection_v1beta1.PhishingProtectionServiceV1Beta1AsyncClient()

    # Initialize request argument(s)
    request = phishingprotection_v1beta1.ReportPhishingRequest(
        parent="parent_value",
        uri="uri_value",
    )

    # Make the request
    response = await client.report_phishing(request=request)

    # Handle the response
    print(response)

# [END phishingprotection_v1beta1_generated_PhishingProtectionServiceV1Beta1_ReportPhishing_async]
