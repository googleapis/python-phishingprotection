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
import functools
import re
from typing import Dict, Sequence, Tuple, Type, Union
import pkg_resources

import google.api_core.client_options as ClientOptions  # type: ignore
from google.api_core import exceptions as core_exceptions  # type: ignore
from google.api_core import gapic_v1  # type: ignore
from google.api_core import retry as retries  # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.phishingprotection_v1beta1.types import phishingprotection
from .transports.base import (
    PhishingProtectionServiceV1Beta1Transport,
    DEFAULT_CLIENT_INFO,
)
from .transports.grpc_asyncio import (
    PhishingProtectionServiceV1Beta1GrpcAsyncIOTransport,
)
from .client import PhishingProtectionServiceV1Beta1Client


class PhishingProtectionServiceV1Beta1AsyncClient:
    """Service to report phishing URIs."""

    _client: PhishingProtectionServiceV1Beta1Client

    DEFAULT_ENDPOINT = PhishingProtectionServiceV1Beta1Client.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = PhishingProtectionServiceV1Beta1Client.DEFAULT_MTLS_ENDPOINT

    common_billing_account_path = staticmethod(
        PhishingProtectionServiceV1Beta1Client.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        PhishingProtectionServiceV1Beta1Client.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(
        PhishingProtectionServiceV1Beta1Client.common_folder_path
    )
    parse_common_folder_path = staticmethod(
        PhishingProtectionServiceV1Beta1Client.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        PhishingProtectionServiceV1Beta1Client.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        PhishingProtectionServiceV1Beta1Client.parse_common_organization_path
    )
    common_project_path = staticmethod(
        PhishingProtectionServiceV1Beta1Client.common_project_path
    )
    parse_common_project_path = staticmethod(
        PhishingProtectionServiceV1Beta1Client.parse_common_project_path
    )
    common_location_path = staticmethod(
        PhishingProtectionServiceV1Beta1Client.common_location_path
    )
    parse_common_location_path = staticmethod(
        PhishingProtectionServiceV1Beta1Client.parse_common_location_path
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
            PhishingProtectionServiceV1Beta1AsyncClient: The constructed client.
        """
        return PhishingProtectionServiceV1Beta1Client.from_service_account_info.__func__(PhishingProtectionServiceV1Beta1AsyncClient, info, *args, **kwargs)  # type: ignore

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
            PhishingProtectionServiceV1Beta1AsyncClient: The constructed client.
        """
        return PhishingProtectionServiceV1Beta1Client.from_service_account_file.__func__(PhishingProtectionServiceV1Beta1AsyncClient, filename, *args, **kwargs)  # type: ignore

    from_service_account_json = from_service_account_file

    @property
    def transport(self) -> PhishingProtectionServiceV1Beta1Transport:
        """Returns the transport used by the client instance.

        Returns:
            PhishingProtectionServiceV1Beta1Transport: The transport used by the client instance.
        """
        return self._client.transport

    get_transport_class = functools.partial(
        type(PhishingProtectionServiceV1Beta1Client).get_transport_class,
        type(PhishingProtectionServiceV1Beta1Client),
    )

    def __init__(
        self,
        *,
        credentials: ga_credentials.Credentials = None,
        transport: Union[
            str, PhishingProtectionServiceV1Beta1Transport
        ] = "grpc_asyncio",
        client_options: ClientOptions = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the phishing protection service v1 beta1 client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.PhishingProtectionServiceV1Beta1Transport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (ClientOptions): Custom options for the client. It
                won't take effect if a ``transport`` instance is provided.
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

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        self._client = PhishingProtectionServiceV1Beta1Client(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

    async def report_phishing(
        self,
        request: phishingprotection.ReportPhishingRequest = None,
        *,
        parent: str = None,
        uri: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> phishingprotection.ReportPhishingResponse:
        r"""Reports a URI suspected of containing phishing content to be
        reviewed. Once the report review is complete, its result can be
        found in the Cloud Security Command Center findings dashboard
        for Phishing Protection. If the result verifies the existence of
        malicious phishing content, the site will be added the to
        `Google's Social Engineering
        lists <https://support.google.com/webmasters/answer/6350487/>`__
        in order to protect users that could get exposed to this threat
        in the future.

        Args:
            request (:class:`google.cloud.phishingprotection_v1beta1.types.ReportPhishingRequest`):
                The request object. The ReportPhishing request message.
            parent (:class:`str`):
                Required. The name of the project for which the report
                will be created, in the format
                "projects/{project_number}".

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            uri (:class:`str`):
                Required. The URI that is being
                reported for phishing content to be
                analyzed.

                This corresponds to the ``uri`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.phishingprotection_v1beta1.types.ReportPhishingResponse:
                The ReportPhishing (empty) response
                message.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, uri])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = phishingprotection.ReportPhishingRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if uri is not None:
            request.uri = uri

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.report_phishing,
            default_timeout=600.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response


try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution(
            "google-cloud-phishingprotection",
        ).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


__all__ = ("PhishingProtectionServiceV1Beta1AsyncClient",)
