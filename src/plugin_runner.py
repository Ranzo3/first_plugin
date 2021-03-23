from dlpx.virtualization.platform import Mount, MountSpecification, Plugin

from generated.definitions import (
    RepositoryDefinition,
    SourceConfigDefinition,
    SnapshotDefinition,
)

plugin = Plugin()


#
# Below is an example of the repository discovery operation.
#
# NOTE: The decorators are defined on the 'plugin' object created above.
#
# Mark the function below as the operation that does repository discovery.
@plugin.discovery.repository()
def repository_discovery(source_connection):
    #
    # This is an object generated from the repositoryDefinition schema.
    # In order to use it locally you must run the 'build -g' command provided
    # by the SDK tools from the plugin's root directory.
    #

    return [RepositoryDefinition(name='e0696a23-4b64-483c-808a-35bd2c9571e3')]


@plugin.discovery.source_config()
def source_config_discovery(source_connection, repository):
    #
    # To have automatic discovery of source configs, return a list of
    # SourceConfigDefinitions similar to the list of
    # RepositoryDefinitions above.
    #

    return []


@plugin.linked.post_snapshot()
def linked_post_snapshot(staged_source,
                         repository,
                         source_config,
                         optional_snapshot_parameters):
    return SnapshotDefinition()


@plugin.linked.mount_specification()
def linked_mount_specification(staged_source, repository):
    mount_path = "/tmp/dlpx_staged_mounts/{}".format(staged_source.guid)
    environment = staged_source.staged_connection.environment
    mounts = [Mount(environment, mount_path)]

    return MountSpecification(mounts)


@plugin.virtual.configure()
def configure(virtual_source, snapshot, repository):
    return SourceConfigDefinition(name=virtual_source.guid)


@plugin.virtual.reconfigure()
def reconfigure(virtual_source, repository, source_config, snapshot):
    return SourceConfigDefinition(name=virtual_source.guid)


@plugin.virtual.post_snapshot()
def virtual_post_snapshot(virtual_source, repository, source_config):
    return SnapshotDefinition()


@plugin.virtual.mount_specification()
def virtual_mount_specification(virtual_source, repository):
    mount_path = "/tmp/dlpx_staged_mounts/{}".format(virtual_source.guid)
    mounts = [Mount(virtual_source.connection.environment, mount_path)]

    return MountSpecification(mounts)
