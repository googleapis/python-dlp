# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
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

from google.auth.transport.requests import AuthorizedSession  # type: ignore
import json  # type: ignore
import grpc  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore
from google.api_core import exceptions as core_exceptions
from google.api_core import retry as retries
from google.api_core import rest_helpers
from google.api_core import rest_streaming
from google.api_core import path_template
from google.api_core import gapic_v1

from google.protobuf import json_format
from google.cloud.location import locations_pb2 # type: ignore
from requests import __version__ as requests_version
import dataclasses
import re
from typing import Callable, Dict, List, Optional, Sequence, Tuple, Union
import warnings

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object]  # type: ignore


from google.cloud.dlp_v2.types import dlp
from google.protobuf import empty_pb2  # type: ignore

from .base import DlpServiceTransport, DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=BASE_DEFAULT_CLIENT_INFO.gapic_version,
    grpc_version=None,
    rest_version=requests_version,
)


class DlpServiceRestInterceptor:
    """Interceptor for DlpService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the DlpServiceRestTransport.

    .. code-block:: python
        class MyCustomDlpServiceInterceptor(DlpServiceRestInterceptor):
            def pre_activate_job_trigger(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_activate_job_trigger(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_cancel_dlp_job(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_create_deidentify_template(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_deidentify_template(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_dlp_job(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_dlp_job(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_inspect_template(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_inspect_template(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_job_trigger(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_job_trigger(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_stored_info_type(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_stored_info_type(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_deidentify_content(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_deidentify_content(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_deidentify_template(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_dlp_job(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_inspect_template(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_job_trigger(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_stored_info_type(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_finish_dlp_job(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_get_deidentify_template(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_deidentify_template(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_dlp_job(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_dlp_job(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_inspect_template(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_inspect_template(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_job_trigger(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_job_trigger(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_stored_info_type(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_stored_info_type(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_hybrid_inspect_dlp_job(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_hybrid_inspect_dlp_job(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_hybrid_inspect_job_trigger(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_hybrid_inspect_job_trigger(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_inspect_content(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_inspect_content(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_deidentify_templates(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_deidentify_templates(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_dlp_jobs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_dlp_jobs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_info_types(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_info_types(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_inspect_templates(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_inspect_templates(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_job_triggers(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_job_triggers(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_stored_info_types(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_stored_info_types(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_redact_image(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_redact_image(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_reidentify_content(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_reidentify_content(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_deidentify_template(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_deidentify_template(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_inspect_template(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_inspect_template(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_job_trigger(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_job_trigger(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_stored_info_type(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_stored_info_type(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = DlpServiceRestTransport(interceptor=MyCustomDlpServiceInterceptor())
        client = DlpServiceClient(transport=transport)


    """
    def pre_activate_job_trigger(self, request: dlp.ActivateJobTriggerRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[dlp.ActivateJobTriggerRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for activate_job_trigger

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_activate_job_trigger(self, response: dlp.DlpJob) -> dlp.DlpJob:
        """Post-rpc interceptor for activate_job_trigger

        Override in a subclass to manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code.
        """
        return response
    def pre_cancel_dlp_job(self, request: dlp.CancelDlpJobRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[dlp.CancelDlpJobRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for cancel_dlp_job

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def pre_create_deidentify_template(self, request: dlp.CreateDeidentifyTemplateRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[dlp.CreateDeidentifyTemplateRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for create_deidentify_template

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_create_deidentify_template(self, response: dlp.DeidentifyTemplate) -> dlp.DeidentifyTemplate:
        """Post-rpc interceptor for create_deidentify_template

        Override in a subclass to manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code.
        """
        return response
    def pre_create_dlp_job(self, request: dlp.CreateDlpJobRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[dlp.CreateDlpJobRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for create_dlp_job

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_create_dlp_job(self, response: dlp.DlpJob) -> dlp.DlpJob:
        """Post-rpc interceptor for create_dlp_job

        Override in a subclass to manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code.
        """
        return response
    def pre_create_inspect_template(self, request: dlp.CreateInspectTemplateRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[dlp.CreateInspectTemplateRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for create_inspect_template

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_create_inspect_template(self, response: dlp.InspectTemplate) -> dlp.InspectTemplate:
        """Post-rpc interceptor for create_inspect_template

        Override in a subclass to manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code.
        """
        return response
    def pre_create_job_trigger(self, request: dlp.CreateJobTriggerRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[dlp.CreateJobTriggerRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for create_job_trigger

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_create_job_trigger(self, response: dlp.JobTrigger) -> dlp.JobTrigger:
        """Post-rpc interceptor for create_job_trigger

        Override in a subclass to manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code.
        """
        return response
    def pre_create_stored_info_type(self, request: dlp.CreateStoredInfoTypeRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[dlp.CreateStoredInfoTypeRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for create_stored_info_type

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_create_stored_info_type(self, response: dlp.StoredInfoType) -> dlp.StoredInfoType:
        """Post-rpc interceptor for create_stored_info_type

        Override in a subclass to manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code.
        """
        return response
    def pre_deidentify_content(self, request: dlp.DeidentifyContentRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[dlp.DeidentifyContentRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for deidentify_content

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_deidentify_content(self, response: dlp.DeidentifyContentResponse) -> dlp.DeidentifyContentResponse:
        """Post-rpc interceptor for deidentify_content

        Override in a subclass to manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code.
        """
        return response
    def pre_delete_deidentify_template(self, request: dlp.DeleteDeidentifyTemplateRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[dlp.DeleteDeidentifyTemplateRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for delete_deidentify_template

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def pre_delete_dlp_job(self, request: dlp.DeleteDlpJobRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[dlp.DeleteDlpJobRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for delete_dlp_job

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def pre_delete_inspect_template(self, request: dlp.DeleteInspectTemplateRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[dlp.DeleteInspectTemplateRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for delete_inspect_template

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def pre_delete_job_trigger(self, request: dlp.DeleteJobTriggerRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[dlp.DeleteJobTriggerRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for delete_job_trigger

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def pre_delete_stored_info_type(self, request: dlp.DeleteStoredInfoTypeRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[dlp.DeleteStoredInfoTypeRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for delete_stored_info_type

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def pre_finish_dlp_job(self, request: dlp.FinishDlpJobRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[dlp.FinishDlpJobRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for finish_dlp_job

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def pre_get_deidentify_template(self, request: dlp.GetDeidentifyTemplateRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[dlp.GetDeidentifyTemplateRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for get_deidentify_template

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_get_deidentify_template(self, response: dlp.DeidentifyTemplate) -> dlp.DeidentifyTemplate:
        """Post-rpc interceptor for get_deidentify_template

        Override in a subclass to manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code.
        """
        return response
    def pre_get_dlp_job(self, request: dlp.GetDlpJobRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[dlp.GetDlpJobRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for get_dlp_job

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_get_dlp_job(self, response: dlp.DlpJob) -> dlp.DlpJob:
        """Post-rpc interceptor for get_dlp_job

        Override in a subclass to manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code.
        """
        return response
    def pre_get_inspect_template(self, request: dlp.GetInspectTemplateRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[dlp.GetInspectTemplateRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for get_inspect_template

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_get_inspect_template(self, response: dlp.InspectTemplate) -> dlp.InspectTemplate:
        """Post-rpc interceptor for get_inspect_template

        Override in a subclass to manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code.
        """
        return response
    def pre_get_job_trigger(self, request: dlp.GetJobTriggerRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[dlp.GetJobTriggerRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for get_job_trigger

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_get_job_trigger(self, response: dlp.JobTrigger) -> dlp.JobTrigger:
        """Post-rpc interceptor for get_job_trigger

        Override in a subclass to manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code.
        """
        return response
    def pre_get_stored_info_type(self, request: dlp.GetStoredInfoTypeRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[dlp.GetStoredInfoTypeRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for get_stored_info_type

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_get_stored_info_type(self, response: dlp.StoredInfoType) -> dlp.StoredInfoType:
        """Post-rpc interceptor for get_stored_info_type

        Override in a subclass to manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code.
        """
        return response
    def pre_hybrid_inspect_dlp_job(self, request: dlp.HybridInspectDlpJobRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[dlp.HybridInspectDlpJobRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for hybrid_inspect_dlp_job

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_hybrid_inspect_dlp_job(self, response: dlp.HybridInspectResponse) -> dlp.HybridInspectResponse:
        """Post-rpc interceptor for hybrid_inspect_dlp_job

        Override in a subclass to manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code.
        """
        return response
    def pre_hybrid_inspect_job_trigger(self, request: dlp.HybridInspectJobTriggerRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[dlp.HybridInspectJobTriggerRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for hybrid_inspect_job_trigger

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_hybrid_inspect_job_trigger(self, response: dlp.HybridInspectResponse) -> dlp.HybridInspectResponse:
        """Post-rpc interceptor for hybrid_inspect_job_trigger

        Override in a subclass to manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code.
        """
        return response
    def pre_inspect_content(self, request: dlp.InspectContentRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[dlp.InspectContentRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for inspect_content

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_inspect_content(self, response: dlp.InspectContentResponse) -> dlp.InspectContentResponse:
        """Post-rpc interceptor for inspect_content

        Override in a subclass to manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code.
        """
        return response
    def pre_list_deidentify_templates(self, request: dlp.ListDeidentifyTemplatesRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[dlp.ListDeidentifyTemplatesRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for list_deidentify_templates

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_list_deidentify_templates(self, response: dlp.ListDeidentifyTemplatesResponse) -> dlp.ListDeidentifyTemplatesResponse:
        """Post-rpc interceptor for list_deidentify_templates

        Override in a subclass to manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code.
        """
        return response
    def pre_list_dlp_jobs(self, request: dlp.ListDlpJobsRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[dlp.ListDlpJobsRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for list_dlp_jobs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_list_dlp_jobs(self, response: dlp.ListDlpJobsResponse) -> dlp.ListDlpJobsResponse:
        """Post-rpc interceptor for list_dlp_jobs

        Override in a subclass to manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code.
        """
        return response
    def pre_list_info_types(self, request: dlp.ListInfoTypesRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[dlp.ListInfoTypesRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for list_info_types

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_list_info_types(self, response: dlp.ListInfoTypesResponse) -> dlp.ListInfoTypesResponse:
        """Post-rpc interceptor for list_info_types

        Override in a subclass to manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code.
        """
        return response
    def pre_list_inspect_templates(self, request: dlp.ListInspectTemplatesRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[dlp.ListInspectTemplatesRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for list_inspect_templates

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_list_inspect_templates(self, response: dlp.ListInspectTemplatesResponse) -> dlp.ListInspectTemplatesResponse:
        """Post-rpc interceptor for list_inspect_templates

        Override in a subclass to manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code.
        """
        return response
    def pre_list_job_triggers(self, request: dlp.ListJobTriggersRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[dlp.ListJobTriggersRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for list_job_triggers

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_list_job_triggers(self, response: dlp.ListJobTriggersResponse) -> dlp.ListJobTriggersResponse:
        """Post-rpc interceptor for list_job_triggers

        Override in a subclass to manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code.
        """
        return response
    def pre_list_stored_info_types(self, request: dlp.ListStoredInfoTypesRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[dlp.ListStoredInfoTypesRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for list_stored_info_types

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_list_stored_info_types(self, response: dlp.ListStoredInfoTypesResponse) -> dlp.ListStoredInfoTypesResponse:
        """Post-rpc interceptor for list_stored_info_types

        Override in a subclass to manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code.
        """
        return response
    def pre_redact_image(self, request: dlp.RedactImageRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[dlp.RedactImageRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for redact_image

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_redact_image(self, response: dlp.RedactImageResponse) -> dlp.RedactImageResponse:
        """Post-rpc interceptor for redact_image

        Override in a subclass to manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code.
        """
        return response
    def pre_reidentify_content(self, request: dlp.ReidentifyContentRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[dlp.ReidentifyContentRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for reidentify_content

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_reidentify_content(self, response: dlp.ReidentifyContentResponse) -> dlp.ReidentifyContentResponse:
        """Post-rpc interceptor for reidentify_content

        Override in a subclass to manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code.
        """
        return response
    def pre_update_deidentify_template(self, request: dlp.UpdateDeidentifyTemplateRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[dlp.UpdateDeidentifyTemplateRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for update_deidentify_template

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_update_deidentify_template(self, response: dlp.DeidentifyTemplate) -> dlp.DeidentifyTemplate:
        """Post-rpc interceptor for update_deidentify_template

        Override in a subclass to manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code.
        """
        return response
    def pre_update_inspect_template(self, request: dlp.UpdateInspectTemplateRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[dlp.UpdateInspectTemplateRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for update_inspect_template

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_update_inspect_template(self, response: dlp.InspectTemplate) -> dlp.InspectTemplate:
        """Post-rpc interceptor for update_inspect_template

        Override in a subclass to manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code.
        """
        return response
    def pre_update_job_trigger(self, request: dlp.UpdateJobTriggerRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[dlp.UpdateJobTriggerRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for update_job_trigger

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_update_job_trigger(self, response: dlp.JobTrigger) -> dlp.JobTrigger:
        """Post-rpc interceptor for update_job_trigger

        Override in a subclass to manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code.
        """
        return response
    def pre_update_stored_info_type(self, request: dlp.UpdateStoredInfoTypeRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[dlp.UpdateStoredInfoTypeRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for update_stored_info_type

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_update_stored_info_type(self, response: dlp.StoredInfoType) -> dlp.StoredInfoType:
        """Post-rpc interceptor for update_stored_info_type

        Override in a subclass to manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class DlpServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: DlpServiceRestInterceptor


class DlpServiceRestTransport(DlpServiceTransport):
    """REST backend transport for DlpService.

    The Cloud Data Loss Prevention (DLP) API is a service that
    allows clients to detect the presence of Personally Identifiable
    Information (PII) and other privacy-sensitive data in
    user-supplied, unstructured data streams, like text blocks or
    images.
    The service also includes methods for sensitive data redaction
    and scheduling of data scans on Google Cloud Platform based data
    sets.
    To learn more about concepts and find how-to guides see
    https://cloud.google.com/dlp/docs/.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1

    """

    def __init__(self, *,
            host: str = 'dlp.googleapis.com',
            credentials: Optional[ga_credentials.Credentials] = None,
            credentials_file: Optional[str] = None,
            scopes: Optional[Sequence[str]] = None,
            client_cert_source_for_mtls: Optional[Callable[[
                ], Tuple[bytes, bytes]]] = None,
            quota_project_id: Optional[str] = None,
            client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
            always_use_jwt_access: Optional[bool] = False,
            url_scheme: str = 'https',
            interceptor: Optional[DlpServiceRestInterceptor] = None,
            api_audience: Optional[str] = None,
            ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.

            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional(Sequence[str])): A list of scopes. This argument is
                ignored if ``channel`` is provided.
            client_cert_source_for_mtls (Callable[[], Tuple[bytes, bytes]]): Client
                certificate to configure mutual TLS HTTP channel. It is ignored
                if ``channel`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you are developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.
            url_scheme: the protocol scheme for the API endpoint.  Normally
                "https", but for testing or local servers,
                "http" can be specified.
        """
        # Run the base constructor
        # TODO(yon-mg): resolve other ctor params i.e. scopes, quota, etc.
        # TODO: When custom host (api_endpoint) is set, `scopes` must *also* be set on the
        # credentials object
        maybe_url_match = re.match("^(?P<scheme>http(?:s)?://)?(?P<host>.*)$", host)
        if maybe_url_match is None:
            raise ValueError(f"Unexpected hostname structure: {host}")  # pragma: NO COVER

        url_match_items = maybe_url_match.groupdict()

        host = f"{url_scheme}://{host}" if not url_match_items["scheme"] else host

        super().__init__(
            host=host,
            credentials=credentials,
            client_info=client_info,
            always_use_jwt_access=always_use_jwt_access,
            api_audience=api_audience
        )
        self._session = AuthorizedSession(
            self._credentials, default_host=self.DEFAULT_HOST)
        if client_cert_source_for_mtls:
            self._session.configure_mtls_channel(client_cert_source_for_mtls)
        self._interceptor = interceptor or DlpServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _ActivateJobTrigger(DlpServiceRestStub):
        def __hash__(self):
            return hash("ActivateJobTrigger")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: dlp.ActivateJobTriggerRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> dlp.DlpJob:
            r"""Call the activate job trigger method over HTTP.

            Args:
                request (~.dlp.ActivateJobTriggerRequest):
                    The request object. Request message for
                ActivateJobTrigger.

                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.dlp.DlpJob:
                    Combines all of the information about
                a DLP job.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v2/{name=projects/*/jobTriggers/*}:activate',
                'body': '*',
            },
{
                'method': 'post',
                'uri': '/v2/{name=projects/*/locations/*/jobTriggers/*}:activate',
                'body': '*',
            },
            ]
            request, metadata = self._interceptor.pre_activate_job_trigger(request, metadata)
            pb_request = dlp.ActivateJobTriggerRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request['body'],
                including_default_value_fields=False,
                use_integers_for_enums=True
            )
            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dlp.DlpJob()
            pb_resp = dlp.DlpJob.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_activate_job_trigger(resp)
            return resp

    class _CancelDlpJob(DlpServiceRestStub):
        def __hash__(self):
            return hash("CancelDlpJob")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: dlp.CancelDlpJobRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ):
            r"""Call the cancel dlp job method over HTTP.

            Args:
                request (~.dlp.CancelDlpJobRequest):
                    The request object. The request message for canceling a
                DLP job.

                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.
            """

            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v2/{name=projects/*/dlpJobs/*}:cancel',
                'body': '*',
            },
{
                'method': 'post',
                'uri': '/v2/{name=projects/*/locations/*/dlpJobs/*}:cancel',
                'body': '*',
            },
            ]
            request, metadata = self._interceptor.pre_cancel_dlp_job(request, metadata)
            pb_request = dlp.CancelDlpJobRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request['body'],
                including_default_value_fields=False,
                use_integers_for_enums=True
            )
            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

    class _CreateDeidentifyTemplate(DlpServiceRestStub):
        def __hash__(self):
            return hash("CreateDeidentifyTemplate")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: dlp.CreateDeidentifyTemplateRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> dlp.DeidentifyTemplate:
            r"""Call the create deidentify
        template method over HTTP.

            Args:
                request (~.dlp.CreateDeidentifyTemplateRequest):
                    The request object. Request message for
                CreateDeidentifyTemplate.

                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.dlp.DeidentifyTemplate:
                    DeidentifyTemplates contains
                instructions on how to de-identify
                content. See
                https://cloud.google.com/dlp/docs/concepts-templates
                to learn more.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v2/{parent=organizations/*}/deidentifyTemplates',
                'body': '*',
            },
{
                'method': 'post',
                'uri': '/v2/{parent=organizations/*/locations/*}/deidentifyTemplates',
                'body': '*',
            },
{
                'method': 'post',
                'uri': '/v2/{parent=projects/*}/deidentifyTemplates',
                'body': '*',
            },
{
                'method': 'post',
                'uri': '/v2/{parent=projects/*/locations/*}/deidentifyTemplates',
                'body': '*',
            },
            ]
            request, metadata = self._interceptor.pre_create_deidentify_template(request, metadata)
            pb_request = dlp.CreateDeidentifyTemplateRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request['body'],
                including_default_value_fields=False,
                use_integers_for_enums=True
            )
            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dlp.DeidentifyTemplate()
            pb_resp = dlp.DeidentifyTemplate.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_create_deidentify_template(resp)
            return resp

    class _CreateDlpJob(DlpServiceRestStub):
        def __hash__(self):
            return hash("CreateDlpJob")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: dlp.CreateDlpJobRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> dlp.DlpJob:
            r"""Call the create dlp job method over HTTP.

            Args:
                request (~.dlp.CreateDlpJobRequest):
                    The request object. Request message for
                CreateDlpJobRequest. Used to initiate
                long running jobs such as calculating
                risk metrics or inspecting Google Cloud
                Storage.

                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.dlp.DlpJob:
                    Combines all of the information about
                a DLP job.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v2/{parent=projects/*}/dlpJobs',
                'body': '*',
            },
{
                'method': 'post',
                'uri': '/v2/{parent=projects/*/locations/*}/dlpJobs',
                'body': '*',
            },
            ]
            request, metadata = self._interceptor.pre_create_dlp_job(request, metadata)
            pb_request = dlp.CreateDlpJobRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request['body'],
                including_default_value_fields=False,
                use_integers_for_enums=True
            )
            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dlp.DlpJob()
            pb_resp = dlp.DlpJob.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_create_dlp_job(resp)
            return resp

    class _CreateInspectTemplate(DlpServiceRestStub):
        def __hash__(self):
            return hash("CreateInspectTemplate")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: dlp.CreateInspectTemplateRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> dlp.InspectTemplate:
            r"""Call the create inspect template method over HTTP.

            Args:
                request (~.dlp.CreateInspectTemplateRequest):
                    The request object. Request message for
                CreateInspectTemplate.

                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.dlp.InspectTemplate:
                    The inspectTemplate contains a
                configuration (set of types of sensitive
                data to be detected) to be used anywhere
                you otherwise would normally specify
                InspectConfig. See
                https://cloud.google.com/dlp/docs/concepts-templates
                to learn more.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v2/{parent=organizations/*}/inspectTemplates',
                'body': '*',
            },
{
                'method': 'post',
                'uri': '/v2/{parent=organizations/*/locations/*}/inspectTemplates',
                'body': '*',
            },
{
                'method': 'post',
                'uri': '/v2/{parent=projects/*}/inspectTemplates',
                'body': '*',
            },
{
                'method': 'post',
                'uri': '/v2/{parent=projects/*/locations/*}/inspectTemplates',
                'body': '*',
            },
            ]
            request, metadata = self._interceptor.pre_create_inspect_template(request, metadata)
            pb_request = dlp.CreateInspectTemplateRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request['body'],
                including_default_value_fields=False,
                use_integers_for_enums=True
            )
            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dlp.InspectTemplate()
            pb_resp = dlp.InspectTemplate.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_create_inspect_template(resp)
            return resp

    class _CreateJobTrigger(DlpServiceRestStub):
        def __hash__(self):
            return hash("CreateJobTrigger")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: dlp.CreateJobTriggerRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> dlp.JobTrigger:
            r"""Call the create job trigger method over HTTP.

            Args:
                request (~.dlp.CreateJobTriggerRequest):
                    The request object. Request message for CreateJobTrigger.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.dlp.JobTrigger:
                    Contains a configuration to make dlp
                api calls on a repeating basis. See
                https://cloud.google.com/dlp/docs/concepts-job-triggers
                to learn more.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v2/{parent=projects/*}/jobTriggers',
                'body': '*',
            },
{
                'method': 'post',
                'uri': '/v2/{parent=projects/*/locations/*}/jobTriggers',
                'body': '*',
            },
{
                'method': 'post',
                'uri': '/v2/{parent=organizations/*/locations/*}/jobTriggers',
                'body': '*',
            },
            ]
            request, metadata = self._interceptor.pre_create_job_trigger(request, metadata)
            pb_request = dlp.CreateJobTriggerRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request['body'],
                including_default_value_fields=False,
                use_integers_for_enums=True
            )
            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dlp.JobTrigger()
            pb_resp = dlp.JobTrigger.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_create_job_trigger(resp)
            return resp

    class _CreateStoredInfoType(DlpServiceRestStub):
        def __hash__(self):
            return hash("CreateStoredInfoType")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: dlp.CreateStoredInfoTypeRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> dlp.StoredInfoType:
            r"""Call the create stored info type method over HTTP.

            Args:
                request (~.dlp.CreateStoredInfoTypeRequest):
                    The request object. Request message for
                CreateStoredInfoType.

                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.dlp.StoredInfoType:
                    StoredInfoType resource message that
                contains information about the current
                version and any pending updates.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v2/{parent=organizations/*}/storedInfoTypes',
                'body': '*',
            },
{
                'method': 'post',
                'uri': '/v2/{parent=organizations/*/locations/*}/storedInfoTypes',
                'body': '*',
            },
{
                'method': 'post',
                'uri': '/v2/{parent=projects/*}/storedInfoTypes',
                'body': '*',
            },
{
                'method': 'post',
                'uri': '/v2/{parent=projects/*/locations/*}/storedInfoTypes',
                'body': '*',
            },
            ]
            request, metadata = self._interceptor.pre_create_stored_info_type(request, metadata)
            pb_request = dlp.CreateStoredInfoTypeRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request['body'],
                including_default_value_fields=False,
                use_integers_for_enums=True
            )
            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dlp.StoredInfoType()
            pb_resp = dlp.StoredInfoType.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_create_stored_info_type(resp)
            return resp

    class _DeidentifyContent(DlpServiceRestStub):
        def __hash__(self):
            return hash("DeidentifyContent")

        def __call__(self,
                request: dlp.DeidentifyContentRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> dlp.DeidentifyContentResponse:
            r"""Call the deidentify content method over HTTP.

            Args:
                request (~.dlp.DeidentifyContentRequest):
                    The request object. Request to de-identify a ContentItem.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.dlp.DeidentifyContentResponse:
                    Results of de-identifying a
                ContentItem.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v2/{parent=projects/*}/content:deidentify',
                'body': '*',
            },
{
                'method': 'post',
                'uri': '/v2/{parent=projects/*/locations/*}/content:deidentify',
                'body': '*',
            },
            ]
            request, metadata = self._interceptor.pre_deidentify_content(request, metadata)
            pb_request = dlp.DeidentifyContentRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request['body'],
                including_default_value_fields=False,
                use_integers_for_enums=True
            )
            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dlp.DeidentifyContentResponse()
            pb_resp = dlp.DeidentifyContentResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_deidentify_content(resp)
            return resp

    class _DeleteDeidentifyTemplate(DlpServiceRestStub):
        def __hash__(self):
            return hash("DeleteDeidentifyTemplate")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: dlp.DeleteDeidentifyTemplateRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ):
            r"""Call the delete deidentify
        template method over HTTP.

            Args:
                request (~.dlp.DeleteDeidentifyTemplateRequest):
                    The request object. Request message for
                DeleteDeidentifyTemplate.

                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.
            """

            http_options: List[Dict[str, str]] = [{
                'method': 'delete',
                'uri': '/v2/{name=organizations/*/deidentifyTemplates/*}',
            },
{
                'method': 'delete',
                'uri': '/v2/{name=organizations/*/locations/*/deidentifyTemplates/*}',
            },
{
                'method': 'delete',
                'uri': '/v2/{name=projects/*/deidentifyTemplates/*}',
            },
{
                'method': 'delete',
                'uri': '/v2/{name=projects/*/locations/*/deidentifyTemplates/*}',
            },
            ]
            request, metadata = self._interceptor.pre_delete_deidentify_template(request, metadata)
            pb_request = dlp.DeleteDeidentifyTemplateRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

    class _DeleteDlpJob(DlpServiceRestStub):
        def __hash__(self):
            return hash("DeleteDlpJob")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: dlp.DeleteDlpJobRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ):
            r"""Call the delete dlp job method over HTTP.

            Args:
                request (~.dlp.DeleteDlpJobRequest):
                    The request object. The request message for deleting a
                DLP job.

                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.
            """

            http_options: List[Dict[str, str]] = [{
                'method': 'delete',
                'uri': '/v2/{name=projects/*/dlpJobs/*}',
            },
{
                'method': 'delete',
                'uri': '/v2/{name=projects/*/locations/*/dlpJobs/*}',
            },
            ]
            request, metadata = self._interceptor.pre_delete_dlp_job(request, metadata)
            pb_request = dlp.DeleteDlpJobRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

    class _DeleteInspectTemplate(DlpServiceRestStub):
        def __hash__(self):
            return hash("DeleteInspectTemplate")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: dlp.DeleteInspectTemplateRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ):
            r"""Call the delete inspect template method over HTTP.

            Args:
                request (~.dlp.DeleteInspectTemplateRequest):
                    The request object. Request message for
                DeleteInspectTemplate.

                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.
            """

            http_options: List[Dict[str, str]] = [{
                'method': 'delete',
                'uri': '/v2/{name=organizations/*/inspectTemplates/*}',
            },
{
                'method': 'delete',
                'uri': '/v2/{name=organizations/*/locations/*/inspectTemplates/*}',
            },
{
                'method': 'delete',
                'uri': '/v2/{name=projects/*/inspectTemplates/*}',
            },
{
                'method': 'delete',
                'uri': '/v2/{name=projects/*/locations/*/inspectTemplates/*}',
            },
            ]
            request, metadata = self._interceptor.pre_delete_inspect_template(request, metadata)
            pb_request = dlp.DeleteInspectTemplateRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

    class _DeleteJobTrigger(DlpServiceRestStub):
        def __hash__(self):
            return hash("DeleteJobTrigger")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: dlp.DeleteJobTriggerRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ):
            r"""Call the delete job trigger method over HTTP.

            Args:
                request (~.dlp.DeleteJobTriggerRequest):
                    The request object. Request message for DeleteJobTrigger.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.
            """

            http_options: List[Dict[str, str]] = [{
                'method': 'delete',
                'uri': '/v2/{name=projects/*/jobTriggers/*}',
            },
{
                'method': 'delete',
                'uri': '/v2/{name=projects/*/locations/*/jobTriggers/*}',
            },
{
                'method': 'delete',
                'uri': '/v2/{name=organizations/*/locations/*/jobTriggers/*}',
            },
            ]
            request, metadata = self._interceptor.pre_delete_job_trigger(request, metadata)
            pb_request = dlp.DeleteJobTriggerRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

    class _DeleteStoredInfoType(DlpServiceRestStub):
        def __hash__(self):
            return hash("DeleteStoredInfoType")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: dlp.DeleteStoredInfoTypeRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ):
            r"""Call the delete stored info type method over HTTP.

            Args:
                request (~.dlp.DeleteStoredInfoTypeRequest):
                    The request object. Request message for
                DeleteStoredInfoType.

                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.
            """

            http_options: List[Dict[str, str]] = [{
                'method': 'delete',
                'uri': '/v2/{name=organizations/*/storedInfoTypes/*}',
            },
{
                'method': 'delete',
                'uri': '/v2/{name=organizations/*/locations/*/storedInfoTypes/*}',
            },
{
                'method': 'delete',
                'uri': '/v2/{name=projects/*/storedInfoTypes/*}',
            },
{
                'method': 'delete',
                'uri': '/v2/{name=projects/*/locations/*/storedInfoTypes/*}',
            },
            ]
            request, metadata = self._interceptor.pre_delete_stored_info_type(request, metadata)
            pb_request = dlp.DeleteStoredInfoTypeRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

    class _FinishDlpJob(DlpServiceRestStub):
        def __hash__(self):
            return hash("FinishDlpJob")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: dlp.FinishDlpJobRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ):
            r"""Call the finish dlp job method over HTTP.

            Args:
                request (~.dlp.FinishDlpJobRequest):
                    The request object. The request message for finishing a
                DLP hybrid job.

                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.
            """

            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v2/{name=projects/*/locations/*/dlpJobs/*}:finish',
                'body': '*',
            },
            ]
            request, metadata = self._interceptor.pre_finish_dlp_job(request, metadata)
            pb_request = dlp.FinishDlpJobRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request['body'],
                including_default_value_fields=False,
                use_integers_for_enums=True
            )
            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

    class _GetDeidentifyTemplate(DlpServiceRestStub):
        def __hash__(self):
            return hash("GetDeidentifyTemplate")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: dlp.GetDeidentifyTemplateRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> dlp.DeidentifyTemplate:
            r"""Call the get deidentify template method over HTTP.

            Args:
                request (~.dlp.GetDeidentifyTemplateRequest):
                    The request object. Request message for
                GetDeidentifyTemplate.

                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.dlp.DeidentifyTemplate:
                    DeidentifyTemplates contains
                instructions on how to de-identify
                content. See
                https://cloud.google.com/dlp/docs/concepts-templates
                to learn more.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v2/{name=organizations/*/deidentifyTemplates/*}',
            },
{
                'method': 'get',
                'uri': '/v2/{name=organizations/*/locations/*/deidentifyTemplates/*}',
            },
{
                'method': 'get',
                'uri': '/v2/{name=projects/*/deidentifyTemplates/*}',
            },
{
                'method': 'get',
                'uri': '/v2/{name=projects/*/locations/*/deidentifyTemplates/*}',
            },
            ]
            request, metadata = self._interceptor.pre_get_deidentify_template(request, metadata)
            pb_request = dlp.GetDeidentifyTemplateRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dlp.DeidentifyTemplate()
            pb_resp = dlp.DeidentifyTemplate.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_get_deidentify_template(resp)
            return resp

    class _GetDlpJob(DlpServiceRestStub):
        def __hash__(self):
            return hash("GetDlpJob")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: dlp.GetDlpJobRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> dlp.DlpJob:
            r"""Call the get dlp job method over HTTP.

            Args:
                request (~.dlp.GetDlpJobRequest):
                    The request object. The request message for [DlpJobs.GetDlpJob][].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.dlp.DlpJob:
                    Combines all of the information about
                a DLP job.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v2/{name=projects/*/dlpJobs/*}',
            },
{
                'method': 'get',
                'uri': '/v2/{name=projects/*/locations/*/dlpJobs/*}',
            },
            ]
            request, metadata = self._interceptor.pre_get_dlp_job(request, metadata)
            pb_request = dlp.GetDlpJobRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dlp.DlpJob()
            pb_resp = dlp.DlpJob.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_get_dlp_job(resp)
            return resp

    class _GetInspectTemplate(DlpServiceRestStub):
        def __hash__(self):
            return hash("GetInspectTemplate")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: dlp.GetInspectTemplateRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> dlp.InspectTemplate:
            r"""Call the get inspect template method over HTTP.

            Args:
                request (~.dlp.GetInspectTemplateRequest):
                    The request object. Request message for
                GetInspectTemplate.

                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.dlp.InspectTemplate:
                    The inspectTemplate contains a
                configuration (set of types of sensitive
                data to be detected) to be used anywhere
                you otherwise would normally specify
                InspectConfig. See
                https://cloud.google.com/dlp/docs/concepts-templates
                to learn more.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v2/{name=organizations/*/inspectTemplates/*}',
            },
{
                'method': 'get',
                'uri': '/v2/{name=organizations/*/locations/*/inspectTemplates/*}',
            },
{
                'method': 'get',
                'uri': '/v2/{name=projects/*/inspectTemplates/*}',
            },
{
                'method': 'get',
                'uri': '/v2/{name=projects/*/locations/*/inspectTemplates/*}',
            },
            ]
            request, metadata = self._interceptor.pre_get_inspect_template(request, metadata)
            pb_request = dlp.GetInspectTemplateRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dlp.InspectTemplate()
            pb_resp = dlp.InspectTemplate.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_get_inspect_template(resp)
            return resp

    class _GetJobTrigger(DlpServiceRestStub):
        def __hash__(self):
            return hash("GetJobTrigger")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: dlp.GetJobTriggerRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> dlp.JobTrigger:
            r"""Call the get job trigger method over HTTP.

            Args:
                request (~.dlp.GetJobTriggerRequest):
                    The request object. Request message for GetJobTrigger.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.dlp.JobTrigger:
                    Contains a configuration to make dlp
                api calls on a repeating basis. See
                https://cloud.google.com/dlp/docs/concepts-job-triggers
                to learn more.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v2/{name=projects/*/jobTriggers/*}',
            },
{
                'method': 'get',
                'uri': '/v2/{name=projects/*/locations/*/jobTriggers/*}',
            },
{
                'method': 'get',
                'uri': '/v2/{name=organizations/*/locations/*/jobTriggers/*}',
            },
            ]
            request, metadata = self._interceptor.pre_get_job_trigger(request, metadata)
            pb_request = dlp.GetJobTriggerRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dlp.JobTrigger()
            pb_resp = dlp.JobTrigger.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_get_job_trigger(resp)
            return resp

    class _GetStoredInfoType(DlpServiceRestStub):
        def __hash__(self):
            return hash("GetStoredInfoType")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: dlp.GetStoredInfoTypeRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> dlp.StoredInfoType:
            r"""Call the get stored info type method over HTTP.

            Args:
                request (~.dlp.GetStoredInfoTypeRequest):
                    The request object. Request message for
                GetStoredInfoType.

                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.dlp.StoredInfoType:
                    StoredInfoType resource message that
                contains information about the current
                version and any pending updates.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v2/{name=organizations/*/storedInfoTypes/*}',
            },
{
                'method': 'get',
                'uri': '/v2/{name=organizations/*/locations/*/storedInfoTypes/*}',
            },
{
                'method': 'get',
                'uri': '/v2/{name=projects/*/storedInfoTypes/*}',
            },
{
                'method': 'get',
                'uri': '/v2/{name=projects/*/locations/*/storedInfoTypes/*}',
            },
            ]
            request, metadata = self._interceptor.pre_get_stored_info_type(request, metadata)
            pb_request = dlp.GetStoredInfoTypeRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dlp.StoredInfoType()
            pb_resp = dlp.StoredInfoType.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_get_stored_info_type(resp)
            return resp

    class _HybridInspectDlpJob(DlpServiceRestStub):
        def __hash__(self):
            return hash("HybridInspectDlpJob")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: dlp.HybridInspectDlpJobRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> dlp.HybridInspectResponse:
            r"""Call the hybrid inspect dlp job method over HTTP.

            Args:
                request (~.dlp.HybridInspectDlpJobRequest):
                    The request object. Request to search for potentially
                sensitive info in a custom location.

                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.dlp.HybridInspectResponse:
                    Quota exceeded errors will be thrown
                once quota has been met.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v2/{name=projects/*/locations/*/dlpJobs/*}:hybridInspect',
                'body': '*',
            },
            ]
            request, metadata = self._interceptor.pre_hybrid_inspect_dlp_job(request, metadata)
            pb_request = dlp.HybridInspectDlpJobRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request['body'],
                including_default_value_fields=False,
                use_integers_for_enums=True
            )
            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dlp.HybridInspectResponse()
            pb_resp = dlp.HybridInspectResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_hybrid_inspect_dlp_job(resp)
            return resp

    class _HybridInspectJobTrigger(DlpServiceRestStub):
        def __hash__(self):
            return hash("HybridInspectJobTrigger")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: dlp.HybridInspectJobTriggerRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> dlp.HybridInspectResponse:
            r"""Call the hybrid inspect job
        trigger method over HTTP.

            Args:
                request (~.dlp.HybridInspectJobTriggerRequest):
                    The request object. Request to search for potentially
                sensitive info in a custom location.

                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.dlp.HybridInspectResponse:
                    Quota exceeded errors will be thrown
                once quota has been met.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v2/{name=projects/*/locations/*/jobTriggers/*}:hybridInspect',
                'body': '*',
            },
            ]
            request, metadata = self._interceptor.pre_hybrid_inspect_job_trigger(request, metadata)
            pb_request = dlp.HybridInspectJobTriggerRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request['body'],
                including_default_value_fields=False,
                use_integers_for_enums=True
            )
            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dlp.HybridInspectResponse()
            pb_resp = dlp.HybridInspectResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_hybrid_inspect_job_trigger(resp)
            return resp

    class _InspectContent(DlpServiceRestStub):
        def __hash__(self):
            return hash("InspectContent")

        def __call__(self,
                request: dlp.InspectContentRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> dlp.InspectContentResponse:
            r"""Call the inspect content method over HTTP.

            Args:
                request (~.dlp.InspectContentRequest):
                    The request object. Request to search for potentially
                sensitive info in a ContentItem.

                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.dlp.InspectContentResponse:
                    Results of inspecting an item.
            """

            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v2/{parent=projects/*}/content:inspect',
                'body': '*',
            },
{
                'method': 'post',
                'uri': '/v2/{parent=projects/*/locations/*}/content:inspect',
                'body': '*',
            },
            ]
            request, metadata = self._interceptor.pre_inspect_content(request, metadata)
            pb_request = dlp.InspectContentRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request['body'],
                including_default_value_fields=False,
                use_integers_for_enums=True
            )
            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dlp.InspectContentResponse()
            pb_resp = dlp.InspectContentResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_inspect_content(resp)
            return resp

    class _ListDeidentifyTemplates(DlpServiceRestStub):
        def __hash__(self):
            return hash("ListDeidentifyTemplates")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: dlp.ListDeidentifyTemplatesRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> dlp.ListDeidentifyTemplatesResponse:
            r"""Call the list deidentify templates method over HTTP.

            Args:
                request (~.dlp.ListDeidentifyTemplatesRequest):
                    The request object. Request message for
                ListDeidentifyTemplates.

                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.dlp.ListDeidentifyTemplatesResponse:
                    Response message for
                ListDeidentifyTemplates.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v2/{parent=organizations/*}/deidentifyTemplates',
            },
{
                'method': 'get',
                'uri': '/v2/{parent=organizations/*/locations/*}/deidentifyTemplates',
            },
{
                'method': 'get',
                'uri': '/v2/{parent=projects/*}/deidentifyTemplates',
            },
{
                'method': 'get',
                'uri': '/v2/{parent=projects/*/locations/*}/deidentifyTemplates',
            },
            ]
            request, metadata = self._interceptor.pre_list_deidentify_templates(request, metadata)
            pb_request = dlp.ListDeidentifyTemplatesRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dlp.ListDeidentifyTemplatesResponse()
            pb_resp = dlp.ListDeidentifyTemplatesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_list_deidentify_templates(resp)
            return resp

    class _ListDlpJobs(DlpServiceRestStub):
        def __hash__(self):
            return hash("ListDlpJobs")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: dlp.ListDlpJobsRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> dlp.ListDlpJobsResponse:
            r"""Call the list dlp jobs method over HTTP.

            Args:
                request (~.dlp.ListDlpJobsRequest):
                    The request object. The request message for listing DLP
                jobs.

                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.dlp.ListDlpJobsResponse:
                    The response message for listing DLP
                jobs.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v2/{parent=projects/*}/dlpJobs',
            },
{
                'method': 'get',
                'uri': '/v2/{parent=projects/*/locations/*}/dlpJobs',
            },
{
                'method': 'get',
                'uri': '/v2/{parent=organizations/*/locations/*}/dlpJobs',
            },
            ]
            request, metadata = self._interceptor.pre_list_dlp_jobs(request, metadata)
            pb_request = dlp.ListDlpJobsRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dlp.ListDlpJobsResponse()
            pb_resp = dlp.ListDlpJobsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_list_dlp_jobs(resp)
            return resp

    class _ListInfoTypes(DlpServiceRestStub):
        def __hash__(self):
            return hash("ListInfoTypes")

        def __call__(self,
                request: dlp.ListInfoTypesRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> dlp.ListInfoTypesResponse:
            r"""Call the list info types method over HTTP.

            Args:
                request (~.dlp.ListInfoTypesRequest):
                    The request object. Request for the list of infoTypes.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.dlp.ListInfoTypesResponse:
                    Response to the ListInfoTypes
                request.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v2/infoTypes',
            },
{
                'method': 'get',
                'uri': '/v2/{parent=locations/*}/infoTypes',
            },
            ]
            request, metadata = self._interceptor.pre_list_info_types(request, metadata)
            pb_request = dlp.ListInfoTypesRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dlp.ListInfoTypesResponse()
            pb_resp = dlp.ListInfoTypesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_list_info_types(resp)
            return resp

    class _ListInspectTemplates(DlpServiceRestStub):
        def __hash__(self):
            return hash("ListInspectTemplates")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: dlp.ListInspectTemplatesRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> dlp.ListInspectTemplatesResponse:
            r"""Call the list inspect templates method over HTTP.

            Args:
                request (~.dlp.ListInspectTemplatesRequest):
                    The request object. Request message for
                ListInspectTemplates.

                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.dlp.ListInspectTemplatesResponse:
                    Response message for
                ListInspectTemplates.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v2/{parent=organizations/*}/inspectTemplates',
            },
{
                'method': 'get',
                'uri': '/v2/{parent=organizations/*/locations/*}/inspectTemplates',
            },
{
                'method': 'get',
                'uri': '/v2/{parent=projects/*}/inspectTemplates',
            },
{
                'method': 'get',
                'uri': '/v2/{parent=projects/*/locations/*}/inspectTemplates',
            },
            ]
            request, metadata = self._interceptor.pre_list_inspect_templates(request, metadata)
            pb_request = dlp.ListInspectTemplatesRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dlp.ListInspectTemplatesResponse()
            pb_resp = dlp.ListInspectTemplatesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_list_inspect_templates(resp)
            return resp

    class _ListJobTriggers(DlpServiceRestStub):
        def __hash__(self):
            return hash("ListJobTriggers")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: dlp.ListJobTriggersRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> dlp.ListJobTriggersResponse:
            r"""Call the list job triggers method over HTTP.

            Args:
                request (~.dlp.ListJobTriggersRequest):
                    The request object. Request message for ListJobTriggers.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.dlp.ListJobTriggersResponse:
                    Response message for ListJobTriggers.
            """

            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v2/{parent=projects/*}/jobTriggers',
            },
{
                'method': 'get',
                'uri': '/v2/{parent=projects/*/locations/*}/jobTriggers',
            },
{
                'method': 'get',
                'uri': '/v2/{parent=organizations/*/locations/*}/jobTriggers',
            },
            ]
            request, metadata = self._interceptor.pre_list_job_triggers(request, metadata)
            pb_request = dlp.ListJobTriggersRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dlp.ListJobTriggersResponse()
            pb_resp = dlp.ListJobTriggersResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_list_job_triggers(resp)
            return resp

    class _ListStoredInfoTypes(DlpServiceRestStub):
        def __hash__(self):
            return hash("ListStoredInfoTypes")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: dlp.ListStoredInfoTypesRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> dlp.ListStoredInfoTypesResponse:
            r"""Call the list stored info types method over HTTP.

            Args:
                request (~.dlp.ListStoredInfoTypesRequest):
                    The request object. Request message for
                ListStoredInfoTypes.

                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.dlp.ListStoredInfoTypesResponse:
                    Response message for
                ListStoredInfoTypes.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v2/{parent=organizations/*}/storedInfoTypes',
            },
{
                'method': 'get',
                'uri': '/v2/{parent=organizations/*/locations/*}/storedInfoTypes',
            },
{
                'method': 'get',
                'uri': '/v2/{parent=projects/*}/storedInfoTypes',
            },
{
                'method': 'get',
                'uri': '/v2/{parent=projects/*/locations/*}/storedInfoTypes',
            },
            ]
            request, metadata = self._interceptor.pre_list_stored_info_types(request, metadata)
            pb_request = dlp.ListStoredInfoTypesRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dlp.ListStoredInfoTypesResponse()
            pb_resp = dlp.ListStoredInfoTypesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_list_stored_info_types(resp)
            return resp

    class _RedactImage(DlpServiceRestStub):
        def __hash__(self):
            return hash("RedactImage")

        def __call__(self,
                request: dlp.RedactImageRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> dlp.RedactImageResponse:
            r"""Call the redact image method over HTTP.

            Args:
                request (~.dlp.RedactImageRequest):
                    The request object. Request to search for potentially
                sensitive info in an image and redact it
                by covering it with a colored rectangle.

                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.dlp.RedactImageResponse:
                    Results of redacting an image.
            """

            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v2/{parent=projects/*}/image:redact',
                'body': '*',
            },
{
                'method': 'post',
                'uri': '/v2/{parent=projects/*/locations/*}/image:redact',
                'body': '*',
            },
            ]
            request, metadata = self._interceptor.pre_redact_image(request, metadata)
            pb_request = dlp.RedactImageRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request['body'],
                including_default_value_fields=False,
                use_integers_for_enums=True
            )
            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dlp.RedactImageResponse()
            pb_resp = dlp.RedactImageResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_redact_image(resp)
            return resp

    class _ReidentifyContent(DlpServiceRestStub):
        def __hash__(self):
            return hash("ReidentifyContent")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: dlp.ReidentifyContentRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> dlp.ReidentifyContentResponse:
            r"""Call the reidentify content method over HTTP.

            Args:
                request (~.dlp.ReidentifyContentRequest):
                    The request object. Request to re-identify an item.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.dlp.ReidentifyContentResponse:
                    Results of re-identifying an item.
            """

            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v2/{parent=projects/*}/content:reidentify',
                'body': '*',
            },
{
                'method': 'post',
                'uri': '/v2/{parent=projects/*/locations/*}/content:reidentify',
                'body': '*',
            },
            ]
            request, metadata = self._interceptor.pre_reidentify_content(request, metadata)
            pb_request = dlp.ReidentifyContentRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request['body'],
                including_default_value_fields=False,
                use_integers_for_enums=True
            )
            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dlp.ReidentifyContentResponse()
            pb_resp = dlp.ReidentifyContentResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_reidentify_content(resp)
            return resp

    class _UpdateDeidentifyTemplate(DlpServiceRestStub):
        def __hash__(self):
            return hash("UpdateDeidentifyTemplate")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: dlp.UpdateDeidentifyTemplateRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> dlp.DeidentifyTemplate:
            r"""Call the update deidentify
        template method over HTTP.

            Args:
                request (~.dlp.UpdateDeidentifyTemplateRequest):
                    The request object. Request message for
                UpdateDeidentifyTemplate.

                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.dlp.DeidentifyTemplate:
                    DeidentifyTemplates contains
                instructions on how to de-identify
                content. See
                https://cloud.google.com/dlp/docs/concepts-templates
                to learn more.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'patch',
                'uri': '/v2/{name=organizations/*/deidentifyTemplates/*}',
                'body': '*',
            },
{
                'method': 'patch',
                'uri': '/v2/{name=organizations/*/locations/*/deidentifyTemplates/*}',
                'body': '*',
            },
{
                'method': 'patch',
                'uri': '/v2/{name=projects/*/deidentifyTemplates/*}',
                'body': '*',
            },
{
                'method': 'patch',
                'uri': '/v2/{name=projects/*/locations/*/deidentifyTemplates/*}',
                'body': '*',
            },
            ]
            request, metadata = self._interceptor.pre_update_deidentify_template(request, metadata)
            pb_request = dlp.UpdateDeidentifyTemplateRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request['body'],
                including_default_value_fields=False,
                use_integers_for_enums=True
            )
            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dlp.DeidentifyTemplate()
            pb_resp = dlp.DeidentifyTemplate.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_update_deidentify_template(resp)
            return resp

    class _UpdateInspectTemplate(DlpServiceRestStub):
        def __hash__(self):
            return hash("UpdateInspectTemplate")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: dlp.UpdateInspectTemplateRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> dlp.InspectTemplate:
            r"""Call the update inspect template method over HTTP.

            Args:
                request (~.dlp.UpdateInspectTemplateRequest):
                    The request object. Request message for
                UpdateInspectTemplate.

                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.dlp.InspectTemplate:
                    The inspectTemplate contains a
                configuration (set of types of sensitive
                data to be detected) to be used anywhere
                you otherwise would normally specify
                InspectConfig. See
                https://cloud.google.com/dlp/docs/concepts-templates
                to learn more.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'patch',
                'uri': '/v2/{name=organizations/*/inspectTemplates/*}',
                'body': '*',
            },
{
                'method': 'patch',
                'uri': '/v2/{name=organizations/*/locations/*/inspectTemplates/*}',
                'body': '*',
            },
{
                'method': 'patch',
                'uri': '/v2/{name=projects/*/inspectTemplates/*}',
                'body': '*',
            },
{
                'method': 'patch',
                'uri': '/v2/{name=projects/*/locations/*/inspectTemplates/*}',
                'body': '*',
            },
            ]
            request, metadata = self._interceptor.pre_update_inspect_template(request, metadata)
            pb_request = dlp.UpdateInspectTemplateRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request['body'],
                including_default_value_fields=False,
                use_integers_for_enums=True
            )
            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dlp.InspectTemplate()
            pb_resp = dlp.InspectTemplate.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_update_inspect_template(resp)
            return resp

    class _UpdateJobTrigger(DlpServiceRestStub):
        def __hash__(self):
            return hash("UpdateJobTrigger")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: dlp.UpdateJobTriggerRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> dlp.JobTrigger:
            r"""Call the update job trigger method over HTTP.

            Args:
                request (~.dlp.UpdateJobTriggerRequest):
                    The request object. Request message for UpdateJobTrigger.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.dlp.JobTrigger:
                    Contains a configuration to make dlp
                api calls on a repeating basis. See
                https://cloud.google.com/dlp/docs/concepts-job-triggers
                to learn more.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'patch',
                'uri': '/v2/{name=projects/*/jobTriggers/*}',
                'body': '*',
            },
{
                'method': 'patch',
                'uri': '/v2/{name=projects/*/locations/*/jobTriggers/*}',
                'body': '*',
            },
{
                'method': 'patch',
                'uri': '/v2/{name=organizations/*/locations/*/jobTriggers/*}',
                'body': '*',
            },
            ]
            request, metadata = self._interceptor.pre_update_job_trigger(request, metadata)
            pb_request = dlp.UpdateJobTriggerRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request['body'],
                including_default_value_fields=False,
                use_integers_for_enums=True
            )
            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dlp.JobTrigger()
            pb_resp = dlp.JobTrigger.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_update_job_trigger(resp)
            return resp

    class _UpdateStoredInfoType(DlpServiceRestStub):
        def __hash__(self):
            return hash("UpdateStoredInfoType")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: dlp.UpdateStoredInfoTypeRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> dlp.StoredInfoType:
            r"""Call the update stored info type method over HTTP.

            Args:
                request (~.dlp.UpdateStoredInfoTypeRequest):
                    The request object. Request message for
                UpdateStoredInfoType.

                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.dlp.StoredInfoType:
                    StoredInfoType resource message that
                contains information about the current
                version and any pending updates.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'patch',
                'uri': '/v2/{name=organizations/*/storedInfoTypes/*}',
                'body': '*',
            },
{
                'method': 'patch',
                'uri': '/v2/{name=organizations/*/locations/*/storedInfoTypes/*}',
                'body': '*',
            },
{
                'method': 'patch',
                'uri': '/v2/{name=projects/*/storedInfoTypes/*}',
                'body': '*',
            },
{
                'method': 'patch',
                'uri': '/v2/{name=projects/*/locations/*/storedInfoTypes/*}',
                'body': '*',
            },
            ]
            request, metadata = self._interceptor.pre_update_stored_info_type(request, metadata)
            pb_request = dlp.UpdateStoredInfoTypeRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request['body'],
                including_default_value_fields=False,
                use_integers_for_enums=True
            )
            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dlp.StoredInfoType()
            pb_resp = dlp.StoredInfoType.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_update_stored_info_type(resp)
            return resp

    @property
    def activate_job_trigger(self) -> Callable[
            [dlp.ActivateJobTriggerRequest],
            dlp.DlpJob]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ActivateJobTrigger(self._session, self._host, self._interceptor) # type: ignore

    @property
    def cancel_dlp_job(self) -> Callable[
            [dlp.CancelDlpJobRequest],
            empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CancelDlpJob(self._session, self._host, self._interceptor) # type: ignore

    @property
    def create_deidentify_template(self) -> Callable[
            [dlp.CreateDeidentifyTemplateRequest],
            dlp.DeidentifyTemplate]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateDeidentifyTemplate(self._session, self._host, self._interceptor) # type: ignore

    @property
    def create_dlp_job(self) -> Callable[
            [dlp.CreateDlpJobRequest],
            dlp.DlpJob]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateDlpJob(self._session, self._host, self._interceptor) # type: ignore

    @property
    def create_inspect_template(self) -> Callable[
            [dlp.CreateInspectTemplateRequest],
            dlp.InspectTemplate]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateInspectTemplate(self._session, self._host, self._interceptor) # type: ignore

    @property
    def create_job_trigger(self) -> Callable[
            [dlp.CreateJobTriggerRequest],
            dlp.JobTrigger]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateJobTrigger(self._session, self._host, self._interceptor) # type: ignore

    @property
    def create_stored_info_type(self) -> Callable[
            [dlp.CreateStoredInfoTypeRequest],
            dlp.StoredInfoType]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateStoredInfoType(self._session, self._host, self._interceptor) # type: ignore

    @property
    def deidentify_content(self) -> Callable[
            [dlp.DeidentifyContentRequest],
            dlp.DeidentifyContentResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeidentifyContent(self._session, self._host, self._interceptor) # type: ignore

    @property
    def delete_deidentify_template(self) -> Callable[
            [dlp.DeleteDeidentifyTemplateRequest],
            empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteDeidentifyTemplate(self._session, self._host, self._interceptor) # type: ignore

    @property
    def delete_dlp_job(self) -> Callable[
            [dlp.DeleteDlpJobRequest],
            empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteDlpJob(self._session, self._host, self._interceptor) # type: ignore

    @property
    def delete_inspect_template(self) -> Callable[
            [dlp.DeleteInspectTemplateRequest],
            empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteInspectTemplate(self._session, self._host, self._interceptor) # type: ignore

    @property
    def delete_job_trigger(self) -> Callable[
            [dlp.DeleteJobTriggerRequest],
            empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteJobTrigger(self._session, self._host, self._interceptor) # type: ignore

    @property
    def delete_stored_info_type(self) -> Callable[
            [dlp.DeleteStoredInfoTypeRequest],
            empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteStoredInfoType(self._session, self._host, self._interceptor) # type: ignore

    @property
    def finish_dlp_job(self) -> Callable[
            [dlp.FinishDlpJobRequest],
            empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._FinishDlpJob(self._session, self._host, self._interceptor) # type: ignore

    @property
    def get_deidentify_template(self) -> Callable[
            [dlp.GetDeidentifyTemplateRequest],
            dlp.DeidentifyTemplate]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetDeidentifyTemplate(self._session, self._host, self._interceptor) # type: ignore

    @property
    def get_dlp_job(self) -> Callable[
            [dlp.GetDlpJobRequest],
            dlp.DlpJob]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetDlpJob(self._session, self._host, self._interceptor) # type: ignore

    @property
    def get_inspect_template(self) -> Callable[
            [dlp.GetInspectTemplateRequest],
            dlp.InspectTemplate]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetInspectTemplate(self._session, self._host, self._interceptor) # type: ignore

    @property
    def get_job_trigger(self) -> Callable[
            [dlp.GetJobTriggerRequest],
            dlp.JobTrigger]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetJobTrigger(self._session, self._host, self._interceptor) # type: ignore

    @property
    def get_stored_info_type(self) -> Callable[
            [dlp.GetStoredInfoTypeRequest],
            dlp.StoredInfoType]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetStoredInfoType(self._session, self._host, self._interceptor) # type: ignore

    @property
    def hybrid_inspect_dlp_job(self) -> Callable[
            [dlp.HybridInspectDlpJobRequest],
            dlp.HybridInspectResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._HybridInspectDlpJob(self._session, self._host, self._interceptor) # type: ignore

    @property
    def hybrid_inspect_job_trigger(self) -> Callable[
            [dlp.HybridInspectJobTriggerRequest],
            dlp.HybridInspectResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._HybridInspectJobTrigger(self._session, self._host, self._interceptor) # type: ignore

    @property
    def inspect_content(self) -> Callable[
            [dlp.InspectContentRequest],
            dlp.InspectContentResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._InspectContent(self._session, self._host, self._interceptor) # type: ignore

    @property
    def list_deidentify_templates(self) -> Callable[
            [dlp.ListDeidentifyTemplatesRequest],
            dlp.ListDeidentifyTemplatesResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListDeidentifyTemplates(self._session, self._host, self._interceptor) # type: ignore

    @property
    def list_dlp_jobs(self) -> Callable[
            [dlp.ListDlpJobsRequest],
            dlp.ListDlpJobsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListDlpJobs(self._session, self._host, self._interceptor) # type: ignore

    @property
    def list_info_types(self) -> Callable[
            [dlp.ListInfoTypesRequest],
            dlp.ListInfoTypesResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListInfoTypes(self._session, self._host, self._interceptor) # type: ignore

    @property
    def list_inspect_templates(self) -> Callable[
            [dlp.ListInspectTemplatesRequest],
            dlp.ListInspectTemplatesResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListInspectTemplates(self._session, self._host, self._interceptor) # type: ignore

    @property
    def list_job_triggers(self) -> Callable[
            [dlp.ListJobTriggersRequest],
            dlp.ListJobTriggersResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListJobTriggers(self._session, self._host, self._interceptor) # type: ignore

    @property
    def list_stored_info_types(self) -> Callable[
            [dlp.ListStoredInfoTypesRequest],
            dlp.ListStoredInfoTypesResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListStoredInfoTypes(self._session, self._host, self._interceptor) # type: ignore

    @property
    def redact_image(self) -> Callable[
            [dlp.RedactImageRequest],
            dlp.RedactImageResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RedactImage(self._session, self._host, self._interceptor) # type: ignore

    @property
    def reidentify_content(self) -> Callable[
            [dlp.ReidentifyContentRequest],
            dlp.ReidentifyContentResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ReidentifyContent(self._session, self._host, self._interceptor) # type: ignore

    @property
    def update_deidentify_template(self) -> Callable[
            [dlp.UpdateDeidentifyTemplateRequest],
            dlp.DeidentifyTemplate]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateDeidentifyTemplate(self._session, self._host, self._interceptor) # type: ignore

    @property
    def update_inspect_template(self) -> Callable[
            [dlp.UpdateInspectTemplateRequest],
            dlp.InspectTemplate]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateInspectTemplate(self._session, self._host, self._interceptor) # type: ignore

    @property
    def update_job_trigger(self) -> Callable[
            [dlp.UpdateJobTriggerRequest],
            dlp.JobTrigger]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateJobTrigger(self._session, self._host, self._interceptor) # type: ignore

    @property
    def update_stored_info_type(self) -> Callable[
            [dlp.UpdateStoredInfoTypeRequest],
            dlp.StoredInfoType]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateStoredInfoType(self._session, self._host, self._interceptor) # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__=(
    'DlpServiceRestTransport',
)
