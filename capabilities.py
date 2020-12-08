import enum


class _accelerationSensor(enum.Enum):
    ACTIVE = 'active'
    INACTIVE = 'inactive'

class _activityLightingMode(enum.Enum):
    READING = 'reading'
    WRITING = 'writing'
    COMPUTER ='computer'
    NIGHT = 'night'

class _airConditionerMode(enum.Enum):
    AUTO = 'auto'
    COOL = 'cool'
    DRY = 'dry'
    COOLCLEAN = 'coolClean'
    DRYCLEAN = 'dryclean'
    FANONLY = 'fanOnly'
    HEAT = 'heat'
    HEATCLEAN = 'heatclean'

class _airQualitySensor(enum.Enum):
    NUMVALUE = 'NUMVALUE'

class _alarm(enum.Enum):
    STROBING = 'strobe'
    SIREN = 'siren'
    OFF = 'off'
    BOTH = 'strobe and sound'

class _audioMute(enum.Enum):
    MUTED = 'muted'
    UNMUTED = 'unmuted'

class _audioVolume(enum.Enum):
    NUMVALUE = 'NUMVALUE'

class _battery(enum.Enum):
    NUMVALUE = 'NUMVALUE'

class _bodyMassIndexMeasurement(enum.Enum):
    NUMVALUE = 'NUMVALUE'

class _bodyWeightMeasurement(enum.Enum):
    NUMVALUE = 'NUMVALUE'

class _button(enum.Enum):
    PUSHED = 'pushed'
    HELD = 'held'
    DOUBLE = 'double'
    PUSHED_2X = 'pushed'
    PUSHED_3X = 'pushed'
    PUSHED_4X = 'pushed'
    PUSHED_5X = 'pushed'
    PUSHED_6X = 'pushed'
    DOWN = 'down'
    UP = 'up'
    UP_HOLD = 'up and held'
    NUM

class Capabilities(enum.Enum):
    # basic data types
    STRING = 'string'
    NUMBER = 'number'
    VECTORS = 'vectors'
    ST_ENUM = 'st-enum'
    ST_DY_ENUM = 'st_dy_enum'
    COLOR_MAP = 'color_map'
    JSON_OBJECT = 'json_object'
    DATE = 'date'

    # devices capabilities
    accelerationSensor = _accelerationSensor
    activityLightingMode = _activityLightingMode
    airConditionerMode = _airConditionerMode
    airQualitySensor = _airQualitySensor
    alarm = _alarm
    audioMute = _audioMute
    audioVolume = _audioVolume
    battery = _battery
    bodyMassIndexMeasurement = _bodyMassIndexMeasurement
    bodyWeightMeasurement = _bodyWeightMeasurement
    button = _button
    carbonDioxideMeasurement = _carbonDioxideMeasurement
    carbonMonoxideDetector = _carbonMonoxideDetector
    carbonMonoxideMeasurement = _carbonMonoxideMeasurement
    colorControl = _colorControl
    colorTemperature = _colorTemperature
    contactSensor = _contactSensor
    dishwasherMode = _dishwasherMode
    dishwasherOperatingState = _dishwasherOperatingState
    doorControl = _doorControl
    dryerMode = _dryerMode
    dryerOperatingState = _dryerOperatingState
    dustSensor = _dustSensor
    energyMeter = _energyMeter
    equivalentCarbonDioxideMeasurement = _equivalentCarbonDioxideMeasurement
    fanSpeed = _fanSpeed
    filterStatus = _filterStatus
    formaldehydeMeasurement = _formaldehydeMeasurement
    garageDoorControl = _garageDoorControl
    illuminanceMeasurement = _illuminanceMeasurement
    infraredLevel = _infraredLevel
    lock = _lock
    mediaInputSource = _mediaInputSource
    mediaPlaybackRepeat = _mediaPlaybackRepeat
    mediaPlaybackShuffle = _mediaPlaybackShuffle
    mediaPlayback = _mediaPlayback
    motionSensor = _motionSensor
    odorSensor = _odorSensor
    ovenMode = _ovenMode
    ovenOperatingState = _ovenOperatingState
    ovenSetpoint = _ovenSetpoint
    powerMeter = _powerMeter
    powerSource = _powerSource
    presenceSensor = _presenceSensor
    rapidCooling = _rapidCooling
    refrigerationSetpoint = _refrigerationSetpoint
    relativeHumidityMeasurement = _relativeHumidityMeasurement
    robotCleanerCleaningMode = _robotCleanerCleaningMode
    robotCleanerMovement = _robotCleanerMovement
    robotCleanerTurboMode = _robotCleanerTurboMode
    signalStrength = _signalStrength
    smokeDetector = _smokeDetector
    soundSensor = _soundSensor
    switchLevel = _switchLevel
    switch = _switch
    tamperAlert = _tamperAlert
    temperatureMeasurement = _temperatureMeasurement
    thermostatCoolingSetpoint = _thermostatCoolingSetpoint
    thermostatFanMode = _thermostatFanMode
    thermostatHeatingSetpoint = _thermostatHeatingSetpoint
    thermostatMode = _thermostatMode
    thermostatOperatingState = _thermostatOperatingState
    thermostatSetpoint = _thermostatSetpoint
    tone = _tone
    tvChannel = _tvChannel
    tvocMeasurement = _tvocMeasurement
    ultravioletIndex = _ultravioletIndex
    valve = _valve
    voltageMeasurement = _voltageMeasurement
    washerMode = _washerMode
    washerOperatingState = _washerOperatingState
    waterSensor = _waterSensor
    windowShade = _windowShade


    

