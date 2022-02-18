PIPELINE_NAME: str = 'pipelineName'
PIPELINE_TYPE: str = 'pipelineType'
STEP_NAME: str = 'stepName'

TERMINATION_CHECK: str = 'terminationCheck'

TIME: str = 'time'
ESTIMATED_START_TIME: str = 'EST'
ESTIMATED_FINISH_TIME: str = 'EFT'
TERMINATION_TIME: str = 'TT'

JOB: str = 'job'
JOB_ORDER: str = 'order'
JOB_NAME: str = 'name'
JOB_RESOURCE: str = 'resource'
JOB_ARCHITECTURE: str = 'architecture'
JOB_ELASTICITY_CONTROLLER_MODE: str = 'elasticityControllerMode'
JOB_DOCKER_IMAGE: str = 'dockerImage'
JOB_DOCKER_CREDENTIALS: str = 'dockerCredentialsUsing'
JOB_DOCKER_USERNAME: str = 'dockerUsername'
JOB_DOCKER_PASSWORD: str = 'dockerPassword'  # yikes
JOB_DOCKER_CUSTOM_REGISTRY: str = 'dockerCustomRegistry'
JOB_REGISTRY: str = 'dockerRegistry'
JOB_REQUIREMENTS: str = 'requirement'
JOB_VIRTUAL_CPUS: str = 'vCPUs'
JOB_RAM: str = 'ram'
JOB_STORAGE: str = 'storage'
JOB_HEALTH_CHECK: str = 'healthCheck'
JOB_TERMINATION_CHECK: str = 'terminationCheck'
JOB_COMMAND: str = 'command'
JOB_ENVIRONMENT_VARIABLES: str = 'environmentalVariables'
JOB_NUM_WORKERS: str = 'numWorkers'

JOB_EXPOSED_INTERFACES: str = 'exposedInterfaces'
JOB_EXPOSED_INTERFACES_NAME: str = 'name'
JOB_EXPOSED_INTERFACES_PORT: str = 'port'
JOB_EXPOSED_INTERFACES_TYPE: str = 'interfaceType'
JOB_EXPOSED_INTERFACES_TRANSMISSION_PROTOCOL: str = 'transmissionProtocol'

JOB_REQUIRED_INTERFACES: str = 'requiredInterfaces'
JOB_PLUGIN: str = 'plugin'
JOB_DEVICES: str = 'devices'
JOB_VOLUMES: str = 'volumes'
JOB_LABEL: str = 'label'
JOB_HOSTNAME: str = 'hostname'
JOB_CAPABILITY_DROPS: str = 'capabilityDrops'
JOB_CAPABILITY_ADDS: str = 'capabilityAdds'
JOB_ULIMIT_MEMLOCK_SOFT: str = 'ulimitMemlockSoft'
JOB_ULIMIT_MEMLOCK_HARD: str = 'ulimitMemlockHard'
JOB_NETWORK_MODE_HOST: str = 'networkModeHost'
JOB_PRIVILEGE: str = 'privilege'

job_keys: list = [
    JOB, JOB_ORDER,
    JOB_NAME,
    JOB_RESOURCE,
    JOB_ARCHITECTURE,
    JOB_ELASTICITY_CONTROLLER_MODE,
    JOB_DOCKER_IMAGE,
    JOB_DOCKER_CREDENTIALS,
    JOB_DOCKER_USERNAME,
    JOB_DOCKER_PASSWORD,   # yikes
    JOB_DOCKER_CUSTOM_REGISTRY,
    JOB_REGISTRY,
    JOB_REQUIREMENTS,
    JOB_VIRTUAL_CPUS,
    JOB_RAM, JOB_STORAGE,
    JOB_HEALTH_CHECK,
    JOB_TERMINATION_CHECK,
    JOB_COMMAND,
    JOB_ENVIRONMENT_VARIABLES,
    JOB_NUM_WORKERS,

    JOB_EXPOSED_INTERFACES,
    JOB_EXPOSED_INTERFACES_NAME,
    JOB_EXPOSED_INTERFACES_PORT,
    JOB_EXPOSED_INTERFACES_TYPE,
    JOB_EXPOSED_INTERFACES_TRANSMISSION_PROTOCOL,

    JOB_REQUIRED_INTERFACES,
    JOB_PLUGIN,
    JOB_DEVICES,
    JOB_VOLUMES,
    JOB_LABEL,
    JOB_HOSTNAME,
    JOB_CAPABILITY_DROPS,
    JOB_CAPABILITY_ADDS,
    JOB_ULIMIT_MEMLOCK_SOFT,
    JOB_ULIMIT_MEMLOCK_HARD,
    JOB_NETWORK_MODE_HOST,
    JOB_PRIVILEGE]
