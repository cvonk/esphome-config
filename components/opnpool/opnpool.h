#pragma once

#include <ELECHOUSE_CC1101_SRC_DRV.h>

#include "esphome/core/component.h"
#include <esphome/core/hal.h>

namespace esphome {
namespace opnpool {

class OPNpool : public Component {

 public:
   OPNpool(InternalGPIOPin *rs485_rx_pin, InternalGPIOPin *rs485_tx_pin, InternalGPIOPin *rs485_rts_pin,
           int rs485_timeout, int dbglvl_datalink, int dbglvl_network, int dbglvl_poolstate,
           int dbglvl_pooltask, int dbglvl_mqtttask, int dbglvl_hasstask, int dbglvl_httpd, int dbglvl_ipc);
   /* 
   void set_bandwidth(float bandwidth);
   void set_frequency(float frequency);
   */

   void setup() override;
   void dump_config() override;

  protected:
  InternalGPIOPin *RS485_RX_;
  InternalGPIOPin *RS485_TX_;
  InternalGPIOPin *RS485_RTS_;
  int RS485_TIMEOUT_;
  int DBGLVL_DATALINK_;
  int DBGLVL_NETWORK_;
  int DBGLVL_POOLSTATE_;
  int DBGLVL_POOLTASK_;
  int DBGLVL_MQTTTASK_;
  int DBGLVL_HASSTASK_;
  int DBGLVL_HTTPD_;
  int DBGLVL_IPC_;

  /*
  float bandwidth_;
  float frequency_;
  */
 
  float _moduleNumber;
};

}  // namespace cc1101
}  // namespace esphome
