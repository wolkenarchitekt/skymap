let client = mqtt.connect(`ws://${location.hostname}:9001`); // Replace with your broker's URL or IP

client.on('connect', function () {
    console.log('Connected to MQTT broker');
    client.subscribe('traffic/#'); // Replace with the topic you want to subscribe to
});

client.on('message', function (topic, message) {
    let event = new CustomEvent("mqtt", {detail: message.toString()});
    document.dispatchEvent(event);
});
