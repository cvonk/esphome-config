# See: https://esphome.io/guides/contributing.html#extras

import esphome.codegen as cg
import esphome.config_validation as cv
from esphome import pins
from esphome.const import (
    CONF_ID,
    CONF_FREQUENCY,
)

# Mark the component to depend on other components.
# If the user hasn’t explicitly added these components in their configuration, a validation error will be generated.
DEPENDENCIES = [ ]
# Automatically load a component if the user hasn’t added it manually
AUTO_LOAD = [ ]
# Mark this component to accept an array of configurations.
# If this is an integer instead of a boolean, validation will only permit the given number of entries.
MULTI_CONF = False

# GitHub usernames or team names of people that are responsible for this component
CODEOWNERS = ["@vinsce"]

# Define constants for configuration keys
CONF_RS485_RX_PIN = "rs485_rx_pin"
CONF_RS485_TX_PIN = "rs485_tx_pin"
CONF_RS485_RTS_PIN = "rs485_rts_pin"
CONF_RS485_TIMEOUT = "rs485_timeout"
CONF_DBGLVL_DATALINK = "dbglvl_datalink"
CONF_DBGLVL_NETWORK = "dbglvl_network"
CONF_DBGLVL_POOLSTATE = "dbglvl_poolstate"
CONF_DBGLVL_POOLTASK = "dbglvl_pooltask"
CONF_DBGLVL_MQTTTASK = "dbglvl_mqtttask"
CONF_DBGLVL_HASSTASK = "dbglvl_hasstask"
CONF_DBGLVL_HTTPD = "dbglvl_httpd"
CONF_DBGLVL_IPC = "dbglvl_ipc"

# C++ namespace
ns = cg.esphome_ns.namespace("opnpool")
OPNpool = ns.class_("OPNpool", cg.Component)

# The configuration schema to validate the user config against
CONFIG_SCHEMA = cv.COMPONENT_SCHEMA.extend(
    {
        cv.GenerateID(): cv.declare_id(OPNpool),
        #cv.Required(CONF_NAME): cv.string,
        # 2BD review input/output pins
        cv.Required(CONF_RS485_RX_PIN): pins.gpio_output_pin_schema,  # Receive GPIO# on ESP32 that connects to RO on the RS-485 Transceiver
        cv.Required(CONF_RS485_TX_PIN): pins.gpio_output_pin_schema,  # Transmit GPIO# on ESP32 that connects to DI on the RS-485 Transceiver
        cv.Required(CONF_RS485_RTS_PIN): pins.gpio_output_pin_schema, # Request-To-Send GPIO# on ESP32 that connects to DE/!RE on the RS-485 Transceiver
        cv.Optional(CONF_RS485_TIMEOUT, default=100): cv.int_,        # Maximum time to wait for a byte on RS485 in milliseconds
        cv.Optional(CONF_DBGLVL_DATALINK, default=1): cv.int_,        # Datalink/RS485 layer debug level, 0 for no debug, 1 for errors only, 2 for all     
        cv.Optional(CONF_DBGLVL_NETWORK, default=1): cv.int_,         # Network layer debug level, 0 for no debug, 1 for errors only, 2 for all
        cv.Optional(CONF_DBGLVL_POOLSTATE, default=1): cv.int_,       # Poolstate debug level, 0 for no debug, 1 for errors only, 2 for all
        cv.Optional(CONF_DBGLVL_POOLTASK, default=1): cv.int_,        # Pool task debug level, 0 for no debug, 1 for errors only, 2 for all
        cv.Optional(CONF_DBGLVL_MQTTTASK, default=1): cv.int_,        # MQTT task debug level, 0 for no debug, 1 for errors only, 2 for all
        cv.Optional(CONF_DBGLVL_HASSTASK, default=2): cv.int_,        # Home assistant task debug level, 0 for no debug, 1 for errors only, 2 for all
        cv.Optional(CONF_DBGLVL_HTTPD, default=1): cv.int_,           # HTTPd debug level, 0 for no debug, 1 for errors only, 2 for all
        cv.Optional(CONF_DBGLVL_IPC, default=0): cv.int_,             # IPC debug level, 0 for no debug, 1 for errors only, 2 for all
    }
)

async def to_code(config):
    rs485_rx_pin = await cg.gpio_pin_expression(config[CONF_RS485_RX_PIN])
    rs485_tx_pin = await cg.gpio_pin_expression(config[CONF_RS485_TX_PIN])
    rs485_rts_pin = await cg.gpio_pin_expression(config[CONF_RS485_RTS_PIN])
    rs485_timeout = config[CONF_RS485_TIMEOUT]
    dbglvl_datalink = config[CONF_DBGLVL_DATALINK]
    dbglvl_network = config[CONF_DBGLVL_NETWORK]
    dbglvl_poolstate = config[CONF_DBGLVL_POOLSTATE]
    dbglvl_pooltask = config[CONF_DBGLVL_POOLTASK]
    dbglvl_mqtttask = config[CONF_DBGLVL_MQTTTASK]
    dbglvl_hasstask = config[CONF_DBGLVL_HASSTASK]
    dbglvl_httpd = config[CONF_DBGLVL_HTTPD]
    dbglvl_ipc = config[CONF_DBGLVL_IPC]

    # Declare new component (object of type OPNpool)
    # Will create a new pointer:
    #   transceiver = new OPNpool::OPNpool();
    var = cg.new_Pvariable(config[CONF_ID], rs485_rx_pin, rs485_tx_pin, rs485_rts_pin,
                           rs485_timeout, dbglvl_datalink, dbglvl_network, dbglvl_poolstate,
                           dbglvl_pooltask, dbglvl_mqtttask, dbglvl_hasstask, dbglvl_httpd, dbglvl_ipc)

    # Configure and register the component:
    #   transceiver->set_update_interval(60000);
    #   transceiver->set_component_source("opnpool");
    #   App.register_component(transceiver);
    await cg.register_component(var, config)

    # cg.add is used to add a piece of code to the generated main.cpp
    #   transceiver->set_bandwidth(200);
    #cg.add(var.set_bandwidth(config[CONF_BANDWIDTH]))
    #cg.add(var.set_frequency(config[CONF_FREQUENCY]))