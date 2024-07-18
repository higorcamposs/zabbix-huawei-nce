output = JSON.parse(value).map(function(faults){
    return {
            "{#LASTCHANGE}": faults["resource-alarm-parameters"]["last-changed"],
            "{#PERCEIVEDSEVERITY}": faults["resource-alarm-parameters"]["perceived-severity"],
            "{#EVENTTYPE}": faults["x733-alarm-parameters"]["event-type"],
            "{#ID}": faults["alarm-parameters"]["alarm-serial-number"],
            "{#NATIVEPROBABLECAUSE}": faults["alarm-parameters"]["native-probable-cause"],
            "{#REPAIRACTION}": faults["alarm-parameters"]["repair-action"],
            "{#PROBABLECAUSE}": faults["alarm-parameters"]["probable-cause"],
            "{#NENAME}": faults["alarm-parameters"]["ne-name"],
            "{#IPADDRESS}": faults["alarm-parameters"]["ip-address"]
        };
    });
    return JSON.stringify({"data": output})