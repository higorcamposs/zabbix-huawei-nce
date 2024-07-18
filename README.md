# Zabbix Template for Huawei NCE Monitoring
---
**📢 If you have any considerations, suggestions, or questions, feel free to contact me! I am available to help.**

---
This template monitors the active alerts in the NCE.

The intention is to capture the current alarms to generate the same view in Zabbix, maintaining the integration flow.

## Template Contents
- 4 Macros
- 1 Item
- 1 Discovery
  - 1 Item prototype
  - 1 Trigger prototype

## Item
The item is of type "External Scripts", triggering the script getAlertsHuaweiNCE.py and passing the 4 macros as parameters:
> getAlertsHuaweiNCE.py[{$USER.API},{$PASS.API},{$URL.API},{$PORT.API}]

## Script
The script getAlertsHuaweiNCE.py receives the parameters sent by Zabbix. After performing validation, it generates a token for access and queries the active alerts. The return will be a JSON with all relevant data.

## Discovery
The discovery is configured to receive these data. It is of type "Item dependent", with the "Master item" being the item that triggers the external script. The "Preprocessing" prepares the JSON. There are 3 steps in the "Preprocessing steps":
1. The first and second steps clean the JSON.
2. The third step prepares the JSON to transform the keys into macros.

## Overrides
The "Overrides" are created to define the severities according to the received data. For example, if the value received is critical, the trigger will be set to high; if the value is warning, the trigger will be set to informational.

## Item Prototype
The "Item prototype" carries the severity value.

## Trigger Prototype
The "Trigger prototype" checks if the value is different from the status "cleared".

