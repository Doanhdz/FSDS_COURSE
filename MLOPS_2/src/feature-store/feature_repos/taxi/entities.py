from feast import Entity

taxi = Entity(
    name="taxi",
    join_keys=["vendorid"],
    description="vendorid",
)
