# esphome
[ESPHome](https://esphome.io/) firmware for IoT Devices.

Contains configurations for

* [Sonoff S31 Smart Plug with Energy Monitoring](https://sonoff.tech/en-us/products/sonoff-s31-s31-lite-compact-design-smart-plug-with-energy-monitoring-us-type): measures electric energy use.

* [Kincody KC868-AI](https://www.kincony.com/esp32-input-module.html): brings wired door and window sensors into the 21st century.

* [BT Proxy on ESP32 Dev](https://www.espressif.com/en/products/devkits/esp32-devkitc/overview): used with the HACS integration [Bermuda BLE Trilateration](https://github.com/agittins/bermuda) as described in [ESPHome room presence detection](https://www.homeautomationguy.io/blog/room-location-detection-with-bermuda-and-home-assistant-8f94b).

## FAQ

* If you get `ERROR Running command failed: Failed to connect to ESP32: Wrong boot 
mode detected (0x13)! The chip needs to be in download mode.`, then bring 
`GPIO0` down (press BOOT), while the ESPHome starts to upload the binary 
(and drives RST to reset the device). Then let go. [Espressif](https://docs.espressif.com/projects/esptool/en/latest/esp32/advanced-topics/boot-mode-selection.html)

* The cheapest ESP32 modules with case are probably labeled `Atom` at M5Stack. US$7.50 when I last checked.
