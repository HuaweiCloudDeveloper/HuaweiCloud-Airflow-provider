from __future__ import annotations
from typing import Any

import json

from airflow.hooks.base import BaseHook

class HuaweiBaseHook(BaseHook):
    
    conn_name_attr = "huaweicloud_conn_id"
    default_conn_name = "huaweicloud_default"
    conn_type = "huaweicloud"
    hook_name = "Huawei Cloud"
    
    def __init__(self,
                 huaweicloud_conn_id="huaweicloud_default",
                 region=None,
                 project_id=None,
                 *args,
                 **kwargs) -> None:
        self.huaweicloud_conn_id = huaweicloud_conn_id
        self.preferred_region = region
        self.preferred_project_id = project_id
        self.conn = self.get_connection(self.huaweicloud_conn_id)
        super().__init__(*args, **kwargs)
    
    def get_default_project_id(self) -> str | None:
        """
        Gets project_id from the extra_config option in connection.
        """
        
        if hasattr(self, "preferred_project_id") and self.preferred_project_id is not None:
            return self.preferred_project_id
        if self.conn.extra_dejson.get('project_id', None) is not None:
            return self.conn.extra_dejson.get('project_id', None)
        raise Exception(f"No project_id is specified for connection: {self.huaweicloud_conn_id}")
    
    def get_region(self) -> str:
        """Returns region for the hook."""
        if hasattr(self, "preferred_region") and self.preferred_region is not None:
            return self.preferred_region
        if self.conn.extra_dejson.get('region', None) is not None:
            return self.conn.extra_dejson.get('region', None)
        raise Exception(f"No region is specified for connection")
    
    @staticmethod
    def get_ui_field_behaviour() -> dict[str, Any]:
        """Returns custom UI field behaviour for Huawei Cloud Connection."""
        return {
            "hidden_fields": ["host", "schema", "port"],
            "relabeling": {
                "login": "Huawei Cloud Access Key ID",
                "password": "Huawei Cloud Secret Access Key",
            },
            "placeholders": {
                "login": "AKIAIOSFODNN7EXAMPLE",
                "password": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
                "extra": json.dumps(
                    {
                        "region": "ap-southeast-3"
                    },
                    indent=2,
                ),
            },
        }
    
    def test_connection(self):
        try:
            return True, self.get_region()
        except Exception as e:
            return False, str(f"{type(e).__name__!r} error occurred while testing connection: {e}")