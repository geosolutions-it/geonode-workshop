import os
import json
from django.apps import AppConfig

import logging

logger = logging.getLogger(__name__)


class MetadataConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "geonode_project.metadata"
    label = "project_metadata"

    def ready(self):
        from geonode.metadata.handlers.sparse import sparse_field_registry
        # Locate the schema file relative to this app
        current_dir = os.path.dirname(os.path.abspath(__file__))
        schema_path = os.path.join(current_dir, "schemas", "project_schema.json")
        
        if os.path.exists(schema_path):
            try:
                with open(schema_path, "r") as f:
                    schema_data = json.load(f)
                
                # Register each field in the GeoNode 5 Sparse Registry
                for property_name, subschema in schema_data.items():
                    # Only register if the handler is set to 'sparse'
                    if subschema.get("geonode:handler") == "sparse":
                        sparse_field_registry.register(property_name, subschema)
                        
                logger.info(f"Successfully registered {len(schema_data)} project metadata fields.")
            
            except Exception as e:
                logger.error(f"Failed to load custom project metadata schema: {e}")
        else:
            logger.warning(f"Metadata schema file not found at {schema_path}")
