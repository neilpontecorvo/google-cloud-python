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
from typing import MutableMapping, MutableSequence

from google.protobuf import timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.talent.v4",
    manifest={
        "ClientEvent",
        "JobEvent",
    },
)


class ClientEvent(proto.Message):
    r"""An event issued when an end user interacts with the
    application that implements Cloud Talent Solution. Providing
    this information improves the quality of results for the API
    clients, enabling the service to perform optimally. The number
    of events sent must be consistent with other calls, such as job
    searches, issued to the service by the client.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        request_id (str):
            Strongly recommended for the best service experience.

            A unique ID generated in the API responses. It can be found
            in
            [ResponseMetadata.request_id][google.cloud.talent.v4.ResponseMetadata.request_id].
        event_id (str):
            Required. A unique identifier, generated by
            the client application.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Required. The timestamp of the event.
        job_event (google.cloud.talent_v4.types.JobEvent):
            An event issued when a job seeker interacts
            with the application that implements Cloud
            Talent Solution.

            This field is a member of `oneof`_ ``event``.
        event_notes (str):
            Notes about the event provided by recruiters
            or other users, for example, feedback on why a
            job was bookmarked.
    """

    request_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    event_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    job_event: "JobEvent" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="event",
        message="JobEvent",
    )
    event_notes: str = proto.Field(
        proto.STRING,
        number=9,
    )


class JobEvent(proto.Message):
    r"""An event issued when a job seeker interacts with the
    application that implements Cloud Talent Solution.

    Attributes:
        type_ (google.cloud.talent_v4.types.JobEvent.JobEventType):
            Required. The type of the event (see
            [JobEventType][google.cloud.talent.v4.JobEvent.JobEventType]).
        jobs (MutableSequence[str]):
            Required. The [job name(s)][google.cloud.talent.v4.Job.name]
            associated with this event. For example, if this is an
            [impression][google.cloud.talent.v4.JobEvent.JobEventType.IMPRESSION]
            event, this field contains the identifiers of all jobs shown
            to the job seeker. If this was a
            [view][google.cloud.talent.v4.JobEvent.JobEventType.VIEW]
            event, this field contains the identifier of the viewed job.

            The format is
            "projects/{project_id}/tenants/{tenant_id}/jobs/{job_id}",
            for example, "projects/foo/tenants/bar/jobs/baz".
    """

    class JobEventType(proto.Enum):
        r"""An enumeration of an event attributed to the behavior of the
        end user, such as a job seeker.

        Values:
            JOB_EVENT_TYPE_UNSPECIFIED (0):
                The event is unspecified by other provided
                values.
            IMPRESSION (1):
                The job seeker or other entity interacting
                with the service has had a job rendered in their
                view, such as in a list of search results in a
                compressed or clipped format. This event is
                typically associated with the viewing of a jobs
                list on a single page by a job seeker.
            VIEW (2):
                The job seeker, or other entity interacting with the
                service, has viewed the details of a job, including the full
                description. This event doesn't apply to the viewing a
                snippet of a job appearing as a part of the job search
                results. Viewing a snippet is associated with an
                [impression][google.cloud.talent.v4.JobEvent.JobEventType.IMPRESSION]).
            VIEW_REDIRECT (3):
                The job seeker or other entity interacting
                with the service performed an action to view a
                job and was redirected to a different website
                for job.
            APPLICATION_START (4):
                The job seeker or other entity interacting
                with the service began the process or
                demonstrated the intention of applying for a
                job.
            APPLICATION_FINISH (5):
                The job seeker or other entity interacting
                with the service submitted an application for a
                job.
            APPLICATION_QUICK_SUBMISSION (6):
                The job seeker or other entity interacting with the service
                submitted an application for a job with a single click
                without entering information. If a job seeker performs this
                action, send only this event to the service. Do not also
                send
                [JobEventType.APPLICATION_START][google.cloud.talent.v4.JobEvent.JobEventType.APPLICATION_START]
                or
                [JobEventType.APPLICATION_FINISH][google.cloud.talent.v4.JobEvent.JobEventType.APPLICATION_FINISH]
                events.
            APPLICATION_REDIRECT (7):
                The job seeker or other entity interacting
                with the service performed an action to apply to
                a job and was redirected to a different website
                to complete the application.
            APPLICATION_START_FROM_SEARCH (8):
                The job seeker or other entity interacting
                with the service began the process or
                demonstrated the intention of applying for a job
                from the search results page without viewing the
                details of the job posting. If sending this
                event, JobEventType.VIEW event shouldn't be
                sent.
            APPLICATION_REDIRECT_FROM_SEARCH (9):
                The job seeker, or other entity interacting with the
                service, performs an action with a single click from the
                search results page to apply to a job (without viewing the
                details of the job posting), and is redirected to a
                different website to complete the application. If a
                candidate performs this action, send only this event to the
                service. Do not also send
                [JobEventType.APPLICATION_START][google.cloud.talent.v4.JobEvent.JobEventType.APPLICATION_START],
                [JobEventType.APPLICATION_FINISH][google.cloud.talent.v4.JobEvent.JobEventType.APPLICATION_FINISH]
                or
                [JobEventType.VIEW][google.cloud.talent.v4.JobEvent.JobEventType.VIEW]
                events.
            APPLICATION_COMPANY_SUBMIT (10):
                This event should be used when a company
                submits an application on behalf of a job
                seeker. This event is intended for use by
                staffing agencies attempting to place
                candidates.
            BOOKMARK (11):
                The job seeker or other entity interacting
                with the service demonstrated an interest in a
                job by bookmarking or saving it.
            NOTIFICATION (12):
                The job seeker or other entity interacting
                with the service was sent a notification, such
                as an email alert or device notification,
                containing one or more jobs listings generated
                by the service.
            HIRED (13):
                The job seeker or other entity interacting
                with the service was employed by the hiring
                entity (employer). Send this event only if the
                job seeker was hired through an application that
                was initiated by a search conducted through the
                Cloud Talent Solution service.
            SENT_CV (14):
                A recruiter or staffing agency submitted an
                application on behalf of the candidate after
                interacting with the service to identify a
                suitable job posting.
            INTERVIEW_GRANTED (15):
                The entity interacting with the service (for
                example, the job seeker), was granted an initial
                interview by the hiring entity (employer). This
                event should only be sent if the job seeker was
                granted an interview as part of an application
                that was initiated by a search conducted through
                / recommendation provided by the Cloud Talent
                Solution service.
        """
        JOB_EVENT_TYPE_UNSPECIFIED = 0
        IMPRESSION = 1
        VIEW = 2
        VIEW_REDIRECT = 3
        APPLICATION_START = 4
        APPLICATION_FINISH = 5
        APPLICATION_QUICK_SUBMISSION = 6
        APPLICATION_REDIRECT = 7
        APPLICATION_START_FROM_SEARCH = 8
        APPLICATION_REDIRECT_FROM_SEARCH = 9
        APPLICATION_COMPANY_SUBMIT = 10
        BOOKMARK = 11
        NOTIFICATION = 12
        HIRED = 13
        SENT_CV = 14
        INTERVIEW_GRANTED = 15

    type_: JobEventType = proto.Field(
        proto.ENUM,
        number=1,
        enum=JobEventType,
    )
    jobs: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))