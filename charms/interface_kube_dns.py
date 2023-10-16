from ops import CharmBase, Relation
from typing import List, Optional


class KubeDnsRequires:
    """Implements the Requires side of the kube-dns interface."""

    def __init__(self, charm: CharmBase, endpoint: str):
        self.charm = charm
        self.endpoint = endpoint

    @property
    def address(self) -> Optional[str]:
        return self.get_any_unit_data("sdn-ip")

    @property
    def domain(self) -> Optional[str]:
        return self.get_any_unit_data("domain")

    def get_any_unit_data(self, key):
        for relation in self.relations:
            for unit in relation.units:
                value = relation.data[unit].get(key)
                if value:
                    return value

    @property
    def port(self) -> Optional[int]:
        value = self.get_any_unit_data("port")
        if value:
            return int(value)

    @property
    def relations(self) -> List[Relation]:
        return self.charm.model.relations[self.endpoint]
