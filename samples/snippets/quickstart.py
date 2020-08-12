# Copyright 2017 Google Inc.
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

"""Sample app that queries the Data Loss Prevention API for supported
categories and info types."""

from __future__ import print_function

import argparse
import sys


def quickstart(project_id):
    """Demonstrates use of the Data Loss Prevention API client library."""

    # [START dlp_quickstart]
    # Import the client library
    import google.cloud.dlp

    # Instantiate a client.
    dlp_client = google.cloud.dlp_v2.DlpServiceClient()

    # The string to inspect
    content = "Robert Frost"

    # Construct the item to inspect.
    item = {"value": content}

    # The info types to search for in the content. Required.
    info_types = [{"name": "FIRST_NAME"}, {"name": "LAST_NAME"}]

    # The minimum likelihood to constitute a match. Optional.
    min_likelihood = "LIKELIHOOD_UNSPECIFIED"

    # The maximum number of findings to report (0 = server maximum). Optional.
    max_findings = 0

    # Whether to include the matching string in the results. Optional.
    include_quote = True

    # Construct the configuration dictionary. Keys which are None may
    # optionally be omitted entirely.
    inspect_config = {
        "info_types": info_types,
        "min_likelihood": min_likelihood,
        "include_quote": include_quote,
        "limits": {"max_findings_per_request": max_findings},
    }

    # Convert the project id into a full resource id.
    parent = dlp_client.project_path(project_id)

    # Call the API.
    response = dlp_client.inspect_content(parent, inspect_config, item)

    # Print out the results.
    if response.result.findings:
        for finding in response.result.findings:
            try:
                print("Quote: {}".format(finding.quote))
            except AttributeError:
                pass
            print("Info type: {}".format(finding.info_type.name))
            # Convert likelihood value to string respresentation.
            likelihood = (
                google.cloud.dlp.types.Finding.DESCRIPTOR.fields_by_name[
                    "likelihood"
                ]
                .enum_type.values_by_number[finding.likelihood]
                .name
            )
            print("Likelihood: {}".format(likelihood))
    else:
        print("No findings.")
    # [END dlp_quickstart]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "project_id", help="Enter your GCP project id.", type=str
    )
    args = parser.parse_args()
    if len(sys.argv) == 1:
        parser.print_usage()
        sys.exit(1)
    quickstart(args.project_id)
