"""Entry point for GCP Functions."""

{% if cookiecutter.trigger_type == 'HTTP' -%}
from typing import Any
{% elif cookiecutter.trigger_type == 'Cloud Pub/Sub' -%}
import base64
import json
from typing import Any, Dict
{% else -%}
from typing import Any, Dict
{% endif -%}

from {{cookiecutter.project_slug}}.pipeline import main


{% if cookiecutter.trigger_type == 'HTTP' -%}
def run_pipeline(request: Any) -> str:
    """HTTP Cloud Function.

    Offical docs: https://cloud.google.com/functions/docs/calling/http

    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>

    Returns:
        str: HTTP Response. Note this is REQUIRED for HTTP triggers to deemed successful.

    """
    # Read in request data
    message = request.get_json()

    # Open in request data as pipeline arguments
    main(**message)
{% elif cookiecutter.trigger_type == 'Cloud Pub/Sub' -%}
def run_pipeline(event: Dict[str, Any], context: Context) -> None:
    """Triggered from a message written to a PubSub topic.

    Official docs: https://cloud.google.com/functions/docs/calling/pubsub
    Scheduler docs: https://cloud.google.com/scheduler/docs/tut-pub-sub

    Args:
        event (dict): The dictionary with data specific to this type of event. The `@type` field
                maps to `type.googleapis.com/google.pubsub.v1.PubsubMessage`. The `data` field
                maps to the PubsubMessage data in a base64-encoded string. The `attributes` field
                maps to the PubsubMessage attributes if any is present.
        context (google.cloud.functions.Context): Metadata of triggering event including `event_id`
                which maps to the PubsubMessage messageId, `timestamp` which maps to the
                PubsubMessage publishTime, `event_type` which maps to
                `google.pubsub.topic.publish`, and `resource` which is a dictionary that describes
                the service API endpoint pubsub.googleapis.com, the triggering topic's name, and
                the triggering event type `type.googleapis.com/google.pubsub.v1.PubsubMessage`.

    """
    payload = base64.b64decode(event["data"]).decode("utf-8")
    pubsub_message = json.loads(payload)

    main(**pubsub_message)
{% elif cookiecutter.trigger_type == 'Cloud Storage' -%}
def run_pipeline(event: Dict[str, Any], context: Any) -> None:
    """Triggered by a change to a Cloud Storage bucket.

    Official docs: https://cloud.google.com/functions/docs/calling/storage

    Important attributes from event:
        "bucket": Name of the bucket.
        "name": Name of the file.

    Args:
        event (dict): The dictionary with data specific to this type of event.
                       The `data` field contains a description of the event in
                       the Cloud Storage `object` format described here:
                       https://cloud.google.com/storage/docs/json_api/v1/objects#resource
        context (google.cloud.functions.Context): Metadata of triggering event.

    """
    main(**event)
{% elif cookiecutter.trigger_type == 'Cloud Firestore' -%}
def run_pipeline(event: Dict[str, Any], context: Any) -> None:
    """Triggered by a change to a Cloud Firestore document.

    Official docs: https://cloud.google.com/functions/docs/calling/cloud-firestore

    Important attributes from event:
        "oldValue": Document snapshot before the change.
        "value": Document snapshot after the change.

    Important attributes from context:
        context.resource: Name of the Cloud Firestore document.

    Args:
         event (Dict[str, Any]): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.

    """
    main(**event)
{% endif -%}
