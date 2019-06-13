<H1>Ublox configuration loader.</H1> 

**Converts ASCI config file to binary format and sends to serial GPS**

Created for UBlox GPS modules lacking non-volitile storage so settings can be loaded on every start 

Usage:

  ```ubxcfg.py [UBlox Config File] [port] [baud_default] [baud_programed]```
  
  **Note:** Port configuration commands are postponed until last but they are not ordered so if a settings file causes the GPS serial port to be reconfigured then the remaining ports (eg UART2, USB & SPI) will fail to be configured; I'm only using UART1 so sorry for not caring about this issue.
