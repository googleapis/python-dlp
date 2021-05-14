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
from collections import OrderedDict
from distutils import util
import os
import re
from typing import Callable, Dict, Optional, Sequence, Tuple, Type, Union
import pkg_resources

from google.api_core import client_options as client_options_lib  # type: ignore
from google.api_core import exceptions as core_exceptions  # type: ignore
from google.api_core import gapic_v1  # type: ignore
from google.api_core import retry as retries  # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport import mtls  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.auth.exceptions import MutualTLSChannelError  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.dlp_v2.services.dlp_service import pagers
from google.cloud.dlp_v2.types import dlp
from google.protobuf import field_mask_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore
from .transports.base import DlpServiceTransport, DEFAULT_CLIENT_INFO
from .transports.grpc import DlpServiceGrpcTransport
from .transports.grpc_asyncio import DlpServiceGrpcAsyncIOTransport


class DlpServiceClientMeta(type):
    """Metaclass for the DlpService client.

    This provides class-level methods for building and retrieving
    support objects (e.g. transport) without polluting the client instance
    objects.
    """

    _transport_registry = OrderedDict()  # type: Dict[str, Type[DlpServiceTransport]]
    _transport_registry["grpc"] = DlpServiceGrpcTransport
    _transport_registry["grpc_asyncio"] = DlpServiceGrpcAsyncIOTransport

    def get_transport_class(cls, label: str = None,) -> Type[DlpServiceTransport]:
        """Returns an appropriate transport class.

        Args:
            label: The name of the desired transport. If none is
                provided, then the first transport in the registry is used.

        Returns:
            The transport class to use.
        """
        # If a specific transport is requested, return that one.
        if label:
            return cls._transport_registry[label]

        # No transport is requested; return the default (that is, the first one
        # in the dictionary).
        return next(iter(cls._transport_registry.values()))


class DlpServiceClient(metaclass=DlpServiceClientMeta):
    """The Cloud Data Loss Prevention (DLP) API is a service that
    allows clients to detect the presence of Personally Identifiable
    Information (PII) and other privacy-sensitive data in user-
    supplied, unstructured data streams, like text blocks or images.
    The service also includes methods for sensitive data redaction
    and scheduling of data scans on Google Cloud Platform based data
    sets.
    To learn more about concepts and find how-to guides see
    https://cloud.google.com/dlp/docs/.
    """

    @staticmethod
    def _get_default_mtls_endpoint(api_endpoint):
        """Converts api endpoint to mTLS endpoint.

        Convert "*.sandbox.googleapis.com" and "*.googleapis.com" to
        "*.mtls.sandbox.googleapis.com" and "*.mtls.googleapis.com" respectively.
        Args:
            api_endpoint (Optional[str]): the api endpoint to convert.
        Returns:
            str: converted mTLS api endpoint.
        """
        if not api_endpoint:
            return api_endpoint

        mtls_endpoint_re = re.compile(
            r"(?P<name>[^.]+)(?P<mtls>\.mtls)?(?P<sandbox>\.sandbox)?(?P<googledomain>\.googleapis\.com)?"
        )

        m = mtls_endpoint_re.match(api_endpoint)
        name, mtls, sandbox, googledomain = m.groups()
        if mtls or not googledomain:
            return api_endpoint

        if sandbox:
            return api_endpoint.replace(
                "sandbox.googleapis.com", "mtls.sandbox.googleapis.com"
            )

        return api_endpoint.replace(".googleapis.com", ".mtls.googleapis.com")

    DEFAULT_ENDPOINT = "dlp.googleapis.com"
    DEFAULT_MTLS_ENDPOINT = _get_default_mtls_endpoint.__func__(  # type: ignore
        DEFAULT_ENDPOINT
    )

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            DlpServiceClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_info(info)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            DlpServiceClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(filename)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file

    @property
    def transport(self) -> DlpServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            DlpServiceTransport: The transport used by the client
                instance.
        """
        return self._transport

    @staticmethod
    def deidentify_template_path(organization: str, deidentify_template: str,) -> str:
        """Returns a fully-qualified deidentify_template string."""
        return "organizations/{organization}/deidentifyTemplates/{deidentify_template}".format(
            organization=organization, deidentify_template=deidentify_template,
        )

    @staticmethod
    def parse_deidentify_template_path(path: str) -> Dict[str, str]:
        """Parses a deidentify_template path into its component segments."""
        m = re.match(
            r"^organizations/(?P<organization>.+?)/deidentifyTemplates/(?P<deidentify_template>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def dlp_content_path(project: str,) -> str:
        """Returns a fully-qualified dlp_content string."""
        return "projects/{project}/dlpContent".format(project=project,)

    @staticmethod
    def parse_dlp_content_path(path: str) -> Dict[str, str]:
        """Parses a dlp_content path into its component segments."""
        m = re.match(r"^projects/(?P<project>.+?)/dlpContent$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def dlp_job_path(project: str, dlp_job: str,) -> str:
        """Returns a fully-qualified dlp_job string."""
        return "projects/{project}/dlpJobs/{dlp_job}".format(
            project=project, dlp_job=dlp_job,
        )

    @staticmethod
    def parse_dlp_job_path(path: str) -> Dict[str, str]:
        """Parses a dlp_job path into its component segments."""
        m = re.match(r"^projects/(?P<project>.+?)/dlpJobs/(?P<dlp_job>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def finding_path(project: str, location: str, finding: str,) -> str:
        """Returns a fully-qualified finding string."""
        return "projects/{project}/locations/{location}/findings/{finding}".format(
            project=project, location=location, finding=finding,
        )

    @staticmethod
    def parse_finding_path(path: str) -> Dict[str, str]:
        """Parses a finding path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/findings/(?P<finding>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def inspect_template_path(organization: str, inspect_template: str,) -> str:
        """Returns a fully-qualified inspect_template string."""
        return "organizations/{organization}/inspectTemplates/{inspect_template}".format(
            organization=organization, inspect_template=inspect_template,
        )

    @staticmethod
    def parse_inspect_template_path(path: str) -> Dict[str, str]:
        """Parses a inspect_template path into its component segments."""
        m = re.match(
            r"^organizations/(?P<organization>.+?)/inspectTemplates/(?P<inspect_template>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def job_trigger_path(project: str, job_trigger: str,) -> str:
        """Returns a fully-qualified job_trigger string."""
        return "projects/{project}/jobTriggers/{job_trigger}".format(
            project=project, job_trigger=job_trigger,
        )

    @staticmethod
    def parse_job_trigger_path(path: str) -> Dict[str, str]:
        """Parses a job_trigger path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/jobTriggers/(?P<job_trigger>.+?)$", path
        )
        return m.groupdict() if m else {}

    @staticmethod
    def stored_info_type_path(organization: str, stored_info_type: str,) -> str:
        """Returns a fully-qualified stored_info_type string."""
        return "organizations/{organization}/storedInfoTypes/{stored_info_type}".format(
            organization=organization, stored_info_type=stored_info_type,
        )

    @staticmethod
    def parse_stored_info_type_path(path: str) -> Dict[str, str]:
        """Parses a stored_info_type path into its component segments."""
        m = re.match(
            r"^organizations/(?P<organization>.+?)/storedInfoTypes/(?P<stored_info_type>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def common_billing_account_path(billing_account: str,) -> str:
        """Returns a fully-qualified billing_account string."""
        return "billingAccounts/{billing_account}".format(
            billing_account=billing_account,
        )

    @staticmethod
    def parse_common_billing_account_path(path: str) -> Dict[str, str]:
        """Parse a billing_account path into its component segments."""
        m = re.match(r"^billingAccounts/(?P<billing_account>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_folder_path(folder: str,) -> str:
        """Returns a fully-qualified folder string."""
        return "folders/{folder}".format(folder=folder,)

    @staticmethod
    def parse_common_folder_path(path: str) -> Dict[str, str]:
        """Parse a folder path into its component segments."""
        m = re.match(r"^folders/(?P<folder>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_organization_path(organization: str,) -> str:
        """Returns a fully-qualified organization string."""
        return "organizations/{organization}".format(organization=organization,)

    @staticmethod
    def parse_common_organization_path(path: str) -> Dict[str, str]:
        """Parse a organization path into its component segments."""
        m = re.match(r"^organizations/(?P<organization>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_project_path(project: str,) -> str:
        """Returns a fully-qualified project string."""
        return "projects/{project}".format(project=project,)

    @staticmethod
    def parse_common_project_path(path: str) -> Dict[str, str]:
        """Parse a project path into its component segments."""
        m = re.match(r"^projects/(?P<project>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_location_path(project: str, location: str,) -> str:
        """Returns a fully-qualified location string."""
        return "projects/{project}/locations/{location}".format(
            project=project, location=location,
        )

    @staticmethod
    def parse_common_location_path(path: str) -> Dict[str, str]:
        """Parse a location path into its component segments."""
        m = re.match(r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)$", path)
        return m.groupdict() if m else {}

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Union[str, DlpServiceTransport, None] = None,
        client_options: Optional[client_options_lib.ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the dlp service client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, DlpServiceTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (google.api_core.client_options.ClientOptions): Custom options for the
                client. It won't take effect if a ``transport`` instance is provided.
                (1) The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client. GOOGLE_API_USE_MTLS_ENDPOINT
                environment variable can also be used to override the endpoint:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto switch to the
                default mTLS endpoint if client certificate is present, this is
                the default value). However, the ``api_endpoint`` property takes
                precedence if provided.
                (2) If GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide client certificate for mutual TLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        if isinstance(client_options, dict):
            client_options = client_options_lib.from_dict(client_options)
        if client_options is None:
            client_options = client_options_lib.ClientOptions()

        # Create SSL credentials for mutual TLS if needed.
        use_client_cert = bool(
            util.strtobool(os.getenv("GOOGLE_API_USE_CLIENT_CERTIFICATE", "false"))
        )

        client_cert_source_func = None
        is_mtls = False
        if use_client_cert:
            if client_options.client_cert_source:
                is_mtls = True
                client_cert_source_func = client_options.client_cert_source
            else:
                is_mtls = mtls.has_default_client_cert_source()
                if is_mtls:
                    client_cert_source_func = mtls.default_client_cert_source()
                else:
                    client_cert_source_func = None

        # Figure out which api endpoint to use.
        if client_options.api_endpoint is not None:
            api_endpoint = client_options.api_endpoint
        else:
            use_mtls_env = os.getenv("GOOGLE_API_USE_MTLS_ENDPOINT", "auto")
            if use_mtls_env == "never":
                api_endpoint = self.DEFAULT_ENDPOINT
            elif use_mtls_env == "always":
                api_endpoint = self.DEFAULT_MTLS_ENDPOINT
            elif use_mtls_env == "auto":
                if is_mtls:
                    api_endpoint = self.DEFAULT_MTLS_ENDPOINT
                else:
                    api_endpoint = self.DEFAULT_ENDPOINT
            else:
                raise MutualTLSChannelError(
                    "Unsupported GOOGLE_API_USE_MTLS_ENDPOINT value. Accepted "
                    "values: never, auto, always"
                )

        # Save or instantiate the transport.
        # Ordinarily, we provide the transport, but allowing a custom transport
        # instance provides an extensibility point for unusual situations.
        if isinstance(transport, DlpServiceTransport):
            # transport is a DlpServiceTransport instance.
            if credentials or client_options.credentials_file:
                raise ValueError(
                    "When providing a transport instance, "
                    "provide its credentials directly."
                )
            if client_options.scopes:
                raise ValueError(
                    "When providing a transport instance, provide its scopes "
                    "directly."
                )
            self._transport = transport
        else:
            Transport = type(self).get_transport_class(transport)
            self._transport = Transport(
                credentials=credentials,
                credentials_file=client_options.credentials_file,
                host=api_endpoint,
                scopes=client_options.scopes,
                client_cert_source_for_mtls=client_cert_source_func,
                quota_project_id=client_options.quota_project_id,
                client_info=client_info,
            )

    def inspect_content(
        self,
        request: dlp.InspectContentRequest = None,
        *,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> dlp.InspectContentResponse:
        r"""Finds potentially sensitive info in content.
        This method has limits on input size, processing time,
        and output size.
        When no InfoTypes or CustomInfoTypes are specified in
        this request, the system will automatically choose what
        detectors to run. By default this may be all types, but
        may change over time as detectors are updated.
        For how to guides, see
        https://cloud.google.com/dlp/docs/inspecting-images and
        https://cloud.google.com/dlp/docs/inspecting-text,

        Args:
            request (google.cloud.dlp_v2.types.InspectContentRequest):
                The request object. Request to search for potentially
                sensitive info in a ContentItem.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dlp_v2.types.InspectContentResponse:
                Results of inspecting an item.
        """
        # Create or coerce a protobuf request object.
        # Minor optimization to avoid making a copy if the user passes
        # in a dlp.InspectContentRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, dlp.InspectContentRequest):
            request = dlp.InspectContentRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.inspect_content]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    def redact_image(
        self,
        request: dlp.RedactImageRequest = None,
        *,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> dlp.RedactImageResponse:
        r"""Redacts potentially sensitive info from an image.
        This method has limits on input size, processing time,
        and output size. See
        https://cloud.google.com/dlp/docs/redacting-sensitive-
        data-images to learn more.

        When no InfoTypes or CustomInfoTypes are specified in
        this request, the system will automatically choose what
        detectors to run. By default this may be all types, but
        may change over time as detectors are updated.

        Args:
            request (google.cloud.dlp_v2.types.RedactImageRequest):
                The request object. Request to search for potentially
                sensitive info in an image and redact it by covering it
                with a colored rectangle.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dlp_v2.types.RedactImageResponse:
                Results of redacting an image.
        """
        # Create or coerce a protobuf request object.
        # Minor optimization to avoid making a copy if the user passes
        # in a dlp.RedactImageRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, dlp.RedactImageRequest):
            request = dlp.RedactImageRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.redact_image]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    def deidentify_content(
        self,
        request: dlp.DeidentifyContentRequest = None,
        *,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> dlp.DeidentifyContentResponse:
        r"""De-identifies potentially sensitive info from a
        ContentItem. This method has limits on input size and
        output size. See
        https://cloud.google.com/dlp/docs/deidentify-sensitive-
        data to learn more.

        When no InfoTypes or CustomInfoTypes are specified in
        this request, the system will automatically choose what
        detectors to run. By default this may be all types, but
        may change over time as detectors are updated.

        Args:
            request (google.cloud.dlp_v2.types.DeidentifyContentRequest):
                The request object. Request to de-identify a list of
                items.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dlp_v2.types.DeidentifyContentResponse:
                Results of de-identifying a
                ContentItem.

        """
        # Create or coerce a protobuf request object.
        # Minor optimization to avoid making a copy if the user passes
        # in a dlp.DeidentifyContentRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, dlp.DeidentifyContentRequest):
            request = dlp.DeidentifyContentRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.deidentify_content]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    def reidentify_content(
        self,
        request: dlp.ReidentifyContentRequest = None,
        *,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> dlp.ReidentifyContentResponse:
        r"""Re-identifies content that has been de-identified. See
        https://cloud.google.com/dlp/docs/pseudonymization#re-identification_in_free_text_code_example
        to learn more.

        Args:
            request (google.cloud.dlp_v2.types.ReidentifyContentRequest):
                The request object. Request to re-identify an item.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dlp_v2.types.ReidentifyContentResponse:
                Results of re-identifying a item.
        """
        # Create or coerce a protobuf request object.
        # Minor optimization to avoid making a copy if the user passes
        # in a dlp.ReidentifyContentRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, dlp.ReidentifyContentRequest):
            request = dlp.ReidentifyContentRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.reidentify_content]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    def list_info_types(
        self,
        request: dlp.ListInfoTypesRequest = None,
        *,
        parent: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> dlp.ListInfoTypesResponse:
        r"""Returns a list of the sensitive information types
        that the DLP API supports. See
        https://cloud.google.com/dlp/docs/infotypes-reference to
        learn more.

        Args:
            request (google.cloud.dlp_v2.types.ListInfoTypesRequest):
                The request object. Request for the list of infoTypes.
            parent (str):
                The parent resource name.

                The format of this value is as follows:

                ::

                    locations/<var>LOCATION_ID</var>

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dlp_v2.types.ListInfoTypesResponse:
                Response to the ListInfoTypes
                request.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a dlp.ListInfoTypesRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, dlp.ListInfoTypesRequest):
            request = dlp.ListInfoTypesRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_info_types]

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    def create_inspect_template(
        self,
        request: dlp.CreateInspectTemplateRequest = None,
        *,
        parent: str = None,
        inspect_template: dlp.InspectTemplate = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> dlp.InspectTemplate:
        r"""Creates an InspectTemplate for re-using frequently
        used configuration for inspecting content, images, and
        storage. See https://cloud.google.com/dlp/docs/creating-
        templates to learn more.

        Args:
            request (google.cloud.dlp_v2.types.CreateInspectTemplateRequest):
                The request object. Request message for
                CreateInspectTemplate.
            parent (str):
                Required. Parent resource name.

                The format of this value varies depending on the scope
                of the request (project or organization) and whether you
                have `specified a processing
                location <https://cloud.google.com/dlp/docs/specifying-location>`__:

                -  Projects scope, location specified:
                   ``projects/``\ PROJECT_ID\ ``/locations/``\ LOCATION_ID
                -  Projects scope, no location specified (defaults to
                   global): ``projects/``\ PROJECT_ID
                -  Organizations scope, location specified:
                   ``organizations/``\ ORG_ID\ ``/locations/``\ LOCATION_ID
                -  Organizations scope, no location specified (defaults
                   to global): ``organizations/``\ ORG_ID

                The following example ``parent`` string specifies a
                parent project with the identifier ``example-project``,
                and specifies the ``europe-west3`` location for
                processing data:

                ::

                    parent=projects/example-project/locations/europe-west3

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            inspect_template (google.cloud.dlp_v2.types.InspectTemplate):
                Required. The InspectTemplate to
                create.

                This corresponds to the ``inspect_template`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dlp_v2.types.InspectTemplate:
                The inspectTemplate contains a
                configuration (set of types of sensitive
                data to be detected) to be used anywhere
                you otherwise would normally specify
                InspectConfig. See
                https://cloud.google.com/dlp/docs/concepts-
                templates to learn more.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, inspect_template])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a dlp.CreateInspectTemplateRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, dlp.CreateInspectTemplateRequest):
            request = dlp.CreateInspectTemplateRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if inspect_template is not None:
                request.inspect_template = inspect_template

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_inspect_template]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    def update_inspect_template(
        self,
        request: dlp.UpdateInspectTemplateRequest = None,
        *,
        name: str = None,
        inspect_template: dlp.InspectTemplate = None,
        update_mask: field_mask_pb2.FieldMask = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> dlp.InspectTemplate:
        r"""Updates the InspectTemplate.
        See https://cloud.google.com/dlp/docs/creating-templates
        to learn more.

        Args:
            request (google.cloud.dlp_v2.types.UpdateInspectTemplateRequest):
                The request object. Request message for
                UpdateInspectTemplate.
            name (str):
                Required. Resource name of organization and
                inspectTemplate to be updated, for example
                ``organizations/433245324/inspectTemplates/432452342``
                or projects/project-id/inspectTemplates/432452342.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            inspect_template (google.cloud.dlp_v2.types.InspectTemplate):
                New InspectTemplate value.
                This corresponds to the ``inspect_template`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Mask to control which fields get
                updated.

                This corresponds to the ``update_mask`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dlp_v2.types.InspectTemplate:
                The inspectTemplate contains a
                configuration (set of types of sensitive
                data to be detected) to be used anywhere
                you otherwise would normally specify
                InspectConfig. See
                https://cloud.google.com/dlp/docs/concepts-
                templates to learn more.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name, inspect_template, update_mask])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a dlp.UpdateInspectTemplateRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, dlp.UpdateInspectTemplateRequest):
            request = dlp.UpdateInspectTemplateRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name
            if inspect_template is not None:
                request.inspect_template = inspect_template
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.update_inspect_template]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    def get_inspect_template(
        self,
        request: dlp.GetInspectTemplateRequest = None,
        *,
        name: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> dlp.InspectTemplate:
        r"""Gets an InspectTemplate.
        See https://cloud.google.com/dlp/docs/creating-templates
        to learn more.

        Args:
            request (google.cloud.dlp_v2.types.GetInspectTemplateRequest):
                The request object. Request message for
                GetInspectTemplate.
            name (str):
                Required. Resource name of the organization and
                inspectTemplate to be read, for example
                ``organizations/433245324/inspectTemplates/432452342``
                or projects/project-id/inspectTemplates/432452342.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dlp_v2.types.InspectTemplate:
                The inspectTemplate contains a
                configuration (set of types of sensitive
                data to be detected) to be used anywhere
                you otherwise would normally specify
                InspectConfig. See
                https://cloud.google.com/dlp/docs/concepts-
                templates to learn more.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a dlp.GetInspectTemplateRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, dlp.GetInspectTemplateRequest):
            request = dlp.GetInspectTemplateRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_inspect_template]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    def list_inspect_templates(
        self,
        request: dlp.ListInspectTemplatesRequest = None,
        *,
        parent: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListInspectTemplatesPager:
        r"""Lists InspectTemplates.
        See https://cloud.google.com/dlp/docs/creating-templates
        to learn more.

        Args:
            request (google.cloud.dlp_v2.types.ListInspectTemplatesRequest):
                The request object. Request message for
                ListInspectTemplates.
            parent (str):
                Required. Parent resource name.

                The format of this value varies depending on the scope
                of the request (project or organization) and whether you
                have `specified a processing
                location <https://cloud.google.com/dlp/docs/specifying-location>`__:

                -  Projects scope, location specified:
                   ``projects/``\ PROJECT_ID\ ``/locations/``\ LOCATION_ID
                -  Projects scope, no location specified (defaults to
                   global): ``projects/``\ PROJECT_ID
                -  Organizations scope, location specified:
                   ``organizations/``\ ORG_ID\ ``/locations/``\ LOCATION_ID
                -  Organizations scope, no location specified (defaults
                   to global): ``organizations/``\ ORG_ID

                The following example ``parent`` string specifies a
                parent project with the identifier ``example-project``,
                and specifies the ``europe-west3`` location for
                processing data:

                ::

                    parent=projects/example-project/locations/europe-west3

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dlp_v2.services.dlp_service.pagers.ListInspectTemplatesPager:
                Response message for
                ListInspectTemplates.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a dlp.ListInspectTemplatesRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, dlp.ListInspectTemplatesRequest):
            request = dlp.ListInspectTemplatesRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_inspect_templates]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListInspectTemplatesPager(
            method=rpc, request=request, response=response, metadata=metadata,
        )

        # Done; return the response.
        return response

    def delete_inspect_template(
        self,
        request: dlp.DeleteInspectTemplateRequest = None,
        *,
        name: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> None:
        r"""Deletes an InspectTemplate.
        See https://cloud.google.com/dlp/docs/creating-templates
        to learn more.

        Args:
            request (google.cloud.dlp_v2.types.DeleteInspectTemplateRequest):
                The request object. Request message for
                DeleteInspectTemplate.
            name (str):
                Required. Resource name of the organization and
                inspectTemplate to be deleted, for example
                ``organizations/433245324/inspectTemplates/432452342``
                or projects/project-id/inspectTemplates/432452342.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a dlp.DeleteInspectTemplateRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, dlp.DeleteInspectTemplateRequest):
            request = dlp.DeleteInspectTemplateRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete_inspect_template]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        rpc(
            request, retry=retry, timeout=timeout, metadata=metadata,
        )

    def create_deidentify_template(
        self,
        request: dlp.CreateDeidentifyTemplateRequest = None,
        *,
        parent: str = None,
        deidentify_template: dlp.DeidentifyTemplate = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> dlp.DeidentifyTemplate:
        r"""Creates a DeidentifyTemplate for re-using frequently
        used configuration for de-identifying content, images,
        and storage. See
        https://cloud.google.com/dlp/docs/creating-templates-
        deid to learn more.

        Args:
            request (google.cloud.dlp_v2.types.CreateDeidentifyTemplateRequest):
                The request object. Request message for
                CreateDeidentifyTemplate.
            parent (str):
                Required. Parent resource name.

                The format of this value varies depending on the scope
                of the request (project or organization) and whether you
                have `specified a processing
                location <https://cloud.google.com/dlp/docs/specifying-location>`__:

                -  Projects scope, location specified:
                   ``projects/``\ PROJECT_ID\ ``/locations/``\ LOCATION_ID
                -  Projects scope, no location specified (defaults to
                   global): ``projects/``\ PROJECT_ID
                -  Organizations scope, location specified:
                   ``organizations/``\ ORG_ID\ ``/locations/``\ LOCATION_ID
                -  Organizations scope, no location specified (defaults
                   to global): ``organizations/``\ ORG_ID

                The following example ``parent`` string specifies a
                parent project with the identifier ``example-project``,
                and specifies the ``europe-west3`` location for
                processing data:

                ::

                    parent=projects/example-project/locations/europe-west3

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            deidentify_template (google.cloud.dlp_v2.types.DeidentifyTemplate):
                Required. The DeidentifyTemplate to
                create.

                This corresponds to the ``deidentify_template`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dlp_v2.types.DeidentifyTemplate:
                DeidentifyTemplates contains
                instructions on how to de-identify
                content. See
                https://cloud.google.com/dlp/docs/concepts-
                templates to learn more.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, deidentify_template])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a dlp.CreateDeidentifyTemplateRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, dlp.CreateDeidentifyTemplateRequest):
            request = dlp.CreateDeidentifyTemplateRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if deidentify_template is not None:
                request.deidentify_template = deidentify_template

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.create_deidentify_template
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    def update_deidentify_template(
        self,
        request: dlp.UpdateDeidentifyTemplateRequest = None,
        *,
        name: str = None,
        deidentify_template: dlp.DeidentifyTemplate = None,
        update_mask: field_mask_pb2.FieldMask = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> dlp.DeidentifyTemplate:
        r"""Updates the DeidentifyTemplate.
        See https://cloud.google.com/dlp/docs/creating-
        templates-deid to learn more.

        Args:
            request (google.cloud.dlp_v2.types.UpdateDeidentifyTemplateRequest):
                The request object. Request message for
                UpdateDeidentifyTemplate.
            name (str):
                Required. Resource name of organization and deidentify
                template to be updated, for example
                ``organizations/433245324/deidentifyTemplates/432452342``
                or projects/project-id/deidentifyTemplates/432452342.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            deidentify_template (google.cloud.dlp_v2.types.DeidentifyTemplate):
                New DeidentifyTemplate value.
                This corresponds to the ``deidentify_template`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Mask to control which fields get
                updated.

                This corresponds to the ``update_mask`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dlp_v2.types.DeidentifyTemplate:
                DeidentifyTemplates contains
                instructions on how to de-identify
                content. See
                https://cloud.google.com/dlp/docs/concepts-
                templates to learn more.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name, deidentify_template, update_mask])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a dlp.UpdateDeidentifyTemplateRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, dlp.UpdateDeidentifyTemplateRequest):
            request = dlp.UpdateDeidentifyTemplateRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name
            if deidentify_template is not None:
                request.deidentify_template = deidentify_template
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.update_deidentify_template
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    def get_deidentify_template(
        self,
        request: dlp.GetDeidentifyTemplateRequest = None,
        *,
        name: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> dlp.DeidentifyTemplate:
        r"""Gets a DeidentifyTemplate.
        See https://cloud.google.com/dlp/docs/creating-
        templates-deid to learn more.

        Args:
            request (google.cloud.dlp_v2.types.GetDeidentifyTemplateRequest):
                The request object. Request message for
                GetDeidentifyTemplate.
            name (str):
                Required. Resource name of the organization and
                deidentify template to be read, for example
                ``organizations/433245324/deidentifyTemplates/432452342``
                or projects/project-id/deidentifyTemplates/432452342.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dlp_v2.types.DeidentifyTemplate:
                DeidentifyTemplates contains
                instructions on how to de-identify
                content. See
                https://cloud.google.com/dlp/docs/concepts-
                templates to learn more.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a dlp.GetDeidentifyTemplateRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, dlp.GetDeidentifyTemplateRequest):
            request = dlp.GetDeidentifyTemplateRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_deidentify_template]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    def list_deidentify_templates(
        self,
        request: dlp.ListDeidentifyTemplatesRequest = None,
        *,
        parent: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListDeidentifyTemplatesPager:
        r"""Lists DeidentifyTemplates.
        See https://cloud.google.com/dlp/docs/creating-
        templates-deid to learn more.

        Args:
            request (google.cloud.dlp_v2.types.ListDeidentifyTemplatesRequest):
                The request object. Request message for
                ListDeidentifyTemplates.
            parent (str):
                Required. Parent resource name.

                The format of this value varies depending on the scope
                of the request (project or organization) and whether you
                have `specified a processing
                location <https://cloud.google.com/dlp/docs/specifying-location>`__:

                -  Projects scope, location specified:
                   ``projects/``\ PROJECT_ID\ ``/locations/``\ LOCATION_ID
                -  Projects scope, no location specified (defaults to
                   global): ``projects/``\ PROJECT_ID
                -  Organizations scope, location specified:
                   ``organizations/``\ ORG_ID\ ``/locations/``\ LOCATION_ID
                -  Organizations scope, no location specified (defaults
                   to global): ``organizations/``\ ORG_ID

                The following example ``parent`` string specifies a
                parent project with the identifier ``example-project``,
                and specifies the ``europe-west3`` location for
                processing data:

                ::

                    parent=projects/example-project/locations/europe-west3

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dlp_v2.services.dlp_service.pagers.ListDeidentifyTemplatesPager:
                Response message for
                ListDeidentifyTemplates.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a dlp.ListDeidentifyTemplatesRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, dlp.ListDeidentifyTemplatesRequest):
            request = dlp.ListDeidentifyTemplatesRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.list_deidentify_templates
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListDeidentifyTemplatesPager(
            method=rpc, request=request, response=response, metadata=metadata,
        )

        # Done; return the response.
        return response

    def delete_deidentify_template(
        self,
        request: dlp.DeleteDeidentifyTemplateRequest = None,
        *,
        name: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> None:
        r"""Deletes a DeidentifyTemplate.
        See https://cloud.google.com/dlp/docs/creating-
        templates-deid to learn more.

        Args:
            request (google.cloud.dlp_v2.types.DeleteDeidentifyTemplateRequest):
                The request object. Request message for
                DeleteDeidentifyTemplate.
            name (str):
                Required. Resource name of the organization and
                deidentify template to be deleted, for example
                ``organizations/433245324/deidentifyTemplates/432452342``
                or projects/project-id/deidentifyTemplates/432452342.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a dlp.DeleteDeidentifyTemplateRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, dlp.DeleteDeidentifyTemplateRequest):
            request = dlp.DeleteDeidentifyTemplateRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.delete_deidentify_template
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        rpc(
            request, retry=retry, timeout=timeout, metadata=metadata,
        )

    def create_job_trigger(
        self,
        request: dlp.CreateJobTriggerRequest = None,
        *,
        parent: str = None,
        job_trigger: dlp.JobTrigger = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> dlp.JobTrigger:
        r"""Creates a job trigger to run DLP actions such as
        scanning storage for sensitive information on a set
        schedule. See
        https://cloud.google.com/dlp/docs/creating-job-triggers
        to learn more.

        Args:
            request (google.cloud.dlp_v2.types.CreateJobTriggerRequest):
                The request object. Request message for
                CreateJobTrigger.
            parent (str):
                Required. Parent resource name.

                The format of this value varies depending on whether you
                have `specified a processing
                location <https://cloud.google.com/dlp/docs/specifying-location>`__:

                -  Projects scope, location specified:
                   ``projects/``\ PROJECT_ID\ ``/locations/``\ LOCATION_ID
                -  Projects scope, no location specified (defaults to
                   global): ``projects/``\ PROJECT_ID

                The following example ``parent`` string specifies a
                parent project with the identifier ``example-project``,
                and specifies the ``europe-west3`` location for
                processing data:

                ::

                    parent=projects/example-project/locations/europe-west3

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            job_trigger (google.cloud.dlp_v2.types.JobTrigger):
                Required. The JobTrigger to create.
                This corresponds to the ``job_trigger`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dlp_v2.types.JobTrigger:
                Contains a configuration to make dlp
                api calls on a repeating basis. See
                https://cloud.google.com/dlp/docs/concepts-
                job-triggers to learn more.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, job_trigger])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a dlp.CreateJobTriggerRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, dlp.CreateJobTriggerRequest):
            request = dlp.CreateJobTriggerRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if job_trigger is not None:
                request.job_trigger = job_trigger

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_job_trigger]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    def update_job_trigger(
        self,
        request: dlp.UpdateJobTriggerRequest = None,
        *,
        name: str = None,
        job_trigger: dlp.JobTrigger = None,
        update_mask: field_mask_pb2.FieldMask = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> dlp.JobTrigger:
        r"""Updates a job trigger.
        See https://cloud.google.com/dlp/docs/creating-job-
        triggers to learn more.

        Args:
            request (google.cloud.dlp_v2.types.UpdateJobTriggerRequest):
                The request object. Request message for
                UpdateJobTrigger.
            name (str):
                Required. Resource name of the project and the
                triggeredJob, for example
                ``projects/dlp-test-project/jobTriggers/53234423``.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            job_trigger (google.cloud.dlp_v2.types.JobTrigger):
                New JobTrigger value.
                This corresponds to the ``job_trigger`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Mask to control which fields get
                updated.

                This corresponds to the ``update_mask`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dlp_v2.types.JobTrigger:
                Contains a configuration to make dlp
                api calls on a repeating basis. See
                https://cloud.google.com/dlp/docs/concepts-
                job-triggers to learn more.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name, job_trigger, update_mask])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a dlp.UpdateJobTriggerRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, dlp.UpdateJobTriggerRequest):
            request = dlp.UpdateJobTriggerRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name
            if job_trigger is not None:
                request.job_trigger = job_trigger
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.update_job_trigger]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    def hybrid_inspect_job_trigger(
        self,
        request: dlp.HybridInspectJobTriggerRequest = None,
        *,
        name: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> dlp.HybridInspectResponse:
        r"""Inspect hybrid content and store findings to a
        trigger. The inspection will be processed
        asynchronously. To review the findings monitor the jobs
        within the trigger.
        Early access feature is in a pre-release state and might
        change or have limited support. For more information,
        see
        https://cloud.google.com/products#product-launch-stages.

        Args:
            request (google.cloud.dlp_v2.types.HybridInspectJobTriggerRequest):
                The request object. Request to search for potentially
                sensitive info in a custom location.
            name (str):
                Required. Resource name of the trigger to execute a
                hybrid inspect on, for example
                ``projects/dlp-test-project/jobTriggers/53234423``.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dlp_v2.types.HybridInspectResponse:
                Quota exceeded errors will be thrown
                once quota has been met.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a dlp.HybridInspectJobTriggerRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, dlp.HybridInspectJobTriggerRequest):
            request = dlp.HybridInspectJobTriggerRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.hybrid_inspect_job_trigger
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    def get_job_trigger(
        self,
        request: dlp.GetJobTriggerRequest = None,
        *,
        name: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> dlp.JobTrigger:
        r"""Gets a job trigger.
        See https://cloud.google.com/dlp/docs/creating-job-
        triggers to learn more.

        Args:
            request (google.cloud.dlp_v2.types.GetJobTriggerRequest):
                The request object. Request message for GetJobTrigger.
            name (str):
                Required. Resource name of the project and the
                triggeredJob, for example
                ``projects/dlp-test-project/jobTriggers/53234423``.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dlp_v2.types.JobTrigger:
                Contains a configuration to make dlp
                api calls on a repeating basis. See
                https://cloud.google.com/dlp/docs/concepts-
                job-triggers to learn more.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a dlp.GetJobTriggerRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, dlp.GetJobTriggerRequest):
            request = dlp.GetJobTriggerRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_job_trigger]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    def list_job_triggers(
        self,
        request: dlp.ListJobTriggersRequest = None,
        *,
        parent: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListJobTriggersPager:
        r"""Lists job triggers.
        See https://cloud.google.com/dlp/docs/creating-job-
        triggers to learn more.

        Args:
            request (google.cloud.dlp_v2.types.ListJobTriggersRequest):
                The request object. Request message for ListJobTriggers.
            parent (str):
                Required. Parent resource name.

                The format of this value varies depending on whether you
                have `specified a processing
                location <https://cloud.google.com/dlp/docs/specifying-location>`__:

                -  Projects scope, location specified:
                   ``projects/``\ PROJECT_ID\ ``/locations/``\ LOCATION_ID
                -  Projects scope, no location specified (defaults to
                   global): ``projects/``\ PROJECT_ID

                The following example ``parent`` string specifies a
                parent project with the identifier ``example-project``,
                and specifies the ``europe-west3`` location for
                processing data:

                ::

                    parent=projects/example-project/locations/europe-west3

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dlp_v2.services.dlp_service.pagers.ListJobTriggersPager:
                Response message for ListJobTriggers.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a dlp.ListJobTriggersRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, dlp.ListJobTriggersRequest):
            request = dlp.ListJobTriggersRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_job_triggers]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListJobTriggersPager(
            method=rpc, request=request, response=response, metadata=metadata,
        )

        # Done; return the response.
        return response

    def delete_job_trigger(
        self,
        request: dlp.DeleteJobTriggerRequest = None,
        *,
        name: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> None:
        r"""Deletes a job trigger.
        See https://cloud.google.com/dlp/docs/creating-job-
        triggers to learn more.

        Args:
            request (google.cloud.dlp_v2.types.DeleteJobTriggerRequest):
                The request object. Request message for
                DeleteJobTrigger.
            name (str):
                Required. Resource name of the project and the
                triggeredJob, for example
                ``projects/dlp-test-project/jobTriggers/53234423``.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a dlp.DeleteJobTriggerRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, dlp.DeleteJobTriggerRequest):
            request = dlp.DeleteJobTriggerRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete_job_trigger]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        rpc(
            request, retry=retry, timeout=timeout, metadata=metadata,
        )

    def activate_job_trigger(
        self,
        request: dlp.ActivateJobTriggerRequest = None,
        *,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> dlp.DlpJob:
        r"""Activate a job trigger. Causes the immediate execute
        of a trigger instead of waiting on the trigger event to
        occur.

        Args:
            request (google.cloud.dlp_v2.types.ActivateJobTriggerRequest):
                The request object. Request message for
                ActivateJobTrigger.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dlp_v2.types.DlpJob:
                Combines all of the information about
                a DLP job.

        """
        # Create or coerce a protobuf request object.
        # Minor optimization to avoid making a copy if the user passes
        # in a dlp.ActivateJobTriggerRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, dlp.ActivateJobTriggerRequest):
            request = dlp.ActivateJobTriggerRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.activate_job_trigger]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    def create_dlp_job(
        self,
        request: dlp.CreateDlpJobRequest = None,
        *,
        parent: str = None,
        inspect_job: dlp.InspectJobConfig = None,
        risk_job: dlp.RiskAnalysisJobConfig = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> dlp.DlpJob:
        r"""Creates a new job to inspect storage or calculate
        risk metrics. See
        https://cloud.google.com/dlp/docs/inspecting-storage and
        https://cloud.google.com/dlp/docs/compute-risk-analysis
        to learn more.
        When no InfoTypes or CustomInfoTypes are specified in
        inspect jobs, the system will automatically choose what
        detectors to run. By default this may be all types, but
        may change over time as detectors are updated.

        Args:
            request (google.cloud.dlp_v2.types.CreateDlpJobRequest):
                The request object. Request message for
                CreateDlpJobRequest. Used to initiate long running jobs
                such as calculating risk metrics or inspecting Google
                Cloud Storage.
            parent (str):
                Required. Parent resource name.

                The format of this value varies depending on whether you
                have `specified a processing
                location <https://cloud.google.com/dlp/docs/specifying-location>`__:

                -  Projects scope, location specified:
                   ``projects/``\ PROJECT_ID\ ``/locations/``\ LOCATION_ID
                -  Projects scope, no location specified (defaults to
                   global): ``projects/``\ PROJECT_ID

                The following example ``parent`` string specifies a
                parent project with the identifier ``example-project``,
                and specifies the ``europe-west3`` location for
                processing data:

                ::

                    parent=projects/example-project/locations/europe-west3

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            inspect_job (google.cloud.dlp_v2.types.InspectJobConfig):
                Set to control what and how to
                inspect.

                This corresponds to the ``inspect_job`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            risk_job (google.cloud.dlp_v2.types.RiskAnalysisJobConfig):
                Set to choose what metric to
                calculate.

                This corresponds to the ``risk_job`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dlp_v2.types.DlpJob:
                Combines all of the information about
                a DLP job.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, inspect_job, risk_job])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a dlp.CreateDlpJobRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, dlp.CreateDlpJobRequest):
            request = dlp.CreateDlpJobRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if inspect_job is not None:
                request.inspect_job = inspect_job
            if risk_job is not None:
                request.risk_job = risk_job

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_dlp_job]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    def list_dlp_jobs(
        self,
        request: dlp.ListDlpJobsRequest = None,
        *,
        parent: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListDlpJobsPager:
        r"""Lists DlpJobs that match the specified filter in the
        request. See
        https://cloud.google.com/dlp/docs/inspecting-storage and
        https://cloud.google.com/dlp/docs/compute-risk-analysis
        to learn more.

        Args:
            request (google.cloud.dlp_v2.types.ListDlpJobsRequest):
                The request object. The request message for listing DLP
                jobs.
            parent (str):
                Required. Parent resource name.

                The format of this value varies depending on whether you
                have `specified a processing
                location <https://cloud.google.com/dlp/docs/specifying-location>`__:

                -  Projects scope, location specified:
                   ``projects/``\ PROJECT_ID\ ``/locations/``\ LOCATION_ID
                -  Projects scope, no location specified (defaults to
                   global): ``projects/``\ PROJECT_ID

                The following example ``parent`` string specifies a
                parent project with the identifier ``example-project``,
                and specifies the ``europe-west3`` location for
                processing data:

                ::

                    parent=projects/example-project/locations/europe-west3

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dlp_v2.services.dlp_service.pagers.ListDlpJobsPager:
                The response message for listing DLP
                jobs.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a dlp.ListDlpJobsRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, dlp.ListDlpJobsRequest):
            request = dlp.ListDlpJobsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_dlp_jobs]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListDlpJobsPager(
            method=rpc, request=request, response=response, metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_dlp_job(
        self,
        request: dlp.GetDlpJobRequest = None,
        *,
        name: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> dlp.DlpJob:
        r"""Gets the latest state of a long-running DlpJob.
        See https://cloud.google.com/dlp/docs/inspecting-storage
        and https://cloud.google.com/dlp/docs/compute-risk-
        analysis to learn more.

        Args:
            request (google.cloud.dlp_v2.types.GetDlpJobRequest):
                The request object. The request message for
                [DlpJobs.GetDlpJob][].
            name (str):
                Required. The name of the DlpJob
                resource.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dlp_v2.types.DlpJob:
                Combines all of the information about
                a DLP job.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a dlp.GetDlpJobRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, dlp.GetDlpJobRequest):
            request = dlp.GetDlpJobRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_dlp_job]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    def delete_dlp_job(
        self,
        request: dlp.DeleteDlpJobRequest = None,
        *,
        name: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> None:
        r"""Deletes a long-running DlpJob. This method indicates
        that the client is no longer interested in the DlpJob
        result. The job will be cancelled if possible.
        See https://cloud.google.com/dlp/docs/inspecting-storage
        and https://cloud.google.com/dlp/docs/compute-risk-
        analysis to learn more.

        Args:
            request (google.cloud.dlp_v2.types.DeleteDlpJobRequest):
                The request object. The request message for deleting a
                DLP job.
            name (str):
                Required. The name of the DlpJob
                resource to be deleted.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a dlp.DeleteDlpJobRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, dlp.DeleteDlpJobRequest):
            request = dlp.DeleteDlpJobRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete_dlp_job]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        rpc(
            request, retry=retry, timeout=timeout, metadata=metadata,
        )

    def cancel_dlp_job(
        self,
        request: dlp.CancelDlpJobRequest = None,
        *,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> None:
        r"""Starts asynchronous cancellation on a long-running
        DlpJob. The server makes a best effort to cancel the
        DlpJob, but success is not guaranteed.
        See https://cloud.google.com/dlp/docs/inspecting-storage
        and https://cloud.google.com/dlp/docs/compute-risk-
        analysis to learn more.

        Args:
            request (google.cloud.dlp_v2.types.CancelDlpJobRequest):
                The request object. The request message for canceling a
                DLP job.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        # Create or coerce a protobuf request object.
        # Minor optimization to avoid making a copy if the user passes
        # in a dlp.CancelDlpJobRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, dlp.CancelDlpJobRequest):
            request = dlp.CancelDlpJobRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.cancel_dlp_job]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        rpc(
            request, retry=retry, timeout=timeout, metadata=metadata,
        )

    def create_stored_info_type(
        self,
        request: dlp.CreateStoredInfoTypeRequest = None,
        *,
        parent: str = None,
        config: dlp.StoredInfoTypeConfig = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> dlp.StoredInfoType:
        r"""Creates a pre-built stored infoType to be used for
        inspection. See
        https://cloud.google.com/dlp/docs/creating-stored-
        infotypes to learn more.

        Args:
            request (google.cloud.dlp_v2.types.CreateStoredInfoTypeRequest):
                The request object. Request message for
                CreateStoredInfoType.
            parent (str):
                Required. Parent resource name.

                The format of this value varies depending on the scope
                of the request (project or organization) and whether you
                have `specified a processing
                location <https://cloud.google.com/dlp/docs/specifying-location>`__:

                -  Projects scope, location specified:
                   ``projects/``\ PROJECT_ID\ ``/locations/``\ LOCATION_ID
                -  Projects scope, no location specified (defaults to
                   global): ``projects/``\ PROJECT_ID
                -  Organizations scope, location specified:
                   ``organizations/``\ ORG_ID\ ``/locations/``\ LOCATION_ID
                -  Organizations scope, no location specified (defaults
                   to global): ``organizations/``\ ORG_ID

                The following example ``parent`` string specifies a
                parent project with the identifier ``example-project``,
                and specifies the ``europe-west3`` location for
                processing data:

                ::

                    parent=projects/example-project/locations/europe-west3

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            config (google.cloud.dlp_v2.types.StoredInfoTypeConfig):
                Required. Configuration of the
                storedInfoType to create.

                This corresponds to the ``config`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dlp_v2.types.StoredInfoType:
                StoredInfoType resource message that
                contains information about the current
                version and any pending updates.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, config])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a dlp.CreateStoredInfoTypeRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, dlp.CreateStoredInfoTypeRequest):
            request = dlp.CreateStoredInfoTypeRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if config is not None:
                request.config = config

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_stored_info_type]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    def update_stored_info_type(
        self,
        request: dlp.UpdateStoredInfoTypeRequest = None,
        *,
        name: str = None,
        config: dlp.StoredInfoTypeConfig = None,
        update_mask: field_mask_pb2.FieldMask = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> dlp.StoredInfoType:
        r"""Updates the stored infoType by creating a new
        version. The existing version will continue to be used
        until the new version is ready. See
        https://cloud.google.com/dlp/docs/creating-stored-
        infotypes to learn more.

        Args:
            request (google.cloud.dlp_v2.types.UpdateStoredInfoTypeRequest):
                The request object. Request message for
                UpdateStoredInfoType.
            name (str):
                Required. Resource name of organization and
                storedInfoType to be updated, for example
                ``organizations/433245324/storedInfoTypes/432452342`` or
                projects/project-id/storedInfoTypes/432452342.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            config (google.cloud.dlp_v2.types.StoredInfoTypeConfig):
                Updated configuration for the
                storedInfoType. If not provided, a new
                version of the storedInfoType will be
                created with the existing configuration.

                This corresponds to the ``config`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Mask to control which fields get
                updated.

                This corresponds to the ``update_mask`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dlp_v2.types.StoredInfoType:
                StoredInfoType resource message that
                contains information about the current
                version and any pending updates.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name, config, update_mask])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a dlp.UpdateStoredInfoTypeRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, dlp.UpdateStoredInfoTypeRequest):
            request = dlp.UpdateStoredInfoTypeRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name
            if config is not None:
                request.config = config
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.update_stored_info_type]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    def get_stored_info_type(
        self,
        request: dlp.GetStoredInfoTypeRequest = None,
        *,
        name: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> dlp.StoredInfoType:
        r"""Gets a stored infoType.
        See https://cloud.google.com/dlp/docs/creating-stored-
        infotypes to learn more.

        Args:
            request (google.cloud.dlp_v2.types.GetStoredInfoTypeRequest):
                The request object. Request message for
                GetStoredInfoType.
            name (str):
                Required. Resource name of the organization and
                storedInfoType to be read, for example
                ``organizations/433245324/storedInfoTypes/432452342`` or
                projects/project-id/storedInfoTypes/432452342.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dlp_v2.types.StoredInfoType:
                StoredInfoType resource message that
                contains information about the current
                version and any pending updates.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a dlp.GetStoredInfoTypeRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, dlp.GetStoredInfoTypeRequest):
            request = dlp.GetStoredInfoTypeRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_stored_info_type]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    def list_stored_info_types(
        self,
        request: dlp.ListStoredInfoTypesRequest = None,
        *,
        parent: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListStoredInfoTypesPager:
        r"""Lists stored infoTypes.
        See https://cloud.google.com/dlp/docs/creating-stored-
        infotypes to learn more.

        Args:
            request (google.cloud.dlp_v2.types.ListStoredInfoTypesRequest):
                The request object. Request message for
                ListStoredInfoTypes.
            parent (str):
                Required. Parent resource name.

                The format of this value varies depending on the scope
                of the request (project or organization) and whether you
                have `specified a processing
                location <https://cloud.google.com/dlp/docs/specifying-location>`__:

                -  Projects scope, location specified:
                   ``projects/``\ PROJECT_ID\ ``/locations/``\ LOCATION_ID
                -  Projects scope, no location specified (defaults to
                   global): ``projects/``\ PROJECT_ID
                -  Organizations scope, location specified:
                   ``organizations/``\ ORG_ID\ ``/locations/``\ LOCATION_ID
                -  Organizations scope, no location specified (defaults
                   to global): ``organizations/``\ ORG_ID

                The following example ``parent`` string specifies a
                parent project with the identifier ``example-project``,
                and specifies the ``europe-west3`` location for
                processing data:

                ::

                    parent=projects/example-project/locations/europe-west3

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dlp_v2.services.dlp_service.pagers.ListStoredInfoTypesPager:
                Response message for
                ListStoredInfoTypes.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a dlp.ListStoredInfoTypesRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, dlp.ListStoredInfoTypesRequest):
            request = dlp.ListStoredInfoTypesRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_stored_info_types]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListStoredInfoTypesPager(
            method=rpc, request=request, response=response, metadata=metadata,
        )

        # Done; return the response.
        return response

    def delete_stored_info_type(
        self,
        request: dlp.DeleteStoredInfoTypeRequest = None,
        *,
        name: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> None:
        r"""Deletes a stored infoType.
        See https://cloud.google.com/dlp/docs/creating-stored-
        infotypes to learn more.

        Args:
            request (google.cloud.dlp_v2.types.DeleteStoredInfoTypeRequest):
                The request object. Request message for
                DeleteStoredInfoType.
            name (str):
                Required. Resource name of the organization and
                storedInfoType to be deleted, for example
                ``organizations/433245324/storedInfoTypes/432452342`` or
                projects/project-id/storedInfoTypes/432452342.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a dlp.DeleteStoredInfoTypeRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, dlp.DeleteStoredInfoTypeRequest):
            request = dlp.DeleteStoredInfoTypeRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete_stored_info_type]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        rpc(
            request, retry=retry, timeout=timeout, metadata=metadata,
        )

    def hybrid_inspect_dlp_job(
        self,
        request: dlp.HybridInspectDlpJobRequest = None,
        *,
        name: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> dlp.HybridInspectResponse:
        r"""Inspect hybrid content and store findings to a job.
        To review the findings inspect the job. Inspection will
        occur asynchronously.
        Early access feature is in a pre-release state and might
        change or have limited support. For more information,
        see
        https://cloud.google.com/products#product-launch-stages.

        Args:
            request (google.cloud.dlp_v2.types.HybridInspectDlpJobRequest):
                The request object. Request to search for potentially
                sensitive info in a custom location.
            name (str):
                Required. Resource name of the job to execute a hybrid
                inspect on, for example
                ``projects/dlp-test-project/dlpJob/53234423``.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dlp_v2.types.HybridInspectResponse:
                Quota exceeded errors will be thrown
                once quota has been met.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a dlp.HybridInspectDlpJobRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, dlp.HybridInspectDlpJobRequest):
            request = dlp.HybridInspectDlpJobRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.hybrid_inspect_dlp_job]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    def finish_dlp_job(
        self,
        request: dlp.FinishDlpJobRequest = None,
        *,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> None:
        r"""Finish a running hybrid DlpJob. Triggers the
        finalization steps and running of any enabled actions
        that have not yet run. Early access feature is in a pre-
        release state and might change or have limited support.
        For more information, see
        https://cloud.google.com/products#product-launch-stages.

        Args:
            request (google.cloud.dlp_v2.types.FinishDlpJobRequest):
                The request object. The request message for finishing a
                DLP hybrid job.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        # Create or coerce a protobuf request object.
        # Minor optimization to avoid making a copy if the user passes
        # in a dlp.FinishDlpJobRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, dlp.FinishDlpJobRequest):
            request = dlp.FinishDlpJobRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.finish_dlp_job]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        rpc(
            request, retry=retry, timeout=timeout, metadata=metadata,
        )


try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution("google-cloud-dlp",).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


__all__ = ("DlpServiceClient",)
