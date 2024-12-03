from ports.output.output_port import OutputPort
from google.cloud import pubsub_v1
import json
from domain.empleado import Empleado

class PubSubWriterAdapter(OutputPort):
    def __init__(self, project_id: str, topic_id: str):
        self.project_id = project_id
        self.topic_id = topic_id

    def escribir_empleado(self, empleado: Empleado) -> None:
        publisher = pubsub_v1.PublisherClient()
        topic_path = publisher.topic_path(self.project_id, self.topic_id)
        message_json = json.dumps(empleado.__dict__).encode("utf-8")
        future = publisher.publish(topic_path, message_json)