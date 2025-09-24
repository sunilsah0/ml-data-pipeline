from feast import Entity, FeatureView, Field
from feast.types import Float32
from datetime import timedelta

customer = Entity(name="customer_id", join_keys=["customer_id"])

customer_features = FeatureView(
    name="customer_features",
    entities=[customer],
    ttl=timedelta(days=1),
    schema=[
        Field(name="avg_spent", dtype=Float32),
        Field(name="event_types", dtype=Float32),
    ],
    online=True,
)
